from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido

c1 = Cidade()
c2 = Cidade( "Porto Alegre" )

p1 = Pessoa()
p2 = Pessoa( "João", cidade=c1 )

prod1 = Produto()
prod2 = Produto( "Coca-cola", qtde=100 )
prod3 = Produto( "Pepsi", 8.99, 50 )

ped1 = Pedido()
ped2 = Pedido( cliente=p2 )

ped2.addProd( prod3 )
ped2.addProd( prod2 )

print( ped2 )