def min_cost(runners_position, ranges):
    # naive solution
    moves = 0
    i = 0
    while i < len(ranges):
        if runners_position < ranges[i][0]:
            moves += ranges[i][0] - runners_position
            runners_position = ranges[i][0]
            if not check(runners_position, ranges, i): return -1
            
        elif runners_position > ranges[i][1]:
            moves += ranges[i][1] - runners_position
            runners_position = ranges[i][1]
            if not check(runners_position, ranges, i): return -1
        
        i += 1
        
    return moves
        
    
def check(runners_position, ranges, n):
    for i in range(n):
        if runners_position < ranges[i][0] or runners_position > ranges[i][1]: return False
    return True

if __name__ == "__main__":
    n, runners_position = map(int, input().split())
    ranges = [sorted([int(x) for x in input().split()]) for _ in range(n)]
    print (min_cost(runners_position, ranges))
    