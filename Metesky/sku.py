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

    def __hash__(self):
        return hash(self.id)
