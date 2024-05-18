def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    
    candies = [1] * n
    
    # Left to Right Pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to Left Pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

# Example usage:
ratings = [1,0,2]
print(candy(ratings))
ratings = [1,2,2]
print(candy(ratings))
ratings = [4,2,3,3,3,3,4,5,4]
print(candy(ratings))