from configuratorReader import get_configuration
from fileGenerator import generate_all_files
from proteinGenerator import generate_proteins_with_connections
from proteinGenerator import generate_proteins_without_connections
from parametersValidator import validate_configuration
from variables import AMINOACIDS_FREQUENCY
from variables import CONNECTIONS
from variables import LEARNING_SAMPLE_SIZE
from variables import NEGATIVE_AMINOACIDS
from variables import NEGATIVE_SAMPLE_SIZE
from variables import NEUTRAL_AMINOACIDS
from variables import POSITIVE_AMINOACIDS
from variables import POSITIVE_SAMPLE_SIZE
from variables import PROTEIN_LENGTH

configuration_file = "./src/resources/configuration.txt"

parameters = get_configuration(configuration_file)

if validate_configuration(parameters):
    protein_length = parameters[PROTEIN_LENGTH]
    amino_acid_freq = parameters[AMINOACIDS_FREQUENCY]
    connections = parameters[CONNECTIONS]
    negative_amino_acids = parameters[NEGATIVE_AMINOACIDS]
    positive_amino_acids = parameters[POSITIVE_AMINOACIDS]
    neutral_amino_acids = parameters[NEUTRAL_AMINOACIDS]
    learning_sample_size = parameters[LEARNING_SAMPLE_SIZE]
    positive_sample_size = parameters[POSITIVE_SAMPLE_SIZE]
    negative_sample_size = parameters[NEGATIVE_SAMPLE_SIZE]

    learning = generate_proteins_with_connections(protein_length, amino_acid_freq, connections, negative_amino_acids,
                                                  positive_amino_acids, learning_sample_size)
    positive = generate_proteins_with_connections(protein_length, amino_acid_freq, connections, negative_amino_acids,
                                                  positive_amino_acids, positive_sample_size)
    negative = generate_proteins_without_connections(protein_length, amino_acid_freq, connections, negative_amino_acids,
                                                     positive_amino_acids, neutral_amino_acids, negative_sample_size)

    generate_all_files(learning, positive, negative, connections)
