from typing import Union
from collections import Counter

from .structures import NUCLEOTIDES, DNA_CODONS

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
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content(seq: str) -> str:
    """Get GC Content in sequence."""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subset(seq: str, k: int = 20):
    """Get GC Content from a sub sequence."""
    result = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i+k]
        result.append(gc_content(subseq))

    return result

def translate_seq(seq: str, pos: int = 0):
    """Return an aminoacid sequence."""
    return [DNA_CODONS[seq[p:p + 3]] for p in range(pos, len(seq) - 2, 3)]

def codon_usage(seq: str, aminoacid: str):
    tmp = [seq[i:i + 3] for i in range(0, len(seq) - 2, 3) if DNA_CODONS[seq[i:i + 3] == aminoacid]]

    freq = dict(Counter(tmp))
    weight = sum(freq.values())
    
    return {k:round(freq[s] / weight, 2) for k, s in freq}
