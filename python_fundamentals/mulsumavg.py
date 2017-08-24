#Print odd numbers from 1 to 1000
for odd in range(1, 1000):
    if odd%2 != 0:
        print odd

for mult in range(5, 1000000 ):
    if mult%5 == 0:
        print mult

a = [1, 2, 5, 10, 255, 3]
print sum(a)
print sum(a)/2