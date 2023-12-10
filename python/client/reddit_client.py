from __future__ import print_function
import sys
import reddit_pb2 as r_pb2 
import reddit_pb2_grpc as r_grpc
import grpc
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class RedditClient:
    """Client for accessing Reddit API."""
    def __init__(self, host, port):
        server_addr = f"{host}:{port}"
        channel = grpc.insecure_channel(server_addr)
        self.stub = r_grpc.RedditStub(channel)

    def create_post(self, post):
        request = r_pb2.CreatePostRequest(post=post)
        return self.stub.CreatePost(request)

    def vote_on_post(self, post_id, vote):
        request = r_pb2.VoteCommentRequest(
            post_id=post_id, vote=vote)
        return self.stub.VoteOnPost(request)

    def get_post(self, post_id):
        request = r_pb2.GetPostRequest(post_id=post_id)
        return self.stub.GetPost(request)

    def create_comment(self, comment):
        request = r_pb2.CreateCommentRequest(comment=comment)
        return self.stub.CreateComment(request)

    def vote_on_comment(self, comment_id, vote):
        request = r_pb2.VoteCommentRequest(
            comment_id=comment_id,
            vote=vote
        )
        return self.stub.VoteOnComment(request)

    def get_post_top_comments(self, post_id, n):
        request = r_pb2.GetPostTopCommentsRequest(
            post_id=post_id,
            n=n
        )
        return self.stub.GetPostTopComments(request)

    def get_expand_comment_branch(self, comment_id, n):
        request = r_pb2.ExpandCommentBranchRequest(
            comment_id=comment_id, 
            n=n
        )
        return self.stub.ExpandCommentBranch(request)

    def get_content_score_updates(self, request_iterator):
        response_iterator = self.stub.GetContentScoreUpdates(request_iterator)
        return response_iterator
    
