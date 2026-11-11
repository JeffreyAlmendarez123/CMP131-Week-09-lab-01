def celsius(f):
    c= 5/9 * (f - 32)
    return c

def main():
    print( "Fahrenheit, Celsius")
    for f in range(21):
        print(f, "F =", celsius(f), "C"))

main()

