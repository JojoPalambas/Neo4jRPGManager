import config_file_extractor as cfe
import neo4j_poster as np
import neo4j_getter as ng
import time


start = time.time()
np.open("bolt://localhost:7687", "neo4j", "azerty")
ng.open("bolt://localhost:7687", "neo4j", "azerty")
print("========== DATA RESET")
np.reset()
print("========== NODES CREATION")
cfe.interpret_file("../data")
print("========== SPECIE-TO-CLASS LINKS")
cfe.interpret_matrix_file("../data_matrix_specie-class")
print("========== SPECIE-TO-SPECIE_MODIF LINKS")
cfe.interpret_matrix_file("../data_matrix_specie-specie_modif")
print("========== CLASS-TO-GENERIC_CLASS LINKS")
cfe.interpret_matrix_file("../data_matrix_class-generic_class")
np.close()
ng.close()

print("Program finished in ", time.time() - start, " seconds.", sep="")