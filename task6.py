a=[1, 2, 3, 4, 5, 6]
b=[5, 6, 7, 8]
c=[6, 9, 5, 7]
d=len(a)
e=len(b)
f=len(c)

for i in range(d,e,f):
    if d!=e and e!=f and f!=d:
        g=d[i] + e[i] + f[i]
        print(g)
    

