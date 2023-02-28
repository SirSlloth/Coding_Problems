

def pe2(limit:int) -> int:
    print(limit)
    print(type(limit))
    term_a=1
    term_b=2
    sum = 0
    while (term_a < limit) & (term_b < limit):
        if term_a % 2 == 0:
            sum += term_a
        term_a = term_a + term_b
        if term_b % 2 == 0:
            sum += term_b
        term_b = term_a + term_b
    return sum

def optomizedPE2(limit:int) -> int:
    pass
    return sum



if __name__ == "__main__":
    solution = pe2(limit=4_000_000)
    print(solution)
    #solution_optimized = optomizedPE2()
    #print(solution_optimized)
