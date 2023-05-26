from typing import List, Tuple

from variables import AMINOACIDS_FREQUENCY
from variables import CONNECTIONS
from variables import NEGATIVE_AMINOACIDS
from variables import NEUTRAL_AMINOACIDS
from variables import POSITIVE_AMINOACIDS
from variables import PROTEIN_LENGTH
from variables import LEARNING_SAMPLE_SIZE
from variables import POSITIVE_SAMPLE_SIZE
from variables import NEGATIVE_SAMPLE_SIZE


def validate_configuration(parameters) -> bool:
    if not validate_parameters_type(parameters):
        return False
    if not validate_connections(parameters[CONNECTIONS], parameters[PROTEIN_LENGTH]):
        print("Incorrect connection data")
        return False
    return True


def validate_parameters_type(parameters) -> bool:
    return True


def validate_connections(connections: List[Tuple[int, int]],
                         protein_length: int) -> bool:
    connections = [(min(a, b), max(a, b)) for a, b in connections]
    connections.sort()

    if connections[len(connections) - 1][1] > protein_length:
        return False
    for i in range(len(connections) - 1):
        if connections[i][1] >= connections[i + 1][0]:
            return False
    return True
