# Code Challenge — Write a program
# In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay. More precisely, it is the time required for an element to reduce in half.

# Let's take an isotope of Radium (Ra) called radium-223. Say, its half-life is about 12 days. This means that every 12 days the number of atoms reduces in half. Write a program that calculates how many full half-life periods (in days) it would take for a certain amount of radium-223 to reduce to a specific value.

# The input format:
# The first line with the starting amount of atoms N (from 2 to 1,000,000), the second line with the resulting quantity R.

# The output format:
# The number of full half-life periods (in days) T it would take for radium-223 to reduce from N to R.

# Assume that any change would take at least 1 half-life period. 
# Suppose, the initial number of atoms is 4 and the resulting quantity equals to 3. In 12 days, 
# the number will reduce to 2 atoms. Since we are counting full half-life periods, you should write 12 and so on.

# Sample Input 1:

# 4
# 3
# Sample Output 1:

# 12

# Sample Input 2:

# 835950
# 139505
# Sample Output 2:

# 36

n = int(input())
original_n = n
r = int(input())
half_life_interval = 12
half_life_counter = 0
days_required_to_hit_target_r = 0

while(n > r):
    half_life_counter += 1
    days_required_to_hit_target_r += 1
    if half_life_counter >= half_life_interval:
        half_life_counter = 0
        n /= 2
        print(f"n is now: {n}")

print(f"It takes {days_required_to_hit_target_r} days to reduce to {r} from {original_n}")




