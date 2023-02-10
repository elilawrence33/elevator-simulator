# Elevator Simulator

This is a text-based python program that simulates an elevator and the controls in which to operate it. The program was written in response to the following coding challenge: 

Provide code that simulates an elevator. You may use any language (recommend using Java or Python). 

Assumptions: 

	* The user has Python 3.0 or greater installed
	* The user will know how to use the terminal to run the python command to start the program. 
	* The user has a mouse and keyboard
	* The elevator will need to know how many floors are available so that it will know how many floors it can move to. This is requested by the user in the main.py
	* The Elevator is the only object 

Features not Implemented: 

	* No graphical buttons for the user to press
	* No audio plays when the user enters the command to ring the alarm
	* The elevator does not go back to the first floor when the alarm plays
	* When the user is specifying how many floors are in the building, they are not allowed to input anything outside the range of 2 - 50. This is because there would be no point of an elevator for a single floor building, and 50 is a decent cap so we do not allow the user to input over 1 million floors and potentially loop forever. 

