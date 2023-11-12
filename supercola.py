TEST_MODE = True

input_set_index = 0
input_sets = []

if TEST_MODE:
    input_sets = [
        """10
JHZTEBEHQTRCFVRE""",
        """26
QBMNFJSBTAOBPAUFNANVOEJBM""",
        """7
FUMYFUMBWUTIUKUTWHFINMUWUH""",
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

    chave = int(input())
    mensagem_codificada = input()
    mensagem = ""

    alfabeto = " abcdefghijklmnopqrstuvwxyz".upper()

    for letra in mensagem_codificada:
        index_alfabeto = alfabeto.index(letra)
        index_mensagem = (index_alfabeto + chave) % 27
        mensagem += alfabeto[index_mensagem]
    print(mensagem)

    # Fim do código principal

    input_set_index += 1
    if TEST_MODE:
        input_index_interno = 0
        print("=-" * 15)
