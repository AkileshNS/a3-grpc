import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2
import reddit_pb2_grpc as r_grpc
import utils.constants as Constants
import client.reddit_client as reddit_client

class TestRedditClient:
    def test_generate_pr_description_positive(self):
        self.client = reddit_client.RedditClient(Constants.HOST, Constants.PORT)
        comment_id = "C1"
        n = 1
        response = self.client.get_expand_comment_branch(comment_id, n)
        print(response)


