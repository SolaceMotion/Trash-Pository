import sys

randomList = [2j, 0, 4]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[1], "occurred.")
        print("Next entry.")
        print("") # line break
print("The reciprocal of", entry, "is", r)
