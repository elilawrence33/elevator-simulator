from elevator import Elevator

def convertIntOrStr(input_value): 
    try: 
        return int(input_value)
    except: 
        return input_value

def main():
    # Initializing
    floors = 20

    try: 
        floors = int(input("\n\nType a number (integer) for the floors in your building (between 2 to 50):\n\n>>> "))
    except: 
        print("Invalid floor number. Setting floors to:", floors)
        input("\nPress any key to continue... ")

    elevator = Elevator(floors)
    elevator.clear()

    while True:
        inp = input("\nEnter a floor number or type 'help' for more commands: (type 'exit' to leave)\n\n>>> ")
        inp = convertIntOrStr(inp)
        if (isinstance(inp, str)): 
        
            if (inp.lower().strip() == "exit"): 
                break
            if (inp.lower().strip() == "help"): 
                print("Extra commands:", elevator.getButtons())
                continue
     
        elevator.buttonHandler(inp)

# Entry point
main()