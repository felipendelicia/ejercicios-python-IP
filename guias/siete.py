# ejercicio 1) 1
def isIn(list:[int], element:int)->bool:
    for i in list:
        if i == element: return True
    return False

# ejercicio 1) 2
def divideAll(list:[int], element:int)->bool:
    for i in list:
        rest:int = i % element
        if rest != 0: return False
    return True

# ejercicio 1) 3
def sumAll(list:[int])->int:
    result:int = 0
    for i in list:
        result += i
    return result

# ejercicio 1) 4
def isOrdered(list:[int])->bool:
    prevValue:int = None;
    for i in list:
        if prevValue:
            if i < prevValue: return False
        prevValue = i
    return True

# ejercicio 1) 5
def isWordMoreLongThan7(list:[str])->bool:
    for i in list:
        if len(i) >= 7: return True
    return False

# ejercicio 1) 6
def isPalindrome(word:str)->bool:
    reversedWord:str = ""
    for i in word:
        reversedWord = i + reversedWord
    return reversedWord == word

