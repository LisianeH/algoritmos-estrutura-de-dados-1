from Torre import Torre

class Apartamento:

    def __init__( self, id, numApartamento, numGaragem=None ):
        self.id = id
        self.numApartamento = numApartamento
        self.numGaragem = numGaragem
        self.torre = Torre
        self.prox = None

    def cadastrar( self ):
        pass

    def imprimir( self ):
        pass