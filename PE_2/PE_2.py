def pe2(limit:int) -> int:

    term_a=1
    term_b=2
    sum = 0
    for (term_a < limit) & (term_b < limit):
        if term_a % 2 == 0:
            sum += term_a
        term_a = term_a + term_b
        if term_b % 2 == 0:
            sum += term_b
        term_b = term_a + term_b



    return sum