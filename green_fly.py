import math

def calculateParents(day):
    f = math.floor((day - 1)/7)
    if(day <= 7):
        return 1
    else:
        return calculateParents( 7 * f) + (math.pow(8, f) * (day - (7*f)))

def calculateOffsprings(day):
    return calculateParents(day) * 8

def calculateTotal(day):
    totalParents = calculateParents(day)
    matureOffsprings = 0
    immatureOffsprings = 0
    for i in range(1,day+1):
        if( i > 7):
            matureOffsprings += calculateOffsprings( i - 7)
        immatureOffsprings += calculateParents(i) * 8

    cummulativeOffsprings = immatureOffsprings - matureOffsprings
    totalGreenflies = cummulativeOffsprings + totalParents
    return totalGreenflies

if __name__ == "__main__" :
    day = int(input("Enter the day number: "))
    print("Number of parents at day {0}: {1}".format(day, calculateParents(day)))
    print("Offsprings produced at day {0}: {1}".format(day, calculateOffsprings(day)))
    print("Total greenflies at day {0}: {1}".format(day, calculateTotal(day)))
