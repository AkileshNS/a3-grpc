import sys
from pathlib import Path
import unittest
from unittest.mock import MagicMock

# Resolving the path to the current script and adding its parent directory to the Python path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import utils.constants as Constants
import client.reddit_client as reddit_client
import tests.operations as operations

class TestPerformOperations(unittest.TestCase):

    def test_perform_multiple_operations_happy_path(self):
        """
        Test the happy path of perform_multiple_operations function.

        - Mocks a RedditClient instance.
        - Sets up expected results for get_post, get_post_top_comments, and get_expanded_comment_branch.
        - Calls perform_multiple_operations with the mock client and a post ID.
        - Verifies that the function returns the expected result and makes the correct calls to the client's methods.
        """
        mock_client = MagicMock(spec=reddit_client.RedditClient)
        post_id = Constants.POST_ID_1

        expected_post = Constants.post1
        expected_top_comment = Constants.comments_1
        expected_expanded_comment_branch = Constants.comment_reply_1

        mock_client.get_post.return_value = expected_post
        mock_client.get_post_top_comments.return_value = expected_top_comment
        mock_client.get_expanded_comment_branch.return_value = expected_expanded_comment_branch

        result = operations.perform_multiple_operations(mock_client, post_id)

        self.assertEqual(result, expected_expanded_comment_branch)

        mock_client.get_post.assert_called_once_with(Constants.POST_ID_1)
        mock_client.get_post_top_comments.assert_called_once_with(Constants.POST_ID_1, 1)
        mock_client.get_expanded_comment_branch.assert_called_once_with(expected_top_comment.comments[0].comment.comment_id, 1)

    def test_perform_multiple_operations_api_failure(self):
        """
        Test perform_multiple_operations when an API failure occurs.

        - Mocks a RedditClient instance.
        - Sets up an exception to be raised when get_post is called.
        - Calls perform_multiple_operations with the mock client and a post ID.
        - Verifies that the function raises an exception.
        """
        mock_client = MagicMock(spec=reddit_client.RedditClient)
        post_id = Constants.POST_ID_1

        mock_client.get_post.side_effect = Exception("API Error")

        with self.assertRaises(Exception):
            operations.perform_multiple_operations(mock_client, post_id)

    def test_perform_multiple_operations_no_top_comment(self):
        """
        Test perform_multiple_operations when there is no top comment.

        - Mocks a RedditClient instance.
        - Sets up expected results for get_post and get_post_top_comments.
        - Calls perform_multiple_operations with the mock client and a post ID.
        - Verifies that the function returns None.
        """
        mock_client = MagicMock(spec=reddit_client.RedditClient)
        post_id = Constants.POST_ID_2

        expected_post = Constants.post2
        expected_top_comment = None
        expected_expanded_comment_branch = None

        # Simulate get_post returning a post with no top comment
        mock_client.get_post.return_value = expected_post
        mock_client.get_post_top_comments.return_value = expected_top_comment
        mock_client.get_expanded_comment_branch.return_value = expected_expanded_comment_branch

        result = operations.perform_multiple_operations(mock_client, post_id)

        self.assertIsNone(result)


    def test_perform_multiple_operations_no_comment_reply(self):
        """
        Test perform_multiple_operations when there is no comment reply.

        - Mocks a RedditClient instance.
        - Sets up expected results for get_post, get_post_top_comments, and get_expanded_comment_branch.
        - Calls perform_multiple_operations with the mock client and a post ID.
        - Verifies that the function returns None.
        """
        mock_client = MagicMock(spec=reddit_client.RedditClient)
        post_id = Constants.POST_ID_3

        expected_post = Constants.post3
        expected_top_comment = Constants.comments_3
        expected_expanded_comment_branch = None

        mock_client.get_post.return_value = expected_post
        mock_client.get_post_top_comments.return_value = expected_top_comment
        mock_client.get_expanded_comment_branch.return_value = expected_expanded_comment_branch

        result = operations.perform_multiple_operations(mock_client, post_id)

        self.assertEqual(result, expected_expanded_comment_branch)
