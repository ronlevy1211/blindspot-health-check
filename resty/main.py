from flask import Flask, request
import healthy_pb2_grpc
import healthy_pb2
import json
from grpc import insecure_channel


app = Flask(__name__)

# Create a gRPC channel to the server
channel = insecure_channel('localhost:50051')

# Create a stub (client) for the gRPC service
stub = healthy_pb2_grpc.HealthCheckServiceStub(channel)


@app.route('/check_security', methods=['POST'])
def check_security():
    # Get the packages from the request
    packages = request.get_json()['packages']
    # Create a request message
    request1 = healthy_pb2.SecurityRequest(packages=packages)
    # Send the request to the gRPC server and get the response
    response = stub.CheckSecurity(request1)
    return json.loads(str(response.security_check_result))


if __name__ == '__main__':
    app.run(debug=True)

