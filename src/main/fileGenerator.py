import os
from typing import List, Tuple


def generate_all_files(learning: List[str],
                       positive: List[str],
                       negative: List[str],
                       connections: List[Tuple[int, int]]) -> None:
    if not os.path.exists("./output"):
        os.makedirs("./output")

    generate_file(learning, 'learning')
    generate_file(positive, 'positive')
    generate_file(negative, 'negative')

    generate_connection_text_file(connections, len(learning), 'learning')
    generate_connection_text_file(connections, len(positive), 'positive')
    generate_connection_text_file(connections, len(negative), 'negative')


def generate_file(proteins: List[str],
                  title: str) -> None:
    with open('./output/' + title + '.txt', 'w') as file:
        for i in range(len(proteins)):
            string = proteins[i]
            file.write('>' + title + f'_{str(i).zfill(7)}\n')
            file.write(f'{string}\n')


def generate_connection_text_file(connections: List[Tuple[int, int]],
                                  number_of_strings: int,
                                  title: str) -> None:
    with open('./output/' + title + '_connections.txt', 'w') as file:
        for i in range(number_of_strings):
            file.write('>' + title + f'_{str(i).zfill(7)}\n')
            for connection in connections:
                string = str(connection[0]) + "\t#\t" + str(connection[1])
                file.write(f'{string}\n')
