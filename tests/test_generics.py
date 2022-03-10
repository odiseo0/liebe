from src.utils.generics import is_valid_sequence
from .utils import generate_random_dna_str

def test_is_valid_sequence():
    dna_str = generate_random_dna_str(20)

    assert dna_str == is_valid_sequence(dna_str)
    assert "ATTCGCG" == is_valid_sequence("attcgCg")
    assert False == is_valid_sequence("ATTXcG")

