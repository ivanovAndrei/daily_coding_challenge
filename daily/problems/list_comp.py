import random
import time

original_list = list(random.sample(range(0, 10000000), 1000000))

start = time.time()
list_comp_query = [elem for elem in original_list if elem % 2 == 0]
end = time.time()
print(f"COmp query ran in {end - start}")

start = time.time()
length = len(list_comp_query)
end = time.time()

print(f"Found {length} elements in {end - start}")

start = time.time()
real_list = []
for i in original_list:
    if i % 2 == 0:
        real_list.append(i)
end = time.time()

print(f"Real list ran in {end - start}")

start = time.time()
real_len = len(real_list)
end = time.time()

print(f"Found {real_len} elements in {end - start}")
