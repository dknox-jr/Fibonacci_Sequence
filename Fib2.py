nums = [1, 1]
for i in range(int(raw_input(">>> "))-2):
    nums.append(nums[-2]+nums[-1])
print nums