#Example 1:-
sq = [i*i for i in range(6) if i%2 != 0]
    #[Output for in iterable if condition]
print(sq)

# [1, 9, 25]

#Example 2:-
nums = [-2, -4, 3, 5, 2, -1]

nums = [0 if val < 0 else val for val in nums]

print(nums)

#[0, 0, 3, 5, 2, 0]

#Example 3:-
words = ["Shree", "Saurabh", "apnacollege"]

words = [val.upper() for val in words]
print(words)

#['SHREE', 'SAURABH', 'APNACOLLEGE']

