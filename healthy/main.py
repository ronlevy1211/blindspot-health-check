import grpc
from concurrent import futures
from models.HealthCheck import HealthCheck
import healthy_pb2_grpc
import healthy_pb2


class HealthCheckService(healthy_pb2_grpc.HealthCheckServiceServicer):
    def CheckSecurity(self, request, context):
        response = healthy_pb2.SecurityResponse()
        packages = request.packages
        with futures.ThreadPoolExecutor(4) as executor:
            future_security_checks = [executor.submit(HealthCheck.HealthCheck(package).security_check) for package in packages]
            for future in futures.as_completed(future_security_checks):
                response.security_check_result.append(future.result())
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    healthy_pb2_grpc.add_HealthCheckServiceServicer_to_server(HealthCheckService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
