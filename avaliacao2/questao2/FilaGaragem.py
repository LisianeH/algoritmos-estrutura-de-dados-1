from Apartamento import Apartamento

class FilaGaragem:

    def __init__( self ):
        self.inicio = None

    def cadastrar( self, id, numApartamento, torre ):
        nodo = Apartamento( id, numApartamento, torre )
        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.prox is None:
            self.inicio.prox = nodo
        else: 
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        print( "\nApartamento cadastrado com sucesso!" )

    def removerPrimeiroDaFila( self ):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            numGaragem = input( f"Digite o número da GARAGEM para o apartamento: " )
            self.numGaragem = numGaragem
            print( "\nApartamento removido da lista de espera com sucesso!" )
        else: 
            print( "Não há elemento a ser removido" )

    def imprimir( self ):
        if self.inicio == None:
            print( "Sem apartamentos na lista de espera!" )
        else:
            aux = self.inicio
            while aux != None:
                print( f"\nApartamento: {aux.numApartamento}, ID: {aux.id}" )
                aux = aux.prox