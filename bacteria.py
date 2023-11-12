TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """3
-3 2 5
-4 -1 1
-1 5 3""",
    ]

    n_inputs = len(input_sets)

    input_index_interno = 0

    def input():
        global input_set_index, input_index_interno
        value = input_sets[input_set_index].split("\n")[input_index_interno]
        input_index_interno += 1
        return value

else:
    n_inputs = 1

while input_set_index < n_inputs:
    if TEST_MODE:
        print(input_sets[input_set_index])
        print(" - " * 10)

    # Código principal:

    n_bacterias = int(input())

    bacterias = []
    for _ in range(n_bacterias):
        bacteria_0 = input().split()
        bacteria = [int(x) for x in bacteria_0]
        bacterias.append(bacteria)

    cont_bacterias = []

    for b1, bacteria1 in enumerate(bacterias):
        cont = 0
        x1, y1, r1 = bacteria1[0], bacteria1[1], bacteria1[2]
        for b2, bacteria2 in enumerate(bacterias):
            if b2 != b1:
                x2, y2, r2 = bacteria2[0], bacteria2[1], bacteria2[2]
                dr = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if dr + r2 < r1:
                    cont += 1
        cont_bacterias.append(cont)

    maior = max(cont_bacterias)
    print(maior)

    maior_bacteria = cont_bacterias.index(maior)
    print(f"{bacterias[maior_bacteria][0]} {bacterias[maior_bacteria][1]}")

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
