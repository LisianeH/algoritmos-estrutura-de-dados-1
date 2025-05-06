from PyQt5.QtWidgets import *

class TelaProduto( QMainWindow ):

    def __init__( self, titulo = "Tela Produto", produtos = [], telaCarro = None ):
        self.listaProduto = produtos
        self.telaCarro = telaCarro
        super().__init__()

        self.setWindowTitle( titulo )
        self.setGeometry( 100, 150, 200, 100 ) 
        self.layout = QVBoxLayout()

        self.definirLayout()

        self.btnSalvar = QPushButton( "Salvar", self ) 
        self.btnSalvar.clicked.connect( self.__salvar ) 
        self.layout.addWidget( self.btnSalvar ) 

        container = QWidget() 
        container.setLayout( self.layout ) 
        self.setCentralWidget( container ) 
    
    def definirLayout( self ):
        self.lblNome = QLabel( "Nome: " )
        self.txtNome = QLineEdit( self ) 
        self.layout.addWidget( self.lblNome )
        self.layout.addWidget( self.txtNome )
    
    def __salvar( self ):
        nome = self.txtNome.text()
        if( nome != "" ):
            cat = Produto( nome )
            self.listaCategorias.append( cat )
            self.telaCarro.carregarCategorias()
            QMessageBox.information( self, "Categoria salva", str( cat ) )
            self.txtNome.text( "" )
            self.hide()