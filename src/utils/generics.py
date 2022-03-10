from typing import Union
from collections import Counter

from .structures import NUCLEOTIDES, DNA_REVERSE_COMPLEMENT

# TODO: Replace Union by new Python 3.10 syntax: str | bool
def is_valid_sequence(seq: str) -> Union[str, bool]:
    """Check DNA Sequence to make sure it is a correct."""
    seq = seq.upper()

    for n in seq:
        if n not in NUCLEOTIDES:
            return False

    return seq

def count_frequency(seq: str) -> dict[str, int]:
    """Count nucleotides frequency."""
    return dict(Counter(seq))

def transcript(seq: str) -> str:
    """Replace Thymine with Uracil. T -> U"""
    return seq.replace("T", "U")

def reverse_seq(seq: str) -> str:
    """Swap adenine with thymine, guanine with cytosine and reverse DNA sequence."""
    return ''.join([DNA_REVERSE_COMPLEMENT[n] for n in seq])[::-1]
