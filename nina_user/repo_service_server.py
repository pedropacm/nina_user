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

import rpc.repo_service_pb2 as repo_service_pb2
import rpc.repo_service_pb2_grpc as repo_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def build_user(request):
    user = User()
    user.id = request.id
    user.name = request.name
    user.email = request.email
    user.password = request.password
    return user

def build_user_response(user):
    return repo_service_pb2.User(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password)

class RepoServiceServicer(repo_service_pb2_grpc.RepoServiceServicer):

    user_repo = UserRepo()
    
    def __init__(self):
        pass

    def Save(self, request, context):
        user = build_user(request)
        if user.id is 0:
            user.id = None
        user = RepoServiceServicer.user_repo.save(user)
        return build_user_response(user)
        
    def FindById(self, request, context):
        user = RepoServiceServicer.user_repo.find_by_id(request.user_id)
        if user is None:
            user = User()
        return build_user_response(user)

    def FindByEmail(self, request, context):
        user = RepoServiceServicer.user_repo.find_by_email(request.user_email)
        if user is None:
            user = User()
        return build_user_response(user)

    def ResetDatabase(self, request, context):
        RepoServiceServicer.user_repo.reset_database()
        return repo_service_pb2.Empty()

def create_server(address, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    repo_service_pb2_grpc.add_RepoServiceServicer_to_server(
        RepoServiceServicer(), server)
    server.add_insecure_port(address)
    return server

def serve():
    server = create_server('[::]:50052', 1)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()