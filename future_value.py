def futureValue(present , rate , months):
    future = present * (1 + rate) ** months
    return future    #performing our calculations

def main(): #Defining our function and storing it in and getting the user input
    present= float(input("Enter the account present balance: "))
    rate= float(input("Enter the monthly interest rate (0.01 for 1%): ")) 
    months= int(input("Enter the months: "))

    result= futureValue(present, rate, months) #Getting our result after getting our return value.
    print("The account future value turns out to be $" , round(result , 2)) 

main()