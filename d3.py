def tuple_unpacking(lis):
    for i in lis:
        [a, b] = i
        print(a + " is " + str(b) + " years old")


def add_manupulation(dic,name,age):

    dic[name] = age
    return dic


def update_manupulation(dic, name, age):
    dic[name] = age
    return dic

def delete_manupulation(dic, name):
   del dic[name]
   return dic


def two_sum_problem(li,k):
    dic = {}
    result = []
    for i in range(len(li)):
        is_avail = dic.get(k-li[i],-1)
        if is_avail == -1:
            dic[li[i]] = i
        else:
            result.append(dic.get(k-li[i]))
            result.append(i)
            break

    return result


def checkPalin(str):
    res = ""
    for i in range(len(str)-1,-1,-1):
        res = res + str[i]

    return res == str

# print(checkPalin("madam"))

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[min_index]:
                min_index = j

#         swap with the first ele
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp


def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)


file_name = "data.txt"

with open(file_name,'w') as file:
    file.write("Hello World")



with open(file_name,'r') as file:
    data = file.read()


li = data.split(" ")
print(li)

out = "output.txt"
try:
    with open(out, 'w') as file:
        file.write("Number of words : " + str(len(li)))
except  FileNotFoundError:
    print(f"File not found named {out}")




def checkError(numerator,denominator):
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of {numerator} / {denominator} is {result}.")
    finally:
        print("Exception handling completed.")


from queue import LifoQueue


class Stack:

    def __init__(self):
        self.stack = LifoQueue()

    def push(self, item):
        self.stack.put(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.get()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack.queue[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return self.stack.empty()

    def size(self):
        return self.stack.qsize()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())