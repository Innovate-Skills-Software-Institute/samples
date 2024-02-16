import grpc
import bidirectional_pb2_grpc
import bidirectional_pb2


class BidirectionalClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.stub = bidirectional_pb2_grpc.BidirectionalStub(self.channel)

    def getServerMessage(self):
        return self.stub.getServerMessage(self.generate_message())

    def generate_message(self):
        for i in range(5):
            yield bidirectional_pb2.RequestPayload(message=f"message no {i}")

    def clientStreamMessage(self):
        return self.stub.clientStreamingMessage(self.generate_message())

    def serverStreamMessage(self):
        request_payload = bidirectional_pb2.RequestPayload(message=f"Server Stream message")
        return self.stub.serverStreamingMessage(request_payload)


if __name__ == "__main__":
    client = BidirectionalClient()
    responses = client.getServerMessage()
    for response in responses:
        print(response.message)

    client_streaming_response = client.clientStreamMessage()
    print(client_streaming_response.message)

    server_streaming_response = client.serverStreamMessage()
    for response in server_streaming_response:
        print(response.message)
