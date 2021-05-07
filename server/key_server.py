from concurrent import futures
import logging

import grpc
import keys_pb2
import keys_pb2_grpc
import keycodes
import send

class KeyServicer(keys_pb2_grpc.KeyService):

    def StreamKeys(self, request_iterator, context):
        
        for request in request_iterator:
            print(request.key)
            send.KeyPress(int(keycodes.keycodes().keydict.get(request.key), 16))
        return keys_pb2.KeyResponse(exit_code="success")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keys_pb2_grpc.add_KeyServiceServicer_to_server(KeyServicer(), server)
    server.add_insecure_port('[::]:50051')
    print('starting server')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
