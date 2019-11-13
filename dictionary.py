nums = [1, 5, 3, 0, 8, 4, 7, 4, 7, 4]
thisdict = {1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
            }
for key in reversed(list(thisdict.keys())):
    print(thisdict[key])
print(thisdict)