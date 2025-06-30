from Livro import Livro

class PilhaLivro:

    def __init__( self ):
        self.topo  = None

    def add( self, book ):
        if self.topo:
            book.prox = self.topo
        self.topo = book
        print( "\nLivro cadastrado com sucesso!" )

    def remover( self ):
        if self.topo == None:
            print( "Pilha de Livros vazia!" )
        else:
            self.topo = self.topo.prox
            print( "\nLivro no topo da pilha removido!\n" )
        self.imprimir()

    def imprimir( self ):
        print( "*************************" )
        if self.topo == None:
            print( "Pilha está vazia!" )
        else:
            aux = self.topo
            while aux:
                print( "------------------------" )
                print( "Título: ", aux.titulo )
                print( "Autor: " , aux.autor.nome )
                print( "Páginas: " , str( aux.paginas ) )
                aux = aux.prox
        print( "*************************" )