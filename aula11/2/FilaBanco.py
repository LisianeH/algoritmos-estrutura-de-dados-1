from Banco import Banco

class FilaBanco:
    
    def __init__( self ):
        self.inicio = None
        self.fim = None

    def atenderCliente( self ):
        if self.inicio is not None:
            self.inicio = self.inicio.proximo
            if self.inicio == None:
                self.fim = None
            print( "Cliente antendido!" )
        else: 
            print( "Não há clientes para serem atendidos." )
        self.imprimir()

    def adicionaFila( self, nome, prioridade ):
        nodo = Banco( nome, prioridade )
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        elif prioridade == "P":
            if self.inicio.prioridade == "N":
                nodo.proximo = self.inicio
                self.inicio = nodo
            else:
                aux = self.inicio
                while aux.proximo is not None and aux.proximo.prioridade == "P":
                    aux = aux.proximo
                nodo.proximo = aux.proximo
                aux.proximo = nodo
                if nodo.proximo is None:
                    self.fim = nodo
        else:
            self.fim.proximo = nodo
            self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print( "----- Fila do Banco -----" )
        if self.inicio is None:
            print( "Fila está vazia!" )
        else:
            aux = self.inicio
            while aux is not None:
                print( str(aux) )
                aux = aux.proximo