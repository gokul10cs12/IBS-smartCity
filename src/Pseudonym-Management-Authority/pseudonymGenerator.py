import random
import string


class PseudonymGenerator:
    @staticmethod
    def generatePseudonym():
        letters = string.ascii_letters
        resultStr = ''.join(random.choice(letters) for i in range(28))
        print("Random string is:", resultStr)
        return resultStr
