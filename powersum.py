def powerSum(X, N):
    
    bases = [i for i in range(1, int(X**(1/N))+1)]
    
    def count_combinations(total, index):
        
        if total == X:
            return 1
        if total > X or index == len(bases):
            return 0
        return count_combinations(total + bases[index]**N, index+1) + count_combinations(total, index+1)
    
    return count_combinations(0, 0)

print(powerSum(int(input()), int(input())))