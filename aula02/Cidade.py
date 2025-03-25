class Cidade:

    def __init__( self, nome = "Porto Alegre" ):
        self.id = None
        self.nome = nome

    def __str__( self ):
        return "ID: " + str( self.id ) + "\n Nome da Cidade: " + self.nome