import grpc
import hello_pb2
import hello_pb2_grpc
from concurrent import futures


class Greater(hello_pb2_grpc.GreeterServicer):

    # def SayHello(self, request, context):
    #     print(request)
    #     return hello_pb2.HelloReply(response=f"yes {request.name}")
    def CalculateArea(self, request, context):
        print(request)
        return hello_pb2.AreaReply(area=request.side1 * request.side2)


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greater(), server)
    server.add_insecure_port('[::]:12346')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serv()
