from Metesky.sku import Sku

class Catalog(set):
    """The master set of Sku's"""

    @staticmethod
    def load(path):
        self = Catalog()
        self._path = path

        import os
        import stat
        for i in os.listdir(self._path + '/skus/'):
            i = self._path + '/skus/' + i

            # should only contain directories
            if not stat.S_ISDIR(os.stat(i)[stat.ST_MODE]):
                raise Exception('%s is not a directory' % i)

            s = Sku.load(i)
            assert(s not in self)
            self.add(s)

        return self

from os.path import expanduser
catalog = Catalog.load(expanduser('~/.metesky'))
