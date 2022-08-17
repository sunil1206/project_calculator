def density(m, v):
    try:

        d = m / v
        print(d)
    except:
        print('Area should not be zero')


m = int(input("mass "))
v = int(input("vol "))
density(m, v)