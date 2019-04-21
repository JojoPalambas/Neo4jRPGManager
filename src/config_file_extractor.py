import neo4j_poster as np
import neo4j_getter as ng
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


def interpret_file(filename):
    instructions = get_instructions_from_file(filename)

    i = 0
    for instr in instructions:
        i += 1
        print("[", int((i / len(instructions) * 100)), "%]", sep="")
        if instr[0] == "node":
            if instr[1] == "specie":
                np.create_specie(instr[2])
            if instr[1] == "generic_specie":
                np.create_generic_specie(instr[2])
            if instr[1] == "specie_modif":
                np.create_specie_modif(instr[2])
            elif instr[1] == "class":
                np.create_class(instr[2])
            elif instr[1] == "generic_class":
                np.create_generic_class(instr[2])
            elif instr[1] == "biome":
                np.create_biome(instr[2])
        elif instr[0] == "link":
            if instr[1] == "specie-class":
                np.link_specie_to_class(instr[2], instr[3])
            if instr[1] == "specie-generic_specie":
                np.link_specie_to_generic_specie(instr[2], instr[3])
            if instr[1] == "specie-specie_modif":
                np.link_specie_to_specie_modif(instr[2], instr[3])
            if instr[1] == "class-generic_class":
                np.link_class_to_generic_class(instr[2], instr[3])
            if instr[1] == "specie-biome":
                np.link_specie_to_biome(instr[2], instr[3])
            if instr[1] == "class-biome":
                np.link_class_to_biome(instr[2], instr[3])


def interpret_matrix_file(filename):
    data = get_matrix_from_file(filename)

    type = data[0]
    column_labels = data[1]
    labelled_line = data[2]

    i = 0
    for ll in labelled_line:
        i += 1
        line_label = ll[0]
        print("[", int((i / len(labelled_line) * 100)), "%] ", line_label, sep="")
        line = ll[1]
        for j in range(len(line)):
            if line[j] == "x":
                if type == "specie-class":
                    np.link_specie_to_class(column_labels[j], line_label)
                if type == "specie-generic_specie":
                    np.link_specie_to_generic_specie(column_labels[j], line_label)
                if type == "specie-specie_modif":
                    np.link_specie_to_specie_modif(column_labels[j], line_label)
                if type == "class-generic_class":
                    np.link_class_to_generic_class(column_labels[j], line_label)
                elif type == "specie-biome":
                    np.link_specie_to_biome(column_labels[j], line_label)
                elif type == "class-biome":
                    np.link_class_to_biome(column_labels[j], line_label)
