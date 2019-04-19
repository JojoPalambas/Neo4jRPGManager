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


def create_class(driver, name):
    res = driver.session().run("CREATE (c:Class {name: $name}) RETURN c", name=name)
    return res.single()


def create_biome(driver, name):
    res = driver.session().run("CREATE (b:Biome {name: $name}) RETURN b", name=name)
    return res.single()


def link_specie_to_class(driver, specie_name, class_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (c:Class {name: $class_name})"
                               "CREATE (s)-[r:CAN_BE]->(c) RETURN r", specie_name=specie_name, class_name=class_name)


def link_specie_to_biome(driver, specie_name, biome_name):
    res = driver.session().run("MATCH (s:Specie {name: $specie_name}), (b:Biome {name: $biome_name})"
                               "CREATE (s)-[r:CNA_LIVE_IN]->(b) RETURN r", specie_name=specie_name, biome_name=biome_name)


def link_class_to_biome(driver, class_name, biome_name):
    res = driver.session().run("MATCH (c:Class {name: $class_name}), (b:Biome {name: $biome_name})"
                               "CREATE (c)-[r:CAN_BE]->(b) RETURN r", class_name=class_name, biome_name=biome_name)
