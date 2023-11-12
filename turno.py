TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """1
5 0
0 0""",
        """5
5 0
0 0""",
        """5
10 10
0 0""",
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

    import math

    dist_turno = int(input())
    coordenadas_elfo = [int(x) for x in input().split()]
    coordenadas_tesouro = [int(x) for x in input().split()]
    PX, PY = coordenadas_elfo[0], coordenadas_elfo[1]
    TX, TY = coordenadas_tesouro[0], coordenadas_tesouro[1]

    dist = ((PX - TX) ** 2 + (PY - TY) ** 2) ** 0.5

    turnos_minimo = math.ceil(dist / dist_turno)

    print(turnos_minimo)

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
