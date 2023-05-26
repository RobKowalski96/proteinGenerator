import random
from typing import List, Tuple, Dict


def generate_proteins_with_connections(protein_length: int,
                                       amino_acid_freq: Dict[str, float],
                                       connections: List[Tuple[int, int]],
                                       negative_amino_acids: List[str],
                                       positive_amino_acids: List[str],
                                       number_of_proteins: int) -> List[str]:
    proteins = []
    for i in range(number_of_proteins):
        proteins.append(
            generate_protein_with_connections(protein_length, amino_acid_freq, connections, negative_amino_acids,
                                              positive_amino_acids))
    return proteins


def generate_proteins_without_connections(protein_length: int,
                                          amino_acid_freq: Dict[str, float],
                                          connections: List[Tuple[int, int]],
                                          negative_amino_acids: List[str],
                                          positive_amino_acids: List[str],
                                          neutral_amino_acids: List[str],
                                          number_of_proteins: int) -> List[str]:
    proteins = []
    for i in range(number_of_proteins):
        proteins.append(
            generate_protein_without_connections(protein_length, amino_acid_freq, connections, negative_amino_acids,
                                                 positive_amino_acids, neutral_amino_acids))
    return proteins


def generate_protein_with_connections(protein_length: int,
                                      amino_acid_freq: Dict[str, float],
                                      connections: List[Tuple[int, int]],
                                      negative_amino_acids: List[str],
                                      positive_amino_acids: List[str]) -> str:

    base_protein = generate_protein_base(protein_length, amino_acid_freq)
    result_protein = add_electrical_connections(base_protein, connections, negative_amino_acids, positive_amino_acids)
    return result_protein


def generate_protein_without_connections(protein_length: int,
                                         amino_acid_freq: Dict[str, float],
                                         connections: List[Tuple[int, int]],
                                         negative_amino_acids: List[str],
                                         positive_amino_acids: List[str],
                                         neutral_amino_acids: List[str]) -> str:

    base_protein = generate_protein_base(protein_length, amino_acid_freq)
    result_protein = add_nonelectrical_connections(base_protein, connections, negative_amino_acids, positive_amino_acids,
                                                   neutral_amino_acids)
    return result_protein


def generate_protein_base(protein_length: int,
                          amino_acid_freq: Dict[str, float]) -> str:
    protein = []
    amino_acids = list(amino_acid_freq.keys())
    freqs = list(amino_acid_freq.values())
    for i in range(protein_length):
        aa = random.choices(amino_acids, weights=freqs, k=1)
        protein.append(aa[0])
    return ''.join(protein)


def add_electrical_connections(base_protein: str,
                               connections: List[Tuple[int, int]],
                               negative_amino_acids: List[str],
                               positive_amino_acids: List[str]) -> str:
    base_protein = list(base_protein)
    for c in connections:
        i, j = c
        replace_negative = random.choice([True, False])
        options = negative_amino_acids if replace_negative else positive_amino_acids
        base_protein[i] = random.choice(options)
        opposite_options = positive_amino_acids if replace_negative else negative_amino_acids
        base_protein[j] = random.choice(opposite_options)
    return ''.join(base_protein)


def add_nonelectrical_connections(protein: str,
                                  connections: List[Tuple[int, int]],
                                  negative_amino_acids: List[str],
                                  positive_amino_acids: List[str],
                                  neutral_amino_acids: List[str]) -> str:
    protein = list(protein)
    for c in connections:
        i, j = c
        options = random.choice([negative_amino_acids, positive_amino_acids, neutral_amino_acids])
        protein[i] = random.choice(options)
        protein[j] = random.choice(options)
    return ''.join(protein)
