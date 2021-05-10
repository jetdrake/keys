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

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import threading

channel = grpc.insecure_channel('localhost:50051')
stub = keys_pb2_grpc.KeyServiceStub(channel)

def onKeyPress(event):
    print(event.char.upper())
    grpc_send(iter([keys_pb2.KeyRequest(key=event.char.upper())]))

def gpu_thread():
    print('gpu thread intialized')
    root = tk.Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha',0.01)
    root.bind('<KeyPress>', onKeyPress)
    root.mainloop()

def grpc_send(key):
    # with grpc.insecure_channel('localhost:50051') as channel:
    #     stub = keys_pb2_grpc.KeyServiceStub(channel)
    response = stub.StreamKeys(key)
    print("Exit Code: " + response.exit_code)

def run():
    threading.Thread(target=gpu_thread()).start()

def getKeys():
    print('get keys')
    for i in range(0, 4):
        yield keys_pb2.KeyRequest(key="B")

if __name__ == '__main__':
    logging.basicConfig()
    run()
