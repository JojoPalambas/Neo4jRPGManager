from neo4j import GraphDatabase


def get_driver(uri, user, password):
    return GraphDatabase.driver(uri, auth=(user, password))


def close(driver):
    driver.close()


def reset(driver):
    driver.session().run("MATCH (n) DETACH DELETE n")


def get_all(driver):
    res = driver.session().run("MATCH (n) RETURN n")
    return res.values()


def create_specie(driver, name):
    res = driver.session().run("CREATE (s:Specie {name: $name}) RETURN s", name=name)
    return res.single()


def create_generic_specie(driver, name):
    res = driver.session().run("CREATE (gs:GenericSpecie {name: $name}) RETURN gs", name=name)
    return res.single()


def create_specie_modif(driver, name):
    res = driver.session().run("CREATE (sm:SpecieModif {name: $name}) RETURN sm", name=name)
    return res.single()


def create_class(driver, name):
    res = driver.session().run("CREATE (c:Class {name: $name}) RETURN c", name=name)
    return res.single()


def create_generic_class(driver, name):
    res = driver.session().run("CREATE (gc:GenericClass {name: $name}) RETURN gc", name=name)
    return res.single()


def create_biome(driver, name):
    res = driver.session().run("CREATE (b:Biome {name: $name}) RETURN b", name=name)
    return res.single()


def link_specie_to_class(driver, specie_name, class_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (c:Class {name: $class_name})"
                               "CREATE (s)-[r:CAN_BE]->(c) RETURN r", specie_name=specie_name, class_name=class_name)


def link_specie_to_specie_modif(driver, specie_name, specie_modif_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (sm:SpecieModif {name: $specie_modif_name})"
                               "CREATE (s)-[r:CAN_BECOME]->(c) RETURN r", specie_name=specie_name, specie_modif_name=specie_modif_name)


def link_specie_to_generic_specie(driver, specie_name, generic_specie_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (gs:GenericSpecie {name: $generic_specie_name})"
                               "CREATE (s)-[r:IS_A_KIND_OF]->(gs) RETURN r", specie_name=specie_name, generic_specie_name=generic_specie_name)


def link_class_to_generic_class(driver, class_name, generic_class_name):
    res = driver.session().run("MATCH (c:Class {name: $class_name}), (gc:GenericClass {name: $generic_class_name})"
                               "CREATE (c)-[r:IS_A_KIND_OF]->(gc) RETURN r", class_name=class_name, generic_class_name=generic_class_name)


def link_specie_to_biome(driver, specie_name, biome_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (b:Biome {name: $biome_name})"
                               "CREATE (s)-[r:CAN_LIVE_IN]->(b) RETURN r", specie_name=specie_name, biome_name=biome_name)


def link_class_to_biome(driver, class_name, biome_name):
    res = driver.session().run("MATCH (c:Class {name: $class_name}), (b:Biome {name: $biome_name})"
                               "CREATE (c)-[r:CAN_BE_TRAINED_IN]->(b) RETURN r", class_name=class_name, biome_name=biome_name)
