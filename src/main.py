import config_file_extractor as cfe
import neo4j_communicator as nc
import time


start = time.time()
nc.open("bolt://localhost:7687", "neo4j", "azerty")
nc.reset()
cfe.interpret_file("../data")
cfe.interpret_matrix_file("../data_matrix_specie-class")
nc.close()

print("Program finished in ", time.time() - start, " seconds.", sep="")