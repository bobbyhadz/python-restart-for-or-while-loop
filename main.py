# How to restart a Loop in Python

import random

num = 1

a_list = []

while num < 5:
    if random.uniform(0, 1) > 0.5:

        num += 1
        a_list.append(num)
    else:
        a_list.append(num)
        num = 1

# 👇️ [1, 1, 2, 2, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 4, 5]
print(a_list)

# 👇️ 5
print(num)