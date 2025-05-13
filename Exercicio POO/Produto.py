from abc import ABC, abstractmethod

class Produto( ABC ):

    def __init__( self, modelo, cor, preco, categoria ):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    @property
    def getInformacoes( self ):
        desc = f'''
            Modelo: { self.modelo }
            Cor: { self.cor }
            Preço: { self.preco }
            Categoria: { self.categoria }
        '''
        return desc

    @abstractmethod
    def cadastrar():
        pass