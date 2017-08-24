def odd_even():
    for x in range(1,2001):
        if x%2 == 0:
            print "Number is", x, "This is an even number"

        if x%2 != 0:
            print "Number is", x, "This is an odd number"
odd_even()
    
newList = []
def multiply(a, b):
    for i in range(0, len(a)):
        newList.append(a[i] *b)

a = [2,4,10,16]
multiply (a, 5)
print newList

