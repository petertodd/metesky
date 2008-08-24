def tofile(name,v):
    open(name,'w').write(str(v) + '\n')

def fromfile(name):
    return open(name).read()[0:-1]
