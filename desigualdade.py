# Média considerada justa
media_justa = 12062

# Dados das cidades
cidades = {
    "1": ("Barueri", 1560),
    "2": ("Osasco", 3330),
    "3": ("Mogi das Cruzes", 4274),
    "4": ("Guarulhos", 6194)
}

print("=" * 50)
print(" ANALISADOR DE DESIGUALDADE SALARIAL")
print("=" * 50)

while True:
    print("\nEscolha uma cidade:")
    print("1 - Barueri")
    print("2 - Osasco")
    print("3 - Mogi das Cruzes")
    print("4 - Guarulhos")
    print("5 - Analisar todas")
    print("0 - Sair")

    opcao = input("\nDigite sua opção: ")

    if opcao == "0":
        print("\n Encerrando programa...")
        break

    elif opcao == "5":
        print("\n RELATÓRIO GERAL")
        print("-" * 50)

        for cidade, salario in cidades.values():
            diferenca = media_justa - salario

            print(f"\n Cidade: {cidade}")
            print(f" Salário médio: R$ {salario:,.2f}")
            print(f" Média justa: R$ {media_justa:,.2f}")
            print(f" Diferença: R$ {diferenca:,.2f}")

    elif opcao in cidades:
        cidade, salario = cidades[opcao]

        diferenca = media_justa - salario
        percentual = (diferenca / media_justa) * 100

        print("\n" + "=" * 50)
        print(f" Cidade analisada: {cidade}")
        print("=" * 50)

        print(f" Salário médio: R$ {salario:,.2f}")
        print(f" Média justa: R$ {media_justa:,.2f}")
        print(f" Diferença salarial: R$ {diferenca:,.2f}")
        print(f" Desigualdade: {percentual:.2f}%")

        if percentual > 50:
            print(" Alto nível de desigualdade salarial.")
        elif percentual > 20:
            print(" Nível moderado de desigualdade salarial.")
        else:
            print(" Situação próxima da média justa.")

    else:
        print(" Opção inválida!")