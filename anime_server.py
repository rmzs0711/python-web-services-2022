"""server
"""

from concurrent.futures import ThreadPoolExecutor
import grpc
import guru_logic as gl
from definitions.builds.service_pb2 import Fact, FactBasis, AnimeRequest, AnimeAdvice
from definitions.builds.service_pb2_grpc import TestServiceServicer
from definitions.builds.service_pb2_grpc import add_TestServiceServicer_to_server

class AnimeGuru(TestServiceServicer):
    """guru that can give you facts and advices
    """
    def tell_me_a_fact(self, request : FactBasis, context) -> Fact:
        """give response with 100% true fact about anime

        Args:
            fact_basis (FactBasis): contains only title's name by now
            context (Any): lame request context

        Returns:
            Fact: absolutely real fact
        """
        fact = Fact()
        anime_name : str = request.anime_name
        fact.fact_data = gl.create_a_fact(anime_name)
        return fact

    def get_advice(self, request : AnimeRequest, context) -> AnimeAdvice:
        """give response with advice in order to decide what anime you need to watch

        Args:
            request (AnimeRequest): contains anime fan's age
            context (Any): lame request context

        Returns:
            AnimeAdvice: good advice from the anime guru
        """
        age : int = request.age
        advice = AnimeAdvice(advice_data=gl.create_advice(age))
        return advice

def execute_server():
    """run server
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(AnimeGuru(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The anime guru is up and ready for your wishes...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
