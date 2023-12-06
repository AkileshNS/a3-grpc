# import grpc
from __future__ import print_function
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import reddit_pb2 as r_pb2 
import reddit_pb2_grpc as r_grpc
import grpc

class CodeAssistantClient:
    """Client for accessing CodeAssistant API."""
    def __init__(self, server_addr):
        channel = grpc.insecure_channel(server_addr)
        self.stub = r_pb2.CodeAssistantStub(channel)

    def generate_pr_description(self, files):
        request = r_pb2.PRDescriptionRequest(files=files)
        return self.stub.GeneratePRDescription(request)

    def smart_autocomplete(self, files, repo_content):
        request = r_pb2.SmartAutoCompleteRequest(
            files=files, repository_content=repo_content)  
        return self.stub.SmartAutocomplete(request)

    def chat_gpt_for_code(self, files, issue_desc):
        request = r_pb2.ChatGPTForCodeRequest(
            files=files, issue_description=issue_desc)
        return self.stub.ChatGPTForCode(request) 

    def virtual_pair_programming(self, request_iterator):
        response_iterator = self.stub.VirtualPairProgramming(request_iterator)
        return response_iterator
