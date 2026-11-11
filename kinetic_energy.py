#Jeffrey almendarez
#CMP131
#Week-09-Lab-01




def main(): #Making our own function and getting the input cfrom the user.
    m=float(input(" Enter the object's mass:"))
    v=float(input("Enter the object's velocity:"))
    ke = kinetic_energy(m, v) #We are calling our ke function here to== get the calculation of the mass times the velocity
    print(f"The object's kinetic energy is {ke:.2f}")

def kinetic_energy(mass, velocity): #Defining our arguments and getting our return value back
    return 0.5* mass* velocity**2

main() #calling our function
