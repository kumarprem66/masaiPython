# 1
print("Hello World")

# integer
i = 10
print(i)
print(type(i))

s = "prem kumar"
print(s)
print(type(s))

b = True
print(b)
print(type(b))

f = 10.4
print(f)
print(type(f))

li = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
print(li)
print(type(li))

tup = ("prem", "kumar", "software", "developer")
print(tup)
print(type(tup))

dic = {"fname": "prem", "lname": "kumar", "age": 21}
print(dic)
print(type(dic))


def createNumber(n):
    li = []
    for i in range(1,n):
        li.append(i)
    li.append(23)
    li.remove(4)
    sorted(li)
    return li


# reverse a number
def reverseString(str):
    bag = ""
    for i in range(len(str)-1,-1,-1):
        bag = bag + str[i]
    return bag


def countVowels(str):
    count = 0;
    for i in range(len(str)):
        if str[i].lower() == 'a' or str[i].lower() == 'e' or str[i].lower() == 'i' or str[i].lower() == 'o' or str[i].lower() == 'u':
            count = count+1
    return count


def checkPrime(n):
    flag = True
    for i in range(2,n):
        if n%i==0:
            flag = False

    return flag

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac
print(factorial(5))





