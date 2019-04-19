import config_file_extractor as cfe
import neo4j_communicator as nc


driver = nc.get_driver("bolt://localhost:7687", "neo4j", "azerty")
nc.reset(driver)
cfe.interpret_file(driver, "../data")
#cfe.interpret_matrix_file(driver, "../data_matrix_specie-class")
nc.close(driver)
