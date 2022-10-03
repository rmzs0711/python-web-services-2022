import grpc
from anime_server import AnimeGuru

from definitions.builds.service_pb2 import AnimeRequest, FactBasis
from definitions.builds.service_pb2_grpc import TestServiceStub


def main() -> None:
    with grpc.insecure_channel("localhost:3000", options=(('grpc.enable_http_proxy', 0),)) as channel:
        while True:
            guru = TestServiceStub(channel)
            com = input("What do you want from me: advice or fact?\n")
            if com == "advice":
                age = int(input("Please tell me your age:\n"))
                req = AnimeRequest()
                req.age = age
                advice = guru.get_advice(req)
                print("My anime advice is: " + advice.advice_data)
            elif com == "fact":
                anime_name = input("What is the name of the anime you want to know a fact about\n")
                fact_basis = FactBasis(anime_name=anime_name)
                fact = guru.tell_me_a_fact(fact_basis)
                print(fact.fact_data)
            else:
                print("I don't understand you, choom, please try again")


if __name__ == "__main__":
    main()