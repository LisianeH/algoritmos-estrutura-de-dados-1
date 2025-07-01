def media( valores ):
    qnt = len( valores )
    num = 0
    for x in valores:
        num += x
    return num / qnt

valores = [ 5, 10, 15 ], [ 2 , 4 ]

resultado = map( media, valores )
print( list( resultado ) )