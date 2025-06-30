from ListaAutor import ListaAutor
from PilhaLivro import PilhaLivro
from Livro import Livro

def main():
    lista_autores = ListaAutor()
    pilha_livros = PilhaLivro()

    while True:
        print( "\n===== MENU =====" )
        print( "1. Adicionar autor" )
        print( "2. Listar autores" )
        print( "3. Adicionar livro" )
        print( "4. Remover livro" )
        print( "5. Listar livros" )
        print( "0. Sair" )

        opcao = input( "Escolha uma opção: " )

        if opcao == "1":
            nome = input( "Nome do autor: " )
            nacionalidade = input("Nacionalidade: ")
            lista_autores.adicionarAutor( nome, nacionalidade )

        elif opcao == "2":
            print( "\n--- Lista de Autores ---" )
            lista_autores.imprimir()

        elif opcao == "3":
            titulo = input( "Título do livro: " )
            nome_autor = input( "Nome do autor: " )
            autor = lista_autores.buscarAutor( nome_autor )
            if autor:
                paginas = int( input( "Número de páginas: " ) )
                livro = Livro( titulo, autor, paginas )
                pilha_livros.add( livro )
            else:
                print( "Autor não encontrado! Cadastre o autor antes." )

        elif opcao == "4":
            pilha_livros.remover()

        elif opcao == "5":
            print( "\n--- Pilha de Livros ---" )
            pilha_livros.imprimir()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

"""
Implemente uma Pilha de livros e uma Lista Encadeada de autores. A lista de autores deve conter os autores ordenados pelo nome do autor.
A classe Livro deve conter os atriburos
título: String
autor: Autor
páginas: int
A classe Autor deve conter os atributos:
nome: String
nacionalidade: String
Monte um menu que permita adicionar e remover livros, adicionar autores e imprimir a lista de autores e a pilha de livros.
"""