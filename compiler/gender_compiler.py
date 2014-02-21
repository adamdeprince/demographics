from bz2 import BZ2File
from csv import DictReader
from sys import stdin, stderr
from collections import namedtuple

def load(fn):
    data = (s.split()[:2] for s in BZ2File(fn))
    data = (s for s in data if len(s) == 2)
    return dict((a,float(b)) for a,b in data)


male = load('data/dist.male.first.bz2')
female = load('data/dist.female.first.bz2')

_G = namedtuple('G', ('m', 'f'))
class G(_G):
    def __repr__(self):
        def convert(i):
            i = str(i)
            while i.endswith('0'):
                i = i[:-1]
            if not i.endswith('.'):
                i = i[1:]
            if i == "0.":
                i = "Z"
            return i
            
        return "G(%s,%s)" % tuple(map(convert, self))


both = {}
for name in set(male.keys() + female.keys()):
    both[name] = G(male.get(name, 0.0), female.get(name, 0.0))

print "from collections import namedtuple"
print "Z = 0.0"
print "G = namedtuple('G', ('m', 'f'))"
print "data = %r" % both
print "del(Z)"

