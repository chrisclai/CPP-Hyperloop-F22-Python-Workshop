'''
The CPP Hyperloop Pod reaches a futuristic junction and has four things to do:
[Turn Left, Turn Right, Go Straight, Stop Moving]

The pod has an on-board camera that is able to detect a color on the sign and proceed according to the following constraints:
If the color on the sign is orange or purple, turn left.
If the color on the sign is yellow or brown, turn right.
If the color on the sign is green or blue, go straight.
If the color on the sign is any other color not mentioned, stop moving.

Write a series of conditional statements that tells the car what to do given the color on the sign, which is user-defined.
'''

def main():
    color = ""
    direction = ""
    validInput = False
    validColors = ["orange", "purple", "yellow", "brown", "green", "blue", "red", "black"]

    # If the user does not enter in a color that is in the list, it will ask them to do it again
    while not validInput:
        color = input("Enter in a color: ")
        if color in validColors:
            validInput = True
        else:
            print("Sorry, this color is not in the list! Try Again!")

    # At this point, color contains the direction that pod needs to go
    if color == "orange" or color == "purple":
        direction = "left"
    elif color == "yellow" or color == "brown":
        direction = "right"
    elif color == "green" or color == "blue":
        direction = "straight"
    else:
        direction = "stop moving"

    # print(f"The direction that the Hyperloop Pod will move in is {direction}")
    print("The direction that the Hyperloop Pod will move in is " + direction)

    number = 6
    print("Test print number: " + str(number))

if __name__ == "__main__":
    main()