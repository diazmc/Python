def draw_stars(a, b):
    c = []
    
    for i in a:
        i *= b
        c.append(i)

    return c

a = [4, 6, 1, 3, 5, 7, 25]
for i in draw_stars(a, '*'):
    print i


def draw(a, b):

    c = []

    for i in a:
        i *= b
        c.append(i)

    return c 

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
for i in draw_stars(x, '*'):
    if type(i) == str: print i 

    elif type(i) == int: print x[i][0]