import neo4j_communicator as nc
import time


def get_instructions_from_file(filename):
    f = open(filename, "r")
    txt = f.read()
    f.close()

    instr = []
    for l in txt.split("\n"):
        instr.append(l.split(":"))
    return instr

def get_matrix_from_file(filename):
    f = open(filename, "r")
    txt = f.read()
    f.close()

    lines = txt.split("\n")
    type = lines[0]
    lines = lines[1:]

    column_titles = lines[0].split("\t")[1:]
    lines = lines[1:]

    ret = [type, column_titles, []]
    for l in lines:
        splitted_l = l.split("\t")
        ret[2].append([splitted_l[0], splitted_l[1:]])
    return ret

def interpret_file(driver, filename):
    instructions = get_instructions_from_file(filename)

    i = 0
    for instr in instructions:
        i += 1
        print("[", int((i / len(instructions) * 100)), "%]", sep="")
        if instr[0] == "node":
            if instr[1] == "specie":
                nc.create_specie(driver, instr[2])
            elif instr[1] == "class":
                nc.create_class(driver, instr[2])
            elif instr[1] == "biome":
                nc.create_biome(driver, instr[2])
        elif instr[0] == "link":
            if instr[1] == "specie-class":
                nc.link_specie_to_class(driver, instr[2], instr[3])
            if instr[1] == "specie-biome":
                nc.link_specie_to_biome(driver, instr[2], instr[3])
            if instr[1] == "class-biome":
                nc.link_class_to_biome(driver, instr[2], instr[3])


def interpret_matrix_file(driver, filename):
    data = get_matrix_from_file(filename)
    
    type = data[0]
    species = data[1]
    labelled_line = data[2]

    i = 0
    for ll in labelled_line:
        i += 1
        print("[", int((i / len(labelled_line) * 100)), "%]", sep="")
        class_name = ll[0]
        line = ll[1]
        for j in range(len(line)):
            if type == "specie-class":
                nc.link_specie_to_class(driver, species[j], class_name)
            elif type == "specie-biome":
                nc.link_specie_to_biome(driver, species[j], class_name)
            elif type == "class-biome":
                nc.link_class_to_biome(driver, species[j], class_name)
