from concurrent import futures
import grpc
import argparse
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2
import reddit_pb2_grpc as r_grpc
import utils.constants as Constants
import time


posts = Constants.POSTS
comments = Constants.COMMENTS


class RedditServicer(r_grpc.RedditServicer):
    def CreatePost(self, request, context):
        post = request.post        
        posts.append(post)
        return r_pb2.CreatePostResponse(response=Constants.POST_RESPONSE)

    def VoteOnPost(self, request, context):
        post_id = request.post_id
        vote = request.vote
        for post in posts:
            if post.post_id==post_id:
                if vote == r_pb2.POST_UPVOTE:
                    post.score +=1
                else:
                    post.score -=1
        return r_pb2.VotePostResponse(response=Constants.VOTE_POST_RESPONSE)
    
    def GetPost(self, request, context):
        post_id = request.post_id
        post_by_post_id = None
        for post in posts:
            if post.post_id == post_id:
                post_by_post_id = post

        if post_by_post_id:
            return r_pb2.GetPostResponse(post = post_by_post_id)
        
        return r_pb2.GetPostResponse(response = Constants.POST_NOT_FOUND)

    def CreateComment(self, request, context):
        comment = request.comment
        # If a comment is made to another comment, the parent comment has it's replies_present set to True
        if comment.comment_on.content_type == r_pb2.COMMENT:
            comment_content_id = comment.comment_on.comment_id
            for comment in comments:
                if comment.comment_id == comment_content_id:
                    comment.replies_present = True
        comments.append(comment)
        return r_pb2.CreateCommentResponse(response = Constants.COMMENT_RESPONSE)
    

    def VoteOnComment(self, request, context):
        comment_id = request.comment_id
        vote = request.vote
        for comment in comments:
            if comment.comment_id==comment_id:
                if vote == r_pb2.COMMENT_UPVOTE:
                    comment.score +=1
                else:
                    comment.score -=1
        return r_pb2.VoteCommentResponse(response=Constants.VOTE_COMMENT_RESPONSE)
    
    def GetPostTopComments(self, request, context):
        post_id = request.post_id
        n = request.n

        post_comments = {}
        top_n_post_comments = []
        
        for comment in comments:
            if comment.comment_on.content_type == r_pb2.POST:
                if comment.comment_on.post_id == post_id:
                    post_comments[comment.score] = comment

        
        sorted_comments = dict(sorted(post_comments.items()))

        for _, comment in sorted(sorted_comments.items(), key=lambda x: x[0], reverse=True)[:n]:
            top_n_post_comments.append(r_pb2.PostCommentsWithReplies(comment=comment, replies_present=comment.replies_present))

        return r_pb2.GetPostTopCommentsResponse(comments=top_n_post_comments)


    def ExpandCommentBranch(self, request, context):

        def getCommentFromCommentID(comment_id):
            for comment in comments:
                if comment.comment_id == comment_id:
                    return comment
        
        comment_id = request.comment_id
        n = request.n

        all_comments = {}
        top_n_comments = {}
        top_n_comments_replies = []

        for comment in comments:
            if comment.comment_on.content_type == r_pb2.COMMENT:
                if comment.comment_on.comment_id == comment_id:
                    all_comments[comment.score] = comment
        
        sorted_comments = dict(sorted(all_comments.items()))

        for _, comment in sorted(sorted_comments.items(), key=lambda x: x[0], reverse=True)[:n]:
            top_n_comments[comment.comment_id] = []

        for comment_id, _ in top_n_comments.items():
            top_n_replies = {}
            for comment in comments:
                if comment.comment_on.content_type == r_pb2.COMMENT and comment.state == r_pb2.COMMENT_NORMAL:
                    if comment.comment_on.comment_id == comment_id:
                        top_n_replies[comment.score] = comment
            
            sorted_replies = dict(sorted(top_n_replies.items()))
            for _, val in sorted(sorted_replies.items(), key=lambda x: x[0], reverse=True)[:n]:
                top_n_comments[comment_id].append(val)

        for comment_id, top_n_replies in top_n_comments.items():
            top_n_comments_replies.append(
                    r_pb2.CommentsReplies(
                        top_comment = getCommentFromCommentID(comment_id),
                        top_n_replies= top_n_replies
                    )
            )

        return r_pb2.ExpandCommentBranchResponse(top_n_comments_replies=top_n_comments_replies)


    def GetContentScoreUpdates(self, request_iterator, context):
        for request in request_iterator:
            post_id = request.post_id
            comment_id = request.comment_id

            if post_id:
                post = next((p for p in posts if p.post_id == post_id), None)
                if post:
                    while True:
                        time.sleep(1)  
                        yield r_pb2.GetContentScoreUpdatesResponse(score=post.score)
            elif comment_id:
                comment = next((c for c in comments if c.comment_id == comment_id), None)
                if comment:
                    while True:
                        time.sleep(1)  
                        yield r_pb2.GetContentScoreUpdatesResponse(score=comment.score)



def serve(host, port):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    r_grpc.add_RedditServicer_to_server(
        RedditServicer(), server)
    server.add_insecure_port(f"{host}:{port}")
    print(f"Server started listening on {host}:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gRPC Server")
    parser.add_argument("--host", type=str, default="localhost", help="Server host")
    parser.add_argument("--port", type=int, default=50051, help="Server port")
    args = parser.parse_args()
    serve(args.host, args.port)
