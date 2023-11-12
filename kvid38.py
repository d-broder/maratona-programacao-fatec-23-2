TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """00001
00001
00011
00111
01111""",
        """10000
01110
00100
01000
11000""",
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

    import copy

    def infecta(matriz, l, n):
        cont = 0
        for dl, dn in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nl, nn = l + dl, n + dn
            if 0 <= nl < 5 and 0 <= nn < 5 and matriz[nl][nn] == "1":
                cont += 1
            if cont >= 2:
                return True
        return False

    matriz = [list(input()) for _ in range(5)]

    while True:
        matriz_inicial = copy.deepcopy(matriz)

        for l in range(5):
            for n in range(5):
                if matriz[l][n] == "0":
                    if infecta(matriz, l, n):
                        matriz[l][n] = "1"

        if matriz == matriz_inicial:
            break

    for linha in matriz:
        print("".join(linha))

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
