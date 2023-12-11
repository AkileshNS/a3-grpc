# Assignment 3 GRPC

The server file is located at python/server/reddit_server.py \
The server file is located at python/client/reddit_client.py \
The test file is located at python/test/test_reddit.py \
The high level function is located at python/test/operations.py \
The stubs generated are located at the python/ folder.

## Commands
All these commands are intended to be run from inside the python/ directory.

To do this simply use the cd python command

Generate Stubs: \
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/reddit.proto

Run Test Cases: \
pytest

Start Server: \
python server/reddit_server.py

Optional parameters: \
--host: specify server host
--port: specify server port


Example: \
python server/reddit_server.py --host localhost --port 50051

