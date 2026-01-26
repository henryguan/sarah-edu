import math

# Question 4c
val_2_years = 1500 * (0.95)**24
print(f"Value after 2 years: {val_2_years}")

# Question 4d
# 1500 * (0.95)^m < 900
# 0.95^m < 0.6
# m * log(0.95) < log(0.6)
m = math.log(0.6) / math.log(0.95)
print(f"Exact m for 900: {m}")

# verification
print(f"Value at month {math.floor(m)}: {1500 * 0.95**math.floor(m)}")
print(f"Value at month {math.ceil(m)}: {1500 * 0.95**math.ceil(m)}")
