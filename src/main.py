import config_file_extractor as cfe
import neo4j_communicator as nc


nc.open("bolt://localhost:7687", "neo4j", "azerty")
nc.reset()
cfe.interpret_file("../data")
cfe.interpret_matrix_file("../data_matrix_specie-class")
nc.close()
