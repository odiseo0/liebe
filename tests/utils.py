import random

from src.utils.generics import NUCLEOTIDES


def generate_random_dna_str(length: int = 8) -> str:
    return ''.join([random.choice(NUCLEOTIDES) for _ in range(length)])
