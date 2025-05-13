from Produto import Produto

class Desktop( Produto ):

    def __init__( self, modelo, cor, preco, categoria, potenciaDaFonte ):
        super().__init__( modelo, cor, preco, categoria )
        self._potenciaDaFonte = potenciaDaFonte

    def cadastrar( self ):
        super().cadastrar 
        self.modelo = input( "Digite o modelo: " )
        self.cor = input( "Digite a cor: " )
        self.preco = input( "Digite o preço: " )
        self.categoria = input( "Digite a categoria: " )
        self._potenciaDaFonte = input( "Digite a potência da fonte: " )

    @property
    def getInformacoes( self ):
        return super().getInformacoes() + f"\nPotência da Fonte:  { self._potenciaDaFonte }"

    @_potenciaDaFonte.setter
    def _potenciaDaFonte( self, valor ):
        self._potenciaDaFonte = valor
    
    @property
    def _potenciaDaFonte( self ):
        return f"\nPotência da Fonte:  { self._potenciaDaFonte }"
    
    def cadastrar( self ):
        print( "Desktop cadastrado com sucesso!" )
        print( self.getInformacoes() )