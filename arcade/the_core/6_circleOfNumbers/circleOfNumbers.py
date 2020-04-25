def circleOfNumbers(n, firstNumber):    
    if(firstNumber < range(0,n)[n//2]):
        return n//2+firstNumber
    else:
        return abs(n//2-firstNumber)