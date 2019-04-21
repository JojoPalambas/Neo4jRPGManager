import config_file_extractor as cfe
import neo4j_getter as ng
import time


start = time.time()
ng.open("bolt://localhost:7687", "neo4j", "azerty")
for c in ng.get_classes_by_specie("Nain"):
    print(c)
ng.close()

print("Program finished in ", time.time() - start, " seconds.", sep="")