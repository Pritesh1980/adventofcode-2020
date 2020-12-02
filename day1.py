
with open('data1.txt') as f:
    data = [ int(i) for i in f ]

data = sorted(data)
# print(data)

def matchDiff(target):
    for x in data:
        diff = target - x
        if diff in data:
            return [x,diff]
    return [0,0]

# Exercise 1
num1 ,num2 = matchDiff(2020)
print(f"{num1} + {num2} = 2020")
print(f"{num1} * {num2} = {num1 *num2}\n")

# Exercise 2
for x in data:
    diff = 2020 - x
    num1,num2 = matchDiff(diff)
    if num1:
        print(f"{num1} + {num2} + {x} = {num1+num2+x}")
        print(f"{num1} * {num2} * {x} = {num1*num2*x}")
        break;