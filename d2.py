def triange(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")

        print()


def filterAndPrint(lis):
    for i in lis:

        if i > 500:
            break
        if i > 150:
            continue
        if i%5==0:
            print(i)

def appendStringInMiddle(s1,s2):
    mid = int(len(s1)/2)
    s3 = s1[0:mid]+s2+s1[mid:]
    return s3

# list comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]


def loweralphabetcomefirst(str):
    loweral = "".join(char for char in str if char.islower())
    upperal = "".join(char for char in str if char.isupper())
    result_str = loweral+upperal
    return result_str

def concatTwoList(li1,li2):
    li = []
    for i in range(len(li1)):
        li.append(li1[i]+li2[i])
    return li


def concatelist(l1,l2):
    li = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            li.append(l1[i]+l2[j])

    return li

def makeDict(li,di):
    result_dic = {}
    for i in li:
        result_dic[i] = di
    return result_dic


def create_new_dic(dic):
    new_dic = {}
    for i in dic.keys():
        if i == "name" or i == "salary":
            new_dic[i] = dic.get(i)
    return new_dic

def modify_tuple(t):

        t[1][0] = 222
        for i in t:
            print(i)








