from neo4j import GraphDatabase


def get_driver(uri, user, password):
    return GraphDatabase.driver(uri, auth=(user, password))

def close(driver):
    driver.close()

def create_specie(driver, name):
    res = driver.session().run("CREATE (s:Specie {name: $name}) RETURN s", name=name)
    return res.single()

def get_all(driver):
    res = driver.session().run("MATCH (n) RETURN n")
    return res.values()
