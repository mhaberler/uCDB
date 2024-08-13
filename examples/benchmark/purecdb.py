import cdblib
with open('bench.cdb', 'rb') as f:
    data = f.read()
reader = cdblib.Reader(data)
for key, value in reader.iteritems():
    print('+{},{}:{}->{}'.format(len(key), len(value), key, value))