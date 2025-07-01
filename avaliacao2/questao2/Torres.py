from Torre import Torre

class Torres: 

    def __init__( self ):
        self.topo  = None
        self.prox = None

    def cadastrar( self, id, nome, endereco ):
        nodo = Torre( id, nome, endereco )
        if self.topo:
            nodo.prox = self.topo
        self.topo = nodo
        print( "\nTorre cadastrada com sucesso!" )

    def buscarTorres(self, nome):
        atual = self.topo
        while atual is not None:
            if atual.nome.lower() == nome.lower():
                return atual
            atual = atual.prox
        return None
    
    def imprimir( self ):
        print( "*************************" )
        if self.topo == None:
            print( "Não há torres cadastradas!" )
        else:
            aux = self.topo
            while aux:
                print( "------------------------" )
                print( "ID torre: ", aux.id )
                print( "Nome: " , aux.nome )
                print( "Endereço: " , str( aux.endereco ) )
                aux = aux.prox
        print( "*************************" )