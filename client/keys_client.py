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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import keys_pb2
import keys_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('4.tcp.ngrok.io:10274') as channel:
        stub = keys_pb2_grpc.KeyServiceStub(channel)
        response = stub.StreamKeys(getKeys())
    print("Exit Code: " + response.exit_code)

def getKeys():
    for i in range(0, 4):
        yield keys_pb2.KeyRequest(key="A")

if __name__ == '__main__':
    logging.basicConfig()
    run()
