import sys


def initialState(line, i, tokens):

    char = line[i]

    if char == " ":
        return initialState, i + 1

    if char.isdigit():
        return numberState, i

    if char in ['+', '-', '*', '/', '%', '^']:

        if char == '/' and line[i + 1] == '/' and i + 1 < len(line):
            tokens.append(("OP", "//"))
            return initialState, i + 2

        tokens.append(("OP", char))
        return initialState, i + 1

    if char == '(':
        tokens.append(("LPARENT", char))
        return initialState, i + 1

    if char == ')':
        tokens.append(("RPARENT", char))
        return initialState, i + 1

    if char.isalpha():
        return wordState, i


def numberState(line, i, tokens):
    num = ""

    while line[i] != " " and i < len(line):
        num += line[i]
        i += 1

    tokens.append(("NUMBER", num))

    return initialState, i


def wordState(line, i, tokens):
    word = ""

    while line[i].isalpha():
        word += line[i]
        i += 1

    if word == "RES":
        tokens.append(("RES", word))
    elif word == "MEM":
        tokens.append(("MEM", word))
    else:
        print("Palavra desconhecida!")

    return initialState, i


def tokenGenerator(line):
    tokens = []
    state = initialState
    i = 0

    while i < len(line):
        state, i = state(line, i, tokens)

    return tokens


def assemblyGenerator(token, assembly, result, memory, label_id):
    pile = []
    recorder = 0

    for type, value in token:

        if type in ["LPARENT", "RPARENT"]:
            continue

        if type == "NUMBER":
            rec = "R" + str(recorder)
            assembly.append("MOV " + rec + ", #" + str(value))
            pile.append((rec, int(value)))
            recorder += 1

        elif type == "OP":
            if len(pile) < 2:
                raise ValueError("Operação inválida: poucos operandos")

            (b, b_val) = pile.pop()
            (a, a_val) = pile.pop()

            if value == "+":
                assembly.append("ADD " + a + ", " + a + ", " + b)
            elif value == "-":
                assembly.append("SUB " + a + ", " + a + ", " + b)
            elif value == "*":
                assembly.append("MUL " + a + ", " + a + ", " + b)
            elif value == "/" or value == "//":
                label_id += 1
                loop = f"div_loop_{label_id}"
                end = f"div_end_{label_id}"
                res = f"R{recorder}"
                recorder += 1

                assembly.append(f"MOV {res}, #0")
                assembly.append(f"{loop}:")
                assembly.append(f"CMP {a}, {b}")
                assembly.append(f"BLT {end}")
                assembly.append(f"SUB {a}, {a}, {b}")
                assembly.append(f"ADD {res}, {res}, #1")
                assembly.append(f"B {loop}")
                assembly.append(f"{end}:")
                assembly.append(f"MOV {a}, {res}")
            elif value == "%":
                label_id += 1
                loop = f"div_loop_{label_id}"
                end = f"div_end_{label_id}"
                res = f"R{recorder}"
                recorder += 1

                assembly.append(f"MOV {res}, #0")
                assembly.append(f"{loop}:")
                assembly.append(f"CMP {a}, {b}")
                assembly.append(f"BLT {end}")
                assembly.append(f"SUB {a}, {a}, {b}")
                assembly.append(f"ADD {res}, {res}, #1")
                assembly.append(f"B {loop}")
                assembly.append(f"{end}:")
                assembly.append(f"MOV {a}, {res}")
            elif value == "^":
                label_id += 1
                loop_label = f"loop_{label_id}"
                end_label = f"end_{label_id}"

                resultado = f"R{recorder}"
                recorder += 1

                assembly.append(f"MOV {resultado}, {a}")

                assembly.append(f"SUB {b}, {b}, #1")

                assembly.append(f"{loop_label}:")
                assembly.append(f"CMP {b}, #0")
                assembly.append(f"BEQ {end_label}")
                assembly.append(f"MUL {resultado}, {resultado}, {a}")
                assembly.append(f"SUB {b}, {b}, #1")
                assembly.append(f"B {loop_label}")
                assembly.append(f"{end_label}:")

                pile.append(resultado)
                continue

            pile.append((a, None))

        elif type == "MEM":
            if len(pile) >= 1:
                (rec, _) = pile.pop()
                assembly.append(f"MOV R10, {rec}")
                memory = "R10"

                pile.append("R10")
            else:
                pile.append(memory)

        elif type == "RES":
            (rec, n) = pile.pop()
            rec = result[-n]
            pile.append(rec)

    final_result = pile[-1]
    return assembly, final_result, memory, recorder, label_id


def saveAssembly(filename, assembly):
    with open(filename, "w") as f:
        f.write(".global _start\n\n")
        f.write("_start:\n")

        for instr in assembly:
            f.write("   " + instr + "\n")

        f.write("\nend:\n")
        f.write("   B end\n")


archive = sys.argv[1]

assembly = []
results = []
memory = None

label_id = 0

with open(archive, "r") as f:
    for line in f:
        print(line.strip())
        token = tokenGenerator(line.strip())
        print(token)
        asm, result, memory, recorder, label_id = assemblyGenerator(token, assembly, results, memory, label_id)

        results.append(result)

saveAssembly("saida.s", assembly)
