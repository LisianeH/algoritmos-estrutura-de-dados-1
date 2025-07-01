from FilaGaragem import FilaGaragem
from Torres import Torres

def main():
    filaEspera = FilaGaragem()
    listaTorres = Torres()

    while True:
        print( "\n===== MENU =====" )
        print( "1. Adicionar apartamento na lista de espera" )
        print( "2. Remover apartamento na lista de espera" )
        print( "3. Listar todos da lista de espera" )
        print( "4. Cadastrar uma nova torre" )
        print( "5. Listar todas as torres cadastradas" )
        print( "0. Sair" )

        opcao = input( "Escolha uma opção: " )

        if opcao == "1":
            id = input( "ID do apartamento: " )
            numApartamento = input( "Número do apartamento: " )
            torre = input( "Nome da torre: " )
            torreBusca = listaTorres.buscarTorres( torre )
            if torreBusca:
                filaEspera.cadastrar( id, numApartamento, torreBusca )
            else:
                print( "Torre não encontrada! Cadastre a torre antes." )

        elif opcao == "2":
            filaEspera.removerPrimeiroDaFila()

        elif opcao == "3":
            print( "\n--- Fila de Espera ---" )
            filaEspera.imprimir()

        elif opcao == "4":
            id = input( "ID da torre: " )
            nome = input( "Nome da torre: " )
            endereco = input( "Endereço da torre: " )
            listaTorres.cadastrar( id, nome, endereco )

        elif opcao == "5":
            listaTorres.imprimir()

        elif opcao == "0":
            print( "Encerrando o programa..." )
            break

        else:
            print( "Opção inválida. Tente novamente." )

if __name__ == "__main__":
    main()