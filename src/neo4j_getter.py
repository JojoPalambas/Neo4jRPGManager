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
    return res.values()


def get_classes_by_specie(name):
    res = session.run("MATCH (s:Specie {name: $name})--(c:Class) RETURN {class: c.name} ORDER BY c.name", name=name)
    return res.values()
