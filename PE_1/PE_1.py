import math

def pe1(limit:int, base_1:int, base_2:int) -> int:
    n = 1
    sum = 0
    while (base_1*n) <= limit:
        sum += base_1*n
        n+=1

    i=1
    while (base_2*i) <= limit:
        if (base_2*i)%base_1 == 0:
            i+=1
        else:
            sum += base_2*i
            i+=1

    return sum

def optomizedPE1(limit:int, base_1:int, base_2:int) -> int:
    def gaussSum(base:int, limit:int) -> int:
        n = limit // base
        a = base
        l = n * base
        return (n * (a + l)) // 2

    sum_1 = gaussSum(base=base_1, limit=limit)

    sum_2 = gaussSum(base=base_2, limit=limit)

    overlapSum = gaussSum(base=math.lcm(base_1,base_2), limit=limit)

    return (sum_1 + sum_2 - overlapSum)

if __name__=="__main__":
    solution = pe1(limit=999, base_1=3, base_2=5)
    print(solution)
    solution2 = optomizedPE1(limit=999, base_1=3, base_2=5)
    print(solution2)