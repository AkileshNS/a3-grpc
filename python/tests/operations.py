import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import utils.constants as Constants

def perform_multiple_operations(Client, post_id):
    post = Client.get_post(post_id)
    most_upvoted_comment = Client.get_post_top_comments(post_id, 1)

    if most_upvoted_comment == None:
        return None
    comment_id = most_upvoted_comment.comments[0].comment.comment_id

    most_upvoted_comment_and_reply = Client.get_expanded_comment_branch(comment_id, 1)

    return most_upvoted_comment_and_reply

