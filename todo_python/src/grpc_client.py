from __future__ import print_function

import logging
import random

import grpc

import todo_pb2
import todo_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response = stub.GetTodos(todo_pb2.Empty())
        print(response)


if __name__ == "__main__":
    logging.basicConfig()
    run()
