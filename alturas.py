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

    for equipe in equipes:
        lista_possibilidades = []
        for a, altura in enumerate(equipe):
            mudanca = False
            if a > 0:
                nova_possibilidade = []
                for p in range(len(lista_possibilidades)):
                    if lista_possibilidades[p][-1] <= altura:
                        lista_possibilidades.append(
                            copy.deepcopy(lista_possibilidades[p])
                        )
                        lista_possibilidades[p].append(altura)
                        mudanca = True
            if not mudanca or a == 0:
                lista_possibilidades.append([altura])
        lista_len_possibilidades = [
            len(possibilidade) for possibilidade in lista_possibilidades
        ]
        resultados.append(max(lista_len_possibilidades))

    if resultados[0] == resultados[1]:
        print(f"EMPATE {resultados[0]}")
    else:
        resultado_melhor = max(resultados)
        equipe_vencedora = resultados.index(resultado_melhor) + 1
        print(f"{equipe_vencedora} {resultado_melhor}")

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
