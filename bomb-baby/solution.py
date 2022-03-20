def solution(x, y):
    ans = solve([long(x), long(y)], 0)
    if ans == 0:
        return 'impossible'
    else:
        return str(ans)
    
def solve(bomb, gen):
    while bomb[0] > 0 and bomb[1] > 0 and bomb[0] != bomb[1]:
        if (bomb[0] > bomb[1]):
            max = bomb[0]
            min = bomb[1]
        else:
            max = bomb[1]
            min = bomb[0]
        if ((max - min) % min == 0 and min != 1):
                return 0
        if ((max - min) % min == 0 and min == 1):
            return gen + max - 1
        else:
            multiplier = (max - min) // min + 1
            return solve([max - (min * multiplier), min], gen + multiplier)
    return 0