def lemonadeChange(bills: list[int]) -> bool:
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            fives -= 1
            tens += 1
        else:  # bill == 20
            if tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
        if fives < 0:
            return False
    return True


# Example test cases
print(lemonadeChange([5,5,5,10,20]))   # True
print(lemonadeChange([5,5,10,10,20])) # False
