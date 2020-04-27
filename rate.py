# rate=0.0137
# q=1+rate
# a=100
# c0=100
# c1=c0 + c0*rate + a
# c2=c1 + c1*rate + a
#
# c12=(q**11-1)/(q-1)*(c2-c1) + c1

rate = 0.1644/366
pace = [45, 21, 28, 37, 44, 9, 54, 7, 32, 30, 34, 25]
c0 = 0
d = 0
for i in pace:
  c0 = c0 + c0 * i * rate + 100
  d = d + i
print(c0)


rate = 0.1644/366
s = [366]
d = 0
for i in pace:
    d = d + i
    s.append(366-d)
s.remove(0)
print(s)

c = 0
for t in s:
    each = 100*((1 + rate)**(t - 2))
    print(each)
    c = c + each
print(c)


