import time
import animation
from os import system, name

class Elevator:
    # variables 
    TIME_BTW_FLOORS = 1.5 # in seconds
    TIME_TO_MV_DOORS = 2.5 # in seconds
    OPEN = "open"
    CLOSE = "close"
    ALARM = "alarm"
    clock = ['-','\\','|','/']
    isOpen = True

    # Constructor
    def __init__(self, floors):
        if (floors > 1 and floors <= 50): 
            self.floors = floors
        else: 
            input("Invalid Entry. Setting floors to 20\n\nPress any key to continue...")
            self.floors = 20 
        self.currentFloor = 1

    # Clear the terminal
    def clear(self):
        # For Windows OS
        if name == 'nt': 
            _ = system('cls')
        # For Mac or Linux OS
        else: 
            _ = system('clear')

    def getButtons(self): 
        return "\n\tTo open doors enter: " + self.OPEN + ",\n\tto close doors enter: " + self.CLOSE + ",\n\tto trigger alarm enter: " + self.ALARM 

    def buttonHandler(self, button):
        self.clear()
        if (isinstance(button, int)):
            if (button > 0 and button <= self.floors): 
                print("You pressed %d" % (button))
                self.moveElevator(button)
            else: 
                print("Invalid Entry. Pick a floor between 1 and", self.floors)
                input("\nPress any key to continue...")
        elif (isinstance(button, str)):
            button = button.lower().strip()
            if (button == self.OPEN): self.openDoors()
            elif (button == self.CLOSE): self.closeDoors()
            elif (button == self.ALARM): self.fireAlarm()
            else: input("Invalid Entry.\n\nPress any key to continue...")
        else: 
            input("Invalid Entry.\n\nPress any key to continue...")

    # Decorator
    @animation.wait(clock, color="blue")
    def moveElevator(self, selectedFloor):
        if (self.currentFloor < selectedFloor):
            self.closeDoors() 
            print("Going up!")
            time.sleep(selectedFloor * self.TIME_BTW_FLOORS)
            print("You have arrived at floor %d" % selectedFloor)
            self.openDoors()
            self.currentFloor = selectedFloor

        elif (self.currentFloor > selectedFloor): 
            self.closeDoors()
            print("Going down!")
            time.sleep(selectedFloor * self.TIME_BTW_FLOORS)
            print("You have arrived at floor %d" % selectedFloor)
            self.openDoors()
            self.currentFloor = selectedFloor

        elif (self.currentFloor == selectedFloor):
            print("You are already on this floor")

    def openDoors(self): 
        if not (self.isOpen): 
            print("Opening doors.")
            time.sleep(self.TIME_TO_MV_DOORS)
            self.isOpen = True
        else: 
            print("The doors are open.")

    def closeDoors(self): 
        if (self.isOpen):
            print("Closing doors.")
            time.sleep(self.TIME_TO_MV_DOORS) 
            self.isOpen = False
        else: 
            print("The doors are closed.")

    def fireAlarm(self): 
        print("The alarm has been triggered.")