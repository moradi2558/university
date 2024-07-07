import random

def generic_list(n):
    group = []
    for i in range(n):
        list = []
        for i in range(9):
            sublist = [random.randint(0,1)for z in range (5)]
            sublist[0]=1
            for k in range(4):
                sublist[k+1] = sublist[k]*10 + sublist[k+1]
            list.append(sublist[4])
        group.append(list)
    return group

def convert(num):
    num2 = 0
    for i in str(num) :
        i = (int(i)+1 )%2
        num2 = (num2 *10) + i
    return num 

def plus (num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 = int(num1, 2)
    num2 = int(num2, 2)
    num = num1 + num2 +1
    number = bin(num).replace("0b","")
    return number[-5:]

def minus(num_1,num_2):
    num_2 = convert(num_2)
    result = int (plus(num_1,num_2))
    if result < 4000: 
        return True
    return False

def Comparison(group):
    category = []
    for i in range(50):
        k = i+1
        category.append(i)
        for k in range(i+1,50):
            x=0
            for j in range (9):
                if minus(group[i][j],group[k][j]):
                    x = x+1
            if x>4 :
                category.append(k)
        category.append("and")

    return category

n = 50
result = generic_list(n)
category = Comparison(result)
print(category)
