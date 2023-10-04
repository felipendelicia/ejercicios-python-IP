import math


# ejercicio 1) 1
def printHelloWorld():
    print("Hola mundo!")


# ejercicio 1) 2
def printVerse():
    print(
        "Este espejo da una imagen exquisita\nEsos pibes son como bombas pequeñitas\nEl peor camino a la cueva del perico\nPara pibes que no duermen por la noche"
    )


# ejercicio 1) 3
def sqrtOfTwo() -> float:
    return round(math.sqrt(2), 4)


# ejercicio 1) 4
def factorialOfTwo() -> int:
    return math.factorial(2)


# ejercicio 1) 5
def perimeter() -> float:
    return math.pi * 2


# ejercicio 2) 1
def personalizedGreeting(name: str):
    print("Hello", name)


# ejercicio 2) 2
def squareRoot(number: float) -> float:
    return math.sqrt(number)


# ejercicio 2) 3
def farenheitToCelcius(farenheit: float) -> float:
    return (farenheit - 32) * (5 / 9)


# ejercicio 2) 4
def isMultiple(divisor: int, dividend: int) -> bool:
    return dividend % divisor == 0


# ejercicio 2) 5
def printChorusTwoTimes():
    print(
        "Este espejo da una imagen exquisita\nEsos pibes son como bombas pequeñitas\nEl peor camino a la cueva del perico\nPara pibes que no duermen por la noche\n"
        * 2
    )


# ejercicio 2) 6
def isPair(number: int) -> bool:
    return isMultiple(2, number)


# ejercicio 2) 7
def minQuantityOfPizzas(clients: int, minPizzasPerClient: int):
    return math.ceil((clients * minPizzasPerClient) / 8)


# ejercicio 3) 1
def isThereOneZero(number1: float, number2: float) -> bool:
    return number1 == 0 or number2 == 0


# ejercicio 3) 2
def areThereZero(number1: float, number2: float) -> bool:
    return number1 == 0 and number2 == 0


# ejercicio 3) 3
def isLongName(name: str) -> bool:
    return 3 <= len(name) <= 8


# ejercicio 3) 4
def isLeapYear(year: int) -> bool:
    isMultipleOf400 = isMultiple(400, year)
    isNotMultipleOf100 = not isMultiple(100, year)
    isMultipleOf4 = isMultipleOf4(4, year)
    return isMultipleOf400 or (isNotMultipleOf100 and isMultipleOf4)


# ejercicio 4) 1
def pineWeight(pineHeight: float) -> float:  # altura en metros
    if pineHeight > 3:
        return 3 * 300 + (pineHeight - 3) * 200
    else:
        return 300 * pineHeight


# ejercicio 4) 2
def isUtilWeight(pineWeight: float) -> bool:  # peso en kilos
    return 400 <= pineWeight <= 1000


# ejercicio 4) 3 && ejercicio 4) 4
def isUtilPine(pineHeight: float) -> bool:
    return isUtilWeight(pineWeight(pineWeight))


# ejercicio 5) 1
def doubleOfPairNumber(number: int) -> int:
    if isPair(number):
        return 2 * number
    return number


# ejercicio 5) 2
def returnNearestPairNumber(number: int) -> int:
    if isPair(number):
        return number
    return number + 1


# ejercicio 5) 3
def returnDoubleOfThreeMultiplesAndTripleOfNineMultiples(number: int) -> int:
    if isMultiple(9, number):
        return 3 * number
    elif isMultiple(3, number):
        return 2 * number
    return number


# ejercicio 5) 4
def beautifulName(name: str):
    if len(name) >= 5:
        print("Tenes un nombre con muchas letras")
    else:
        print("Tenes un nombre con pocas letras")


# ejercicio 5) 5
def rangeOfNumber(number: float):
    if number > 20:
        print("Mayor que 20")
    elif number >= 10:
        print("Entre 20 y 10")
    elif number < 5:
        print("Es menor que 5")


# ejercicio 5) 6
def printIsAbleToWork(gender: str, age: int):
    if age < 18:
        print("Anda a estudiar, vago")
    if gender == "F" and age >= 60:
        print("Jubilada")
    elif gender == "M" and age >= 65:
        print("Jubilado")
    else:
        print("Anda a laburar, bobo")


# ejercicio 6) 1
def printNumbersFromOneToTen():
    i = 1
    while i <= 10:
        print(i)
        i += 1


# ejercicio 6) 2
def printPairNumbersFromTenToForty():
    i = 10
    while i <= 40:
        print(i)
        i += 2


# ejercicio 6) 3
def printEcoTenTimes():
    i = 1
    while i <= 10:
        print("Eco!")
        i += 1


# ejercicio 6) 4
def countDown(_from: int):
    i = _from
    while i > 0:
        print(i)
        i -= 1
    else:
        print("Despegue!")


# ejercicio 6) 5
def timeJourney(_from: int, at: int):
    i = _from
    while i >= at:
        print("Viajo un año al pasado, estoy en el año", i)
        i -= 1


# ejercicio 7) 1
def printNumbersFromOneToTenFor():
    for i in range(10):
        print(i + 1)


# ejercicio 7) 2
def printPairNumbersFromTenToFortyFor():
    for i in range(10, 41, 2):
        print(i)


# ejercicio 7) 3
def printEcoTenTimesFor():
    for i in range(10):
        print("Eco!")


# ejercicio 7) 4
def countDownFor(_from: int):
    for i in range(_from, 0, -1):
        print(i)
    else:
        print("Despegue!")


# ejercicio 7) 5
def timeJourneyFor(_from: int, at: int):
    for i in range(_from, at, -1):
        print("Viajo un año al pasado, estoy en el año", i)
