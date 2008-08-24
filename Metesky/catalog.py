from Metesky.sku import Sku
import os
import stat
import urllib
from decimal import Decimal

class Catalog(dict):
    """The master set of Sku's"""

    @staticmethod
    def load(path):
        self = Catalog()
        self._path = path

        for i in os.listdir(self._path + '/skus/'):
            i = self._path + '/skus/' + i

            # should only contain directories
            if not stat.S_ISDIR(os.stat(i)[stat.ST_MODE]):
                raise Exception('%s is not a directory' % i)

            s = Sku.load(i)
            assert(s not in self)
            self[s.id] = s
        return self

    def update_sku(self,
                   id = '',
                   stock = '',
                   pn = '',
                   description = '',
                   supplier = '',
                   price = Decimal()): 

        # new sku?
        if not id in self:
            s = Sku()
            s._path = self._path + '/skus/' + urllib.quote_plus(id)
            os.mkdir(s._path)

            s.id = id
            s.stock = 0 # FIXME: zero stock out for now 
            s.pn = pn
            s.description = description
            s.supplier = supplier
            s.price = price


            s.save()
            self[id] = s
        else:
            print '%s already exists' % id


from os.path import expanduser
catalog = Catalog.load(expanduser('~/.metesky'))
