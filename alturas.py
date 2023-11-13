TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """7
165 169 153 155 155 185 172
181 156 160 173 178 167 179""",
        """11
170 172 180 181 174 179 179 183 185 190 192
155 157 165 165 174 172 173 173 183 182 181""",
        """4
150 149 167 175
161 173 172 180""",
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

    n_membros = int(input())
    equipes = [list(map(int, input().split())) for _ in range(2)]
    resultados = []

    equipe_vencedora, melhor_resultado = 1, 0

    for e, equipe in enumerate(equipes):
        lista_possibilidades = []
        for a, altura in enumerate(equipe):
            mudanca = False
            if a > 0:
                for p in range(len(lista_possibilidades)):
                    if lista_possibilidades[p][-1] <= altura:
                        lista_possibilidades.append(
                            copy.deepcopy(lista_possibilidades[p])
                        )
                        lista_possibilidades[p].append(altura)
                        lista_possibilidades.sort(key=len, reverse=True)
                        mudanca = True
                        break
            if not mudanca or a == 0:
                lista_possibilidades.append([altura])
        if e == 0:
            melhor_resultado = len(lista_possibilidades[0])
        elif len(lista_possibilidades[0]) == melhor_resultado:
            equipe_vencedora = "EMPATE"
        elif len(lista_possibilidades[0]) > melhor_resultado:
            equipe_vencedora = 2
            melhor_resultado = len(lista_possibilidades[0])

    print(f"{equipe_vencedora} {melhor_resultado}")

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
