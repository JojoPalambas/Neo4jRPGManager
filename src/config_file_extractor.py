

def get_instructions_from_file(filename):
    f = open(filename, "r")
    txt = f.read()
    f.close()

    instr = []
    for l in txt.split("\n"):
        instr.append(l.split(":"))
    return instr