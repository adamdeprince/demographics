from bz2 import BZ2File
from csv import DictReader
from sys import stdin, stderr
data = {}
from collections import namedtuple

def f(s, d=100.0):
    if s == '(S)':
        return None
    
    return float(s) / d

def convert(i):
    if i is None:
        return "N"
    i = str(i)
    while i.endswith('0'):
        i = i[:-1]
    if i.startswith('0') and not i.endswith('.') and 'e' not in i:
        i = i[1:]
    if i == "0.":
        i = "Z"
    if 'e-0' in i:
        i = i.replace('e-0', 'e-')
    return i

_R = namedtuple('R', 'rate white black hispanic aian api multi'.split())
internment = {}
class R(_R):
    def __repr__(self):                
        if self in internment:
            return internment[self]
        return self.raw()
    def raw(self):
        return "R(%s)" % ",".join(map(convert, self))

tally = {}
for row in DictReader(BZ2File("data/app_c.csv.bz2")):
    row = dict(row)
    try:
        d = R(f(row['prop100k'], 100000), 
                f(row['pctwhite']),
                f(row['pctblack']),
                f(row['pcthispanic']),
                f(row['pctaian']),
                f(row['pctapi']),
                f(row['pct2prace']))
        data[row['name']] = d 
        for r in d:
            tally[r] = tally.get(r,0) + len(convert(r)) - 1
    except:
        print >>stderr, "Skipping", row 
print >>stderr, "Building histogram"
histogram = {}
for row in data.values():
    histogram[row] = histogram.get(row, 0) + 1 

histogram = sorted(((v, k) for (k,v) in histogram.items() if v > 1), reverse=True)
histogram = [x[1] for x in histogram]
output = "I=%r" % histogram

for x, h in enumerate(histogram):
    v = "I[%d]" % x
    internment[h] = v

letters = "abcdefghijklmnopqrstuvwxyz_ABCDEFGHJKLMOPSTUVWXYQ"
replacements = []
for x, (c, v) in enumerate(reversed(sorted((a,b) for b,a in tally.items()))):
   #  print >>stderr, x, c, v
    try:
        print "%c = %s" % (letters[x], convert(v))
    except:
        break
    replacements.append((convert(v), letters[x]))

print "from collections import namedtuple"
print "R = namedtuple('R', 'rate white black hispanic aian api multi'.split())"
print "N = None"
print "Z = 0.0"

output += ("\ndata = %r" % data).replace(' ','')
for f, t in replacements:
    output = output.replace(",%s," % f, ",%s," % t)
    output = output.replace(",%s)" % f, ",%s)" % t)
    output = output.replace("(%s," % f, "(%s," % t)
print output
for l in letters:
    print "del(%c)" % l
print "del(I)"
print "del(namedtuple)"
print "del(N)"
print "del(Z)"
