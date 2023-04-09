from collections import Counter
def sol(string):
    
    counts = Counter(string)
    counts = list(counts.values())
    
    if len(set(counts)) == 1: return "YES"
    else:
        counts.sort()
        counts2 = counts[ : ]
        # 1st possibility____________________________
        counts[-1] -= 1
        if counts[-1] == 0:
            counts.pop(0)
        if len(set(counts)) == 1: return "YES"
        # ___________________________________________
        # 2nd possibility____________________________
        counts2 [0] -= 1
        if counts2[0] == 0:
            counts2.pop(0)
        if len(set(counts2)) == 1: return "YES"
        # ___________________________________________
        return "NO"
        

if __name__ == "__main__":
    string = input()# a-z
    print (sol(string))
    