import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2
import reddit_pb2_grpc as r_grpc
import utils.constants as Constants
import client.reddit_client as reddit_client



