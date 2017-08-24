l = ['magical unicorns',19,'hello',98.98,'world']
strings = []
nums = []
c = 0



for i in l:
    if isinstance(i,str):
        strings.append(i)
print "String:", strings

for i in l:
    if isinstance (i, (int, float)):
        nums.append(i)
print "Sum: ", sum(nums)
    