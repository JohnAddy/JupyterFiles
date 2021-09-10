import random


# John Adekunle

def check():
    u = input("Pick Your Choice between Rock = r , Paper = p , Scissors = s:  ").lower() # Getting input and changing to lower
    lists = {"r": "Rock", "p": "Paper", "s": "Scissors"} # key/value data stored as a dictionary
    keys = list(lists.keys()) # getting the keys in a list
    if u in lists:
        print("\nYou choose " + lists[u] + "\n") # print my choice
        c = random.choice(keys)
        print("Computer choose " + lists[c]) # print computer's random choice

        if u == "r" and c == "s":
            return "You Won!"
        elif u == "s" and c == "r":
            return "You lost"

        elif u == "s" and c == "p":
            return "You Won!"
        elif u == "p" and c == "s":
            return "You lost"

        elif u == "p" and c == "r":
            return "You Won!"
        elif u == "r" and c == "p":
            return "You lost"
        else:
            return check() # returning the function
