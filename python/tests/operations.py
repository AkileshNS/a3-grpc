import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2
import reddit_pb2_grpc as r_grpc
import utils.constants as Constants
import client.reddit_client as reddit_client

def perform_multiple_operations(Client):
    post_id = Constants.POST_ID
    n = 2
    post = Client.get_post(post_id)
    most_upvoted_comment = Client.get_post_top_comments(post_id, 1)
    comment_id = most_upvoted_comment.comments[0].comment.comment_id
    most_upvoted_comment_and_reply = Client.get_expanded_comment_branch(comment_id, 1)

    return most_upvoted_comment_and_reply

client = reddit_client.RedditClient(Constants.HOST, Constants.PORT)
perform_multiple_operations(client)