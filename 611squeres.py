import math

N = 10**12

def judgeSquareSum(c):
    for i in range(2, math.sqrt(c)+1):
        int count = 0
        if (c % i == 0) {
            while (c % i == 0) {
                count++;
                c /= i;
            }
            if (i % 4 == 3 && count % 2 != 0)
                return false;
        }
    }
    return c % 4 != 3;
}

squares = [n*n for n in range(1, int(math.sqrt(N))+1)]
print(len(squares), "squares")
doors = [False] * (N+1)
for i, s in enumerate(squares):
    if i%100 == 0:
        print(i)
    for n in squares[i + 1:]:
        if s+n > N:
            break
        doors[s+n] = not doors[s+n]

print(doors)
print(sum(doors))
