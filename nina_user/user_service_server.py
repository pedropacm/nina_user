# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import time
import math
import logging

from repo.user_repo import UserRepo, User

import grpc

import rpc.user_service_pb2 as user_service_pb2
import rpc.user_service_pb2_grpc as user_service_pb2_grpc

import rpc.repo_service_pb2 as repo_service_pb2
import rpc.repo_service_pb2_grpc as repo_service_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def build_id_request(user_id):
    return repo_service_pb2.User_Id(user_id=user_id)

def validate_user(user):
    if (len(user.name) == 0 and len(user.email) == 0 and len(user.password) == 0):
        user = None
    return user

def build_user_from_response(response_user):
    user = User()
    user.id = response_user.id
    user.name = response_user.name
    user.email = response_user.email
    user.password = response_user.password
    return validate_user(user)

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):

    def __init__(self):
        pass

    def GetName(self, request, context):
        channel = grpc.insecure_channel('localhost:50052')
        stub = repo_service_pb2_grpc.RepoServiceStub(channel)
        user = build_user_from_response(stub.FindById(build_id_request(request.id)))
        if user is None:
            return user_service_pb2.UserName(name="not_found")
        else:
            return user_service_pb2.UserName(name=user.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()