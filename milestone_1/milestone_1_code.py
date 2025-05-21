import json, os
from datetime import datetime

# Loads an object from a file containing json.
def loadJsonFromFile(fileName: str) -> object:
    with open(fileName, "r") as f:
        return json.loads(f.read())

# Saves an object to a file as json.
def saveJsonFromObject(fileName: str, obj: object) -> None:
    with open(fileName, "w") as f:
        f.write(json.dumps(obj))

# Ask for the user's name and return it.
def askForName() -> str:
    return input("What is your name?: ")

# Ask for the users's birthday, convert to a UNIX timestamp and return it.
def askForBirthday() -> int:
    while True:
        dateStr = input("What date is your birthday? (dd/mm/yyyy): ")
        try:
            return int(datetime.strptime(dateStr, "%d/%m/%Y").timestamp())
        except ValueError:
            print("Invalid date. Please enter a valid date in the format dd/mm/yyyy.")

# Check userdata and fix any issues.
def checkAndFixUserdata(userdata: object) -> object:
    if not ("name" in userdata): userdata["name"] = askForName()
    if not ("birthdayTimestamp" in userdata): userdata["birthdayTimestamp"] = askForBirthday()
    return userdata


# Get the next birthday for a given birthday timestamp.
def getNextBirthday(birthdayTimestamp: int) -> int:
    birthday = datetime.fromtimestamp(birthdayTimestamp)
    now = datetime.now()
    nextBirthday = birthday.replace(year=now.year)
    if nextBirthday < now:
        nextBirthday = nextBirthday.replace(year=now.year + 1)
    return int(nextBirthday.timestamp())

def main():
    userdata = {}
    if os.path.exists("userdata.json"):
        userdata = loadJsonFromFile("userdata.json")
    userdata = checkAndFixUserdata(userdata)

    daysToNextBirthday = (datetime.fromtimestamp(getNextBirthday(userdata["birthdayTimestamp"])) - datetime.now()).days

    print(f"Hello {userdata["name"]}, your birthday is in {daysToNextBirthday} days.")

    saveJsonFromObject("userdata.json", userdata)

# Execute only if the script in run directly and not imported as a module to another script.
if __name__ == "__main__":
    main()