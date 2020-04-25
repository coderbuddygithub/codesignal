def checkPalindromeS1(inputString):
   if list(inputString) == list(reversed(inputString)):
      return True
   else:
      return False


def checkPalindromeS2(inputString):
    return inputString == inputString[::-1]


checkPalindromeS3 = lambda s: s[::-1] == s