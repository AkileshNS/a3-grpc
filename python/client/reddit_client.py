from __future__ import print_function
import sys
import grpc
from pathlib import Path

# Resolving the path to the current script and adding its parent directory to the Python path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2 
import reddit_pb2_grpc as r_grpc

class RedditClient:
    """Client for accessing Reddit API."""

    def __init__(self, host, port):
        """
        Initialize the RedditClient.

        Parameters:
        - host (str): The host address.
        - port (int): The port number.
        """
        server_addr = f"{host}:{port}"
        channel = grpc.insecure_channel(server_addr)
        self.stub = r_grpc.RedditStub(channel)

    def create_post(self, post):
        """
        Create a new post.

        Parameters:
        - post: The post object.

        Returns:
        - The response from the server.
        """
        request = r_pb2.CreatePostRequest(post=post)
        return self.stub.CreatePost(request)

    def vote_on_post(self, post_id, vote):
        """
        Vote on a specific post.

        Parameters:
        - post_id (str): The ID of the post.
        - vote (int): The vote value.

        Returns:
        - The response from the server.
        """
        request = r_pb2.VoteCommentRequest(
            post_id=post_id, vote=vote)
        return self.stub.VoteOnPost(request)

    def get_post(self, post_id):
        """
        Get information about a specific post.

        Parameters:
        - post_id (str): The ID of the post.

        Returns:
        - The response from the server.
        """
        request = r_pb2.GetPostRequest(post_id=post_id)
        return self.stub.GetPost(request)

    def create_comment(self, comment):
        """
        Create a new comment.

        Parameters:
        - comment: The comment object.

        Returns:
        - The response from the server.
        """    
        request = r_pb2.CreateCommentRequest(comment=comment)
        return self.stub.CreateComment(request)

    def vote_on_comment(self, comment_id, vote):
        """
        Vote on a specific comment.

        Parameters:
        - comment_id (str): The ID of the comment.
        - vote (int): The vote value.

        Returns:
        - The response from the server.
        """
        request = r_pb2.VoteCommentRequest(
            comment_id=comment_id,
            vote=vote
        )
        return self.stub.VoteOnComment(request)

    def get_post_top_comments(self, post_id, n):
        """
        Get the top comments of a specific post.

        Parameters:
        - post_id (str): The ID of the post.
        - n (int): The number of top comments to retrieve.

        Returns:
        - The response from the server.
        """    
        request = r_pb2.GetPostTopCommentsRequest(
            post_id=post_id,
            n=n
        )
        return self.stub.GetPostTopComments(request)

    def get_expanded_comment_branch(self, comment_id, n):
        """
        Expand the comment branch for a specific comment.

        Parameters:
        - comment_id (str): The ID of the comment.
        - n (int): The depth of the comment branch to expand.

        Returns:
        - The response from the server.
        """ 
        request = r_pb2.ExpandCommentBranchRequest(
            comment_id=comment_id, 
            n=n
        )
        return self.stub.ExpandCommentBranch(request)

    def get_content_score_updates(self, request_iterator):
        """
        Get updates on content scores.

        Parameters:
        - request_iterator: An iterator for requests.

        Returns:
        - The response iterator from the server.
        """
        response_iterator = self.stub.GetContentScoreUpdates(request_iterator)
        return response_iterator
    
