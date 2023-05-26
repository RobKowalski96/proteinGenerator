from typing import Dict, List, Tuple, Union

from variables import AMINOACIDS_FREQUENCY_FILE
from variables import CONNECTIONS_FILE
from variables import NEGATIVE_AMINOACIDS_FILE
from variables import NEUTRAL_AMINOACIDS_FILE
from variables import POSITIVE_AMINOACIDS_FILE
from variables import AMINOACIDS_FREQUENCY
from variables import CONNECTIONS
from variables import NEGATIVE_AMINOACIDS
from variables import NEUTRAL_AMINOACIDS
from variables import POSITIVE_AMINOACIDS

AMINOACIDS_FREQUENCY_FILE_DELIMITER = "\t"
CONNECTIONS_FILE_DELIMITER = "\t#\t"


def get_configuration(file_path: str) -> Dict[str, Union[str, int, Dict[str, float], List[Tuple[int, int]], List[str]]]:
    parameters = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line:
                key, value = line.split('=')
                value = value.strip()
                if key in ['proteinLength', 'learningSampleSize', 'positiveSampleSize', 'negativeSampleSize']:
                    value = int(value)
                parameters[key.strip()] = value

    load_parameters_from_files(parameters)

    return parameters


def load_parameters_from_files(parameters):
    parameters[AMINOACIDS_FREQUENCY] = load_probabilities(parameters.get(AMINOACIDS_FREQUENCY_FILE))
    parameters.pop(AMINOACIDS_FREQUENCY_FILE)
    parameters[CONNECTIONS] = load_connections(parameters.get(CONNECTIONS_FILE))
    parameters.pop(CONNECTIONS_FILE)
    parameters[NEGATIVE_AMINOACIDS] = load_aminoacids_list(parameters.get(NEGATIVE_AMINOACIDS_FILE))
    parameters.pop(NEGATIVE_AMINOACIDS_FILE)
    parameters[NEUTRAL_AMINOACIDS] = load_aminoacids_list(parameters.get(NEUTRAL_AMINOACIDS_FILE))
    parameters.pop(NEUTRAL_AMINOACIDS_FILE)
    parameters[POSITIVE_AMINOACIDS] = load_aminoacids_list(parameters.get(POSITIVE_AMINOACIDS_FILE))
    parameters.pop(POSITIVE_AMINOACIDS_FILE)


def load_probabilities(file_path: str) -> Dict[str, float]:
    probabilities = {}
    with open(file_path, "r") as f:
        for line in f:
            letter, number = line.strip().split(AMINOACIDS_FREQUENCY_FILE_DELIMITER)
            probabilities[letter] = float(number)
    return probabilities


def load_connections(file_path: str) -> List[Tuple[int, int]]:
    connections = []
    with open(file_path, "r") as f:
        for line in f:
            first_number, second_number = line.strip().split(CONNECTIONS_FILE_DELIMITER)
            connections.append((int(first_number), int(second_number)))
    return connections


def load_aminoacids_list(file_path: str) -> List[str]:
    amino_acids_list = []
    with open(file_path, "r") as f:
        for line in f:
            amino_acids_list.append(line.strip())
    return amino_acids_list
