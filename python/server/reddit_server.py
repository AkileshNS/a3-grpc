from concurrent import futures
import grpc
import sys
import argparse
from grpc_interceptor import ServerInterceptor
import reddit_pb2 as r_pb2
import reddit_pb2_grpc as r_grpc
import utils.constants as Constants
import time
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

posts = []
comments = []

class AuthInterceptor(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        return request

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
        post_comments = []
        n_top_post_comments = []

        for comment in comments:
            if comment.comment_on.content_type == r_pb2.POST:
                if comment.comment_on.content_type.post_id == post_id:
                    post_comments.append([comment.score, r_pb2.PostCommentsWithReplies(comment=comment, replies_present=comment.replies_present)])

        post_comments.sort(key=lambda x: 0)
        post_comments = post_comments[-n:]
        for _, value in post_comments:
            n_top_post_comments.append(value)
        
        return r_pb2.GetPostTopCommentsResponse(PostCommentsWithReplies=n_top_post_comments)


    def ExpandCommentBranch(self, request, context):
        comment_id = request.comment_id
        n = request.n

        def get_comments_recursive(comment_id, depth):
            result = []
            for comment in comments:
                if comment.comment_on.content_type == r_pb2.COMMENT and comment.comment_on.comment_id == comment_id:
                    result.append(comment)

            result.sort(key=lambda x: x.score, reverse=True)
            result = result[:n]

            if depth > 0:
                for sub_comment in result:
                    sub_comment_id = sub_comment.comment_id
                    sub_comments = get_comments_recursive(sub_comment_id, depth - 1)
                    sub_comments.sort(key=lambda x: x.score, reverse=True)
                    sub_comments = sub_comments[:n]
                    sub_comment.replies_present = bool(sub_comments)
                    result.extend(sub_comments)

            return result

        comment_branch = get_comments_recursive(comment_id, depth=1)

        expanded_comments = [comment for comment in comment_branch if not comment.comment_on.content_type == r_pb2.COMMENT]
        expanded_reply_comments = [comment for comment in comment_branch if comment.comment_on.content_type == r_pb2.COMMENT]

        return r_pb2.GetCommentTopCommentsResponse(top_n_comments=expanded_comments,
                                                    top_n_reply_comments=expanded_reply_comments)


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
    interceptors = [AuthInterceptor()]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=interceptors)
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
