from decimal import Decimal

class Sku:
    """A unique identifier for each distinct product and services that can be
    ordered from a supplier."""

    id = ''

    pn = ''
    supplier = ''

    description = ''

    price = Decimal()

    stock = 0

    def cost(self,qty):
        """Calculate cost for x units"""
        return self.price * qty

    @staticmethod
    def load(path):
        self = Sku()
        self._path = path
        self.id = path.split('/')[-1]

        from util import fromfile
        def get(n,f = str):
            self.__dict__[n] = f(fromfile(path + '/' + n))
        get('pn')
        get('supplier')
        get('description')
        get('price',Decimal)
        get('stock',int)

        return self

    def save(self):
        from util import tofile
        def put(n):
            tofile(self._path + '/' + n,str(self.__dict__[n]))
        put('pn')
        put('supplier')
        put('description')
        put('price')
        put('stock')

    def __hash__(self):
        return hash(self.id)
