import random

from src.utils import generics, structures


ran_dna_str = ''.join([random.choice(structures.NUCLEOTIDES) for _ in range(20)])

DNA_STR = generics.is_valid_sequence(ran_dna_str)

print(DNA_STR)
print(f"Frequencia de Nucleótidos: {generics.count_frequency(DNA_STR)}\n")
print(f"Transcipción de ADN: {generics.transcript(DNA_STR)}\n")
print(f"5' {DNA_STR} 3'")
print(f"  {''.join(['|' for _ in range(len(DNA_STR))])}")
print(f"3' {generics.reverse_seq(DNA_STR)[::-1]} 5' (Complemento)")
print(f"5' {generics.reverse_seq(DNA_STR)} 3' (Complemento Rev.)")
