from neo4j import GraphDatabase


driver = None
session = None


def open(uri, user, password):
    global driver
    global session
    driver = GraphDatabase.driver(uri, auth=(user, password))
    session = driver.session()


def close():
    driver.close()


def get_all():
    res = session.run("MATCH (n) RETURN n")
    session.sync()
    return res.values()


def get_classes_by_specie(name):
    res = session.run("MATCH (s:Specie {name: $name})-[:CAN_BE]->(c:Class) RETURN {class: c.name} ORDER BY c.name", name=name)
    session.sync()
    return res.values()


def get_species_by_class(name):
    res = session.run("MATCH (s:Specie)-[:CAN_BE]-(c:Class {name: $name}) RETURN {specie: s.name} ORDER BY s.name", name=name)
    session.sync()
    return res.values()
