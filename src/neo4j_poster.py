from neo4j import GraphDatabase


driver = None
session = None


def open(uri, user, password):
    global driver
    global session
    driver = GraphDatabase.driver(uri, auth=(user, password))
    session = driver.session()


def close():
    session.sync()
    driver.close()


def reset():
    session.run("MATCH (n) DETACH DELETE n")
    session.sync()


def create_specie(name):
    res = session.run("CREATE (s:Specie {name: $name}) RETURN s", name=name)
    session.sync()
    return res.single()


def create_generic_specie(name):
    res = session.run("CREATE (gs:GenericSpecie {name: $name}) RETURN gs", name=name)
    session.sync()
    return res.single()


def create_specie_modif(name):
    res = session.run("CREATE (sm:SpecieModif {name: $name}) RETURN sm", name=name)
    session.sync()
    return res.single()


def create_class(name):
    res = session.run("CREATE (c:Class {name: $name}) RETURN c", name=name)
    session.sync()
    return res.single()


def create_generic_class(name):
    res = session.run("CREATE (gc:GenericClass {name: $name}) RETURN gc", name=name)
    session.sync()
    return res.single()


def create_biome(name):
    res = session.run("CREATE (b:Biome {name: $name}) RETURN b", name=name)
    session.sync()
    return res.single()


def link_specie_to_class(specie_name, class_name):
    res = session.run("MATCH (s:Specie {name: $specie_name}), (c:Class {name: $class_name})"
                               "CREATE (s)-[r:CAN_BE]->(c) RETURN r", specie_name=specie_name, class_name=class_name)
    session.sync()


def link_specie_to_specie_modif(specie_name, specie_modif_name):
    res = session.run("MATCH (s:Specie {name: $specie_name}), (sm:SpecieModif {name: $specie_modif_name})"
                               "CREATE (s)-[r:CAN_BECOME]->(sm) RETURN r", specie_name=specie_name, specie_modif_name=specie_modif_name)
    session.sync()


def link_specie_to_generic_specie(specie_name, generic_specie_name):
    res = session.run("MATCH (s:Specie {name: $specie_name}), (gs:GenericSpecie {name: $generic_specie_name})"
                               "CREATE (s)-[r:IS_A_KIND_OF]->(gs) RETURN r", specie_name=specie_name, generic_specie_name=generic_specie_name)
    session.sync()


def link_class_to_generic_class(class_name, generic_class_name):
    print(class_name, generic_class_name)
    res = session.run('MATCH (c:Class {name: $class_name}), (gc:GenericClass {name: $generic_class_name})'
                      'CREATE (c)-[r:IS_A_KIND_OF]->(gc) RETURN r', class_name=class_name, generic_class_name=generic_class_name)
    session.sync()


def link_specie_to_biome(specie_name, biome_name):
    res = session.run("MATCH (s:Specie {name: $specie_name}), (b:Biome {name: $biome_name})"
                               "CREATE (s)-[r:CAN_LIVE_IN]->(b) RETURN r", specie_name=specie_name, biome_name=biome_name)
    session.sync()


def link_class_to_biome(class_name, biome_name):
    res = session.run("MATCH (c:Class {name: $class_name}), (b:Biome {name: $biome_name})"
                               "CREATE (c)-[r:CAN_BE_TRAINED_IN]->(b) RETURN r", class_name=class_name, biome_name=biome_name)
    session.sync()
