#Jeffrey Almendarez
#CMP131
#WEEK9
#Lab01
#Celsius_temperature_table.py

def celsius(f): # our function making fahrenheit to celsius
    c= 5/9 * (f - 32)
    return c

def main():
    print( "Fahrenheit Celsius") #Getting the name of our header
    for f in range(21): #looping through 1-20
        print(f, "F =", round (celsius(f), 1), "C")
        

main()

