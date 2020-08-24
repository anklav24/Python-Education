def dna_to_rna(dna: str) -> str:
    """Translates a given DNA string into RNA"""
    return dna.replace('T', 'U')


print(dna_to_rna("GCAT"))
