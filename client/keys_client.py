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

import queue
send_queue = queue.SimpleQueue()  # or Queue if using Python before 3.7

def onKeyPress(event):
    print(event.char)
    send_queue.push(keys_pb2.KeyRequest(key=""+event.char))

def gpu_thread():
    root = tk.Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha',0.2)
    root.bind('<KeyPress>', onKeyPress)
    root.mainloop()

def grpc_thread():
    with grpc.insecure_channel('4.tcp.ngrok.io:10274') as channel:
        stub = keys_pb2_grpc.KeyServiceStub(channel)
        response = stub.StreamKeys(iter(send_queue.get, None))
    print("Exit Code: " + response.exit_code)

def run():
    threading.Thread(target=grpc_thread()).start()
    threading.Thread(target=gpu_thread()).start()

def getKeys():
    print('get keys')
    for i in range(0, 4):
        yield keys_pb2.KeyRequest(key="B")

if __name__ == '__main__':
    logging.basicConfig()
    run()
