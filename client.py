"""client
"""

import re
import grpc
from definitions.builds.service_pb2 import AnimeRequest, FactBasis
from definitions.builds.service_pb2_grpc import TestServiceStub


def main() -> None:
    """main code
    """
    with grpc.insecure_channel("localhost:3000", options=(('grpc.enable_http_proxy', 0),)) as chan:
        advice_pattern = re.compile("\s*advice\s*")
        fact_pattern = re.compile("\s*fact\s*")
        while True:
            guru = TestServiceStub(chan)
            com = input("What do you want from me: advice or fact?\n")
            if advice_pattern.match(com):
                age = 0
                age = input("Please tell me your age:\n")
                while not age.isdigit():
                    age = input(
                        "Are you dumb? I asked your age, not your mom's credit card password, " +
                        "so just tell me your age:\n")
                age = int(age)
                req = AnimeRequest()
                req.age = age

                advice = guru.get_advice(req)
                print("My anime advice is: " + advice.advice_data)
            elif fact_pattern.match(com):
                anime_name = input("What is the name of the anime you want to know a fact about\n")
                fact_basis = FactBasis(anime_name=anime_name)
                fact = guru.tell_me_a_fact(fact_basis)
                print(fact.fact_data)
            else:
                print("I don't understand you, choom, please try again")


if __name__ == "__main__":
    main()
