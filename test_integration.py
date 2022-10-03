"""tests
"""

from anime_server import AnimeGuru
from definitions.builds.service_pb2 import Fact, FactBasis, AnimeRequest, AnimeAdvice


def test_advice_and_fact_integration():
    """test advice logic integration
    """
    guru = AnimeGuru()
    advice = guru.get_advice(AnimeRequest(age=0), None)
    assert advice.advice_data == "Boku no Piko"
    fact = guru.tell_me_a_fact(FactBasis(anime_name=""), None)
    assert fact.fact_data == " IS THE BEST ANIME IN THE WORLD!!!"
