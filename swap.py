def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("The swapped numbers are: a=", a, "b=", b)
swap(1,5)

def swap0(a,b):
    a = (a&b) + (a | b)
    b = a + ~b + 1 
    a= a+ ~b + 1
    print("The swapped numbers are:a= ",a,"b=", b )
swap0(1,5)


