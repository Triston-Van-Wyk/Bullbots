from statistics import mean
min=0
max=101
print(f'The average of a list from "{min}" to "{max}" is "{mean(range(min,max+1))}"')
mylist = range(min, max)
# averagelist = []
# for i in range(min,max-10):
#     meantemp=mean(mylist[i:i+11])
#     averagelist.append(meantemp)
#
# print(averagelist)