import grpc
import hello_pb2
import hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:12346') as channel:
        # stub = hello_pb2_grpc.GreeterStub(channel)
        # response = stub.SayHello(hello_pb2.HelloRequest(name='Adrian'))
        stub1 = hello_pb2_grpc.GreeterStub(channel)
        response1 = stub1.CalculateArea(hello_pb2.GiveSide(side1=4, side2=4))
        print(f'The area is: {response1.area}')


if __name__ == "__main__":
    run()