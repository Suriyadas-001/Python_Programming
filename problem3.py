# SOUVIK MANNA

# 3. From nums = [10, 25, 37, 40, 55], use filter() with a lambda to get only numbers divisible by 5.

nums = [10, 25, 37, 40, 55]

result = list(filter(lambda x: x % 5 == 0, nums))

print(result)
