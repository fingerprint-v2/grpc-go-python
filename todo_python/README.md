# Compile

`python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/todo.proto`

# Running

pymon grpc_server.py --all
