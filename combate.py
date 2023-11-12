TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """1
15 15
7
N 3 7
19
N 14 1
12
N 17 9
8
V 11 5
13
N 3 8
16
D 15 12
20
V 16 18
7""",
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

    qttd_monstros = int(input())

    m = 0
    monstros = [list(map(int, input().split())) for _ in range(qttd_monstros)]

    n_rolagens = int(input())

    for i in range(n_rolagens):
        fim = False
        atrib_jogador = [
            int(atributo) if atributo.isdigit() else atributo
            for atributo in input().split()
        ]
        dano_jogador = int(input())

        atq = atrib_jogador[1]
        if atrib_jogador[0] == "V":
            atq = max(atrib_jogador[1], atrib_jogador[2])
        elif atrib_jogador[0] == "D":
            atq = min(atrib_jogador[1], atrib_jogador[2])
        atq = int(atq)

        if atq > monstros[m][0]:
            monstros[m][1] -= dano_jogador
            if monstros[m][1] <= 0:
                m += 1
                if m >= qttd_monstros:
                    print("VITORIA")
                    fim = True
        if fim:
            break
    if m < qttd_monstros:
        print("DERROTA")

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
