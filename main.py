# A simple calculator on the terminal...
# I'm getting started to code...
# Thank you for download or utilisation in program or watch...
print("Thank you for download or utilisation in program or watch...")

print("Program made by TidyCodeur, if you want to know TidyCodeur's projects, search on github TidyCodeur...")

# Inform to program start
print("Program start...")

# Establish an array that contains the numbers from 0 to 9, in the form of a string.
stringNumberArray = []
for h in range(0, 10):
  stringNumberArray += str(h)

# Initialize an array that contains all valid characters/numbers/words.
allValid = stringNumberArray + [".", "*", "-", "+", "/", "modulo"]

# Print the valid characters/numbers/words.
print("The valid characters/numbers/words is " + ", ".join(["* (for multiplication)", "/ (for division)", "mudulo (no need to traduct you if you are learned python programming, i thing so, else if you don't know, modulo is the rest of a division)", "+", "-"] + stringNumberArray + [". (the comma)"]) + "...")

def checkOperationSyntax(theEntranceZ):
  return False

def tidyOneIn(tidyArrayA, tidyArrayB):
  if tidyArrayA != [] or len(tidyArrayA) == 1:
    for e in tidyArrayA:
      for eb in tidyArrayB:
        if e == eb:
          return False
  elif len(tidyArrayA) == 1:
    for ed in tidyArrayB:
      if ed == tidyArrayA[0]:
        return False
    return True
  elif tidyArrayA == []:
    return True
def checkChars(theEntranceZ, validCharsZ, validWordsZ):
  localisationLetter = 0
  reservedPlaces = []
  for i in theEntranceZ:
    localisationWord = 0
    for b in validWordsZ:
      if len(b) <= len(theEntranceZ[localisationLetter:]):
        if theEntranceZ[localisationLetter:localisationLetter+len(b)] == b and tidyOneIn(reservedPlaces, [range(localisationLetter, localisationLetter+len(b)+1)]):
          reservedPlaces += [range(localisationLetter, localisationLetter+len(b)+1)]
      localisationWord += 1
    localisationLetter += 1
  localisationLetter = 0
  for ib in theEntranceZ:
    for z in validCharsZ:
      if z == ib and localisationLetter not in reservedPlaces:
        reservedPlaces += [localisationLetter]
  localisationLetter += 1
  if len(reservedPlaces) == len(theEntranceZ):
    return True
  else:
    return False

# Initialize function checkChars for check if a string/array/tuple... contains only characters/words/numbers... of a Array/String/tuple...
def checkCharsAndSyntax(theEntrance, validChars, validWords):
  if checkChars(theEntrance, validChars, validWords):
    print("You are enter valids chars/words/numbers...")
    if checkOperationSyntax(theEntrance):
      print("The syntax of your operation is valid...")
      return True
  print("The syntax of the operation it's not valid, and the entrance contains other only valid chars...")
  return False
# Entrance for operation...
entrance = input()
# Check if the operation entrance is valid or not, if not valid, recommence to ask entrance...
while entrance.replace(" ", "") == "" or not checkCharsAndSyntax(entrance.replace(" ", ""), allValid[:-1], [allValid[-1]]):
  print("Please enter valid operation...")
  entrance = input()

# After Check, doing the operation with eval function...
print(entrance + " = " + str(eval(entrance.replace("modulo", "%").replace(" ", ""))))

