'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

num = int(input("What is the smallest number that is evenly divisible \
by all the number from 1 to (enter value) "))

denom = []
for i in range(1, num+1):
    denom.append(i)

# start counting and go up in 'den' increment to find the number faster
count = num
cond = True
while cond == True:
    div = []
    for x in denom:
        rem = count % x
        div.append(rem)
    if sum(div) == 0:
        print(count)
        cond = False
    else:
        count = count + num