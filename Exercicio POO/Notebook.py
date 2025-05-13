from Produto import Produto

class Notebook( Produto ):

    def __init__( self, modelo, cor, preco, categoria, tempoDeBateria ):
        super().__init__( modelo, cor, preco, categoria ) 
        self.__tempoDeBateria = tempoDeBateria

    def cadastrar( self ):
        super().cadastrar 
        self.modelo = input( "Digite o modelo: " )
        self.cor = input( "Digite a cor: " )
        self.preco = input( "Digite o preço: " )
        self.categoria = input( "Digite a categoria: " )
        self.__tempoDeBateria = input( "Digite o tempo de bateria: " )
    
    @property
    def getInformacoes( self ):
        return super().getInformacoes() + f"\nTempo de bateria:  { self.__tempoDeBateria }"

    
    @__tempoDeBateria.setter
    def __tempoDeBateria( self, valor ):
        self.__tempoDeBateria = valor
    
    @property
    def __tempoDeBateria( self ):
        return f"\nTempo de bateria:  { self.__tempoDeBateria }"
    
    def cadastrar( self ):
        print( "Notebook cadastrado com sucesso!" )
        print( self.getInformacoes() )