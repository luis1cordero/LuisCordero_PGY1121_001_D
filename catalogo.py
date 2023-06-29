class libro:
    codigo = ''
    titulo = ''
    autor = ''
    precio = 0
    pais = ''
    categoria = ''
    an_pub = ''

    def __init__(self):
        self.codigo = ''
        self.titulo = ''
        self.autor = ''
        self.precio = 10000
        self.pais = ''
        self.categoria = ''
        self.an_pub = 0

    def selfCodigo(self,cod):
        self.codigo = cod
        if cod[1:3].isalpha and cod[3:6].isnumeric:
            c=True

    def selfPrecio(self,precio):
        precio=precio
        if precio<10000:
            print("el valor esta denajo del minimo (10.000)")
            return False