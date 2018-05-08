def parents_at_day_n(n):
    if n <= 7:
        return 1
    return parents_at_day_n(n-1) + offsprings_at_day_n(n-7)

def offsprings_at_day_n(n):
    return parents_at_day_n(n) * 8

def population_at_day_n(n):
    total = 0
    for i in range(1, n+1):
        total += offsprings_at_day_n(i)
    return total + 1 #add initial parent

if __name__ == "__main__":
    print("Day\t\tParents\t\tOffsprings\t\tTotal")
    for i in range(1, 29):
        print("{0}\t\t{1}\t\t{2}\t\t{3}".format(i, parents_at_day_n(i), offsprings_at_day_n(i), population_at_day_n(i)))
