# Suriya Das

# 2. Create a list of squares of numbers from 1 to 20, but only include numbers divisible by 3.

squares = []
squares = [i**2 for i in range(1,21) if i%3==0]
print(squares)