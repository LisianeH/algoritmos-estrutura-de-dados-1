nomes = ['Camisa', 'Jeans', 'Meia']
precos = [68.99, 143.90, 12.00]
quantidades = [30, 50, 100]

def imprimir_produto(indice):
    if 0 <= indice < len(nomes):
        print(f"Produto: {nomes[indice]}")
        print(f"Preço: R$ {precos[indice]:.2f}")
        print(f"Quantidade: {quantidades[indice]}")
    else:
        print("Índice inválido.")

def retirar_produto(indice):
    if 0 <= indice < len(nomes):
        print(f"Produto removido: {nomes[indice]}")
        nomes.pop(indice)
        precos.pop(indice)
        quantidades.pop(indice)
    else:
        print("Índice inválido.")

imprimir_produto(1)
print("----------")
retirar_produto(0)
print("----------")
imprimir_produto(0)
