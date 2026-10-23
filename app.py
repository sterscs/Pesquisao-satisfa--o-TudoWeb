
excelente = 0
ruim = 0

for i in range(1, 51):
    print("Entrevistado", i)

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 2:
        print("Opinião registrada: BOM")
    elif opiniao == 3:
        ruim = ruim + 1
    else:
        print("Opinião inválida!")

    print("Obrigado por participar da pesquisa!")
    print("-----------------------------")

print("RESULTADO FINAL DA PESQUISA")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)