from Autor import Autor 

class ListaAutor:

    def __init__ ( self ):
        self.inicio = None
    
    def adicionarAutor( self, nome, nacionalidade ):
        novo = Autor( nome, nacionalidade )
        if self.inicio is None or nome.lower() < self.inicio.nome.lower():
            novo.prox = self.inicio
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.prox is not None and atual.prox.nome.lower() < nome.lower():
                atual = atual.prox
            novo.prox = atual.prox
            atual.prox = novo

    def imprimir( self ):
        if self.inicio == None:
            print( "Sem autores cadastrados!" )
        else:
            aux = self.inicio
            while aux != None:
                print( f"\nAutor: {aux.nome}, nacionalidade: {aux.nacionalidade}" )
                aux = aux.prox

    def buscarAutor(self, nome):
        atual = self.inicio
        while atual is not None:
            if atual.nome.lower() == nome.lower():
                return atual
            atual = atual.prox
        return None