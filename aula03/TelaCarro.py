import sys 
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from Carro import Carro

class TelaCarro ( TelaVeiculo ):

    def __init__( self, titulo = "Tela Carro", categorias = [], telaCat = None ):
        self.listaCategorias = categorias
        self.telaCategoria = telaCat
        self.telaCategoria.telaCarro = self 
        super().__init__( titulo ) #função super() afirma que o init da superclasse será a mesma da declarada de quem ela herda. Neste caso, a classe TelaCarro recebe os mesmos parâmateros e funções de TelaVeiculo
        self.setGeometry( 450, 150, 300, 300 )

    def definirLayout( self ): #estou redefinindo uma função que já existe e herdei de TelaVeiculo,o nome disto é POLIMORFISMO: o ato de alterar funções de classes herdadas, mas mantendo outras comooriginalmente são.
        super().definirLayout()
        self.lblPortas = QLabel("Quantidade de Portas: ")
        self.txtPortas = QLineEdit( self ) #QLineEdit recebe somente o que a própria classe recebe, por isto self
        self.layout.addWidget( self.lblPortas )
        self.layout.addWidget( self.txtPortas )

        self.lblCategoria = QLabel("Categoria ")
        self.layout.addWidget( self.lblCategoria )

        self.comboBoxCategoria = QComboBox( self )
        self.carregarCategorias()
        self.layout.addWidget( self.comboBoxCategoria )

        self.botaoAbrirTelaCategoria = QPushButton( "Adicionar Categoria", self )
        self.botaoAbrirTelaCategoria.clicked.connect( self.abrirTelaCategoria )
        self.layout.addWidget( self.botaoAbrirTelaCategoria )

    def abrirTelaCategoria( self ):
        
        self.telaCategoria.show()

    def carregarCategorias( self ):
        self.comboBoxCategoria.clear()
        self.comboBoxCategoria.addItem( "Selecione...", None )
        for cat in self.listaCategorias:
            self.comboBoxCategoria.addItem( cat.nome, cat )

    def salvar( self ):
        modelo = self.txtModelo.text() 
        ano = self.txtAno.text()
        if( ano != "" ): 
            ano = int( ano ) 
        portas = self.txtPortas.text()
        if portas != '':
            portas = int( portas )
        carro = Carro( modelo, ano, portas ) 
        QMessageBox.information( self, "Carro salvo", str( carro ) )
    
