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

from threading import *
import time

# NOTE: need to map keycodes.csv to tkinter keycodes
address = "localhost:50051"
with open('address.txt', 'r') as file:
    address = file.read()

channel = grpc.insecure_channel(address)
stub = keys_pb2_grpc.KeyServiceStub(channel)
pressed = []
queue = []

def on_key_press(event):

    if (event.keycode in pressed):
        return

    print(event)
    if (event.keycode == 32):
        k = "SPACE"
    elif (event.keycode == 17):
        k = "LCONTROL"
    elif (event.keycode == 50):
        k = "LSHIFT"
    elif (event.keycode == 36):
        k = "RETURN"
    elif (event.keycode == 8):
        k = "BACK"
    elif (event.keycode == 9):
        k = "ESCAPE"
    else:
        k = event.char.upper()
    print(k)
    pressed.append(event.keycode)
    queue.append(k)
    #stub.PressKey(keys_pb2.KeyRequest(key=k))
    #grpc_send(iter([keys_pb2.KeyRequest(key=k)]))

def on_key_release(event):
    print(event)
    if (event.keycode == 32):
        k = "SPACE"
    elif (event.keycode == 17):
        k = "LCONTROL"
    elif (event.keycode == 50):
        k = "LSHIFT"
    elif (event.keycode == 36):
        k = "RETURN"
    elif (event.keycode == 8):
        k = "BACK"
    else:
        k = event.char.upper()
    print(k)
    #stub.ReleaseKey(keys_pb2.KeyRequest(key=k))
    pressed.remove(event.keycode)


def gpu_thread():
    print('gpu thread intialized')
    root = tk.Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha',0.1)
    root.bind('<KeyPress>', on_key_press)
    root.bind('<KeyRelease>', on_key_release)

    t1=Thread(target=grpc_stream)
    t1.start()

    root.mainloop()

def grpc_send(key):
    response = stub.StreamKeys(key)
    print("Exit Code: " + response.exit_code)

def stream_get_keys():
    while True:
        if len(queue) > 0:
            k = queue.pop()
            if k == "ESCAPE":
                return
            yield keys_pb2.KeyRequest(key=k)
        

def grpc_stream():
    stub.StreamKeys(iter(stream_get_keys()))
    print('other thread')
    #stream_get_keys()


def run():
    gpu_thread()

if __name__ == '__main__':
    logging.basicConfig()
    run()
