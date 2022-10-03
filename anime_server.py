from concurrent.futures import ThreadPoolExecutor
from pickletools import uint8

import grpc

import definitions.builds.service_pb2
from definitions.builds.service_pb2 import Fact, FactBasis, AnimeRequest, AnimeAdvice
from definitions.builds.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server

class AnimeGuru(TestServiceServicer):
    def tell_me_a_fact(self, fact_basis : FactBasis, context) -> Fact:
        """tell a fact about anime title

        Args:
            fact_basis (FactBasis): contains only title's name by now
            context (Any): lame request context

        Returns:
            Fact: absolutely real fact
        """
        fact = Fact()
        anime_name : str = fact_basis.anime_name 
        fact.fact_data = anime_name.upper() + " IS THE BEST ANIME IN THE WORLD!!!"
        return fact

    def get_advice(self, request : AnimeRequest, context) -> AnimeAdvice:
        """get advice to decide what anime to watch

        Args:
            request (AnimeRequest): contains anime fan's age
            context (Any): lame request context

        Returns:
            AnimeAdvice: good advice from anime guru
        """
        age : int = request.age
        advice_data = ""
        if age < 6:
            advice_data = "Boku no Piko"
        elif 6 <= age < 12:
            advice_data = "JoJo's Bizarre Adventure"
        elif 12 <= age < 18:
            advice_data = "Blend S"
        elif 18 <= age < 24:
            advice_data = "duuude, you'd better study instead of searching waifus"
        elif 24 <= age < 30:
            advice_data = "maaaaan, you'd better work instead of searching waifus"
        else:
            advice_data = "Hello kitty"
        
        advice = AnimeAdvice(advice_data=advice_data)
        return advice

def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(AnimeGuru(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The anime guru is up and ready for your wishes...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()