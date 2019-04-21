import config_file_extractor as cfe
import neo4j_poster as np
import time


start = time.time()
np.open("bolt://localhost:7687", "neo4j", "azerty")
np.reset()
cfe.interpret_file("../data")
cfe.interpret_matrix_file("../data_matrix_specie-class")
np.close()

print("Program finished in ", time.time() - start, " seconds.", sep="")