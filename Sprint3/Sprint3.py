import random
import string
import secrets

class RandomPassword:

    def __init__(self, Name, Surname, Username):
        self.Name = Name
        self.Surname = Surname
        self.Username = Username

    def generatePassword(self):
        
        passLetters = ""

        randomLettersLC = string.ascii_lowercase
        randomLettersUC = string.ascii_uppercase
    
        for x in range(2):
            passLetters = str(passLetters) + random.choice(randomLettersLC)

        for x in range(2):
            passLetters = str(passLetters) + random.choice(randomLettersUC)

        passNumbers = ""

        randomNumbers = string.digits
    
        for x in range(6):
            passNumbers = str(passNumbers) + secrets.choice(randomNumbers)

        passSymbols = "@!"

        passwordString = str(passLetters) + str(passNumbers) + str(passSymbols)

        password = ''.join(random.sample(passwordString, len(passwordString)))

        return "{} {}, Username: {}'s Password is: {}".format(self.Name, self.Surname, self.Username, password)

user1 = RandomPassword("Mar'waan", "Koma", "MKoma38")
user2 = RandomPassword("Nathan", "Absolom", "NAbsolom1235")
user3 = RandomPassword("Shana", "Barendse", "SBarendse1011")

print(RandomPassword.generatePassword(user1))
print(RandomPassword.generatePassword(user2))
print(RandomPassword.generatePassword(user3))