englishNumbers = ("One", "Two", "Three", "Four", "Five")
spanishNumbers = ("Uno", "Dos", "Tres", "Cuatro", "Cinco")

#Your task: Create a new function called zipLists() to implement you own version of the built-in zip() function.
#Your zipLists() function will need to take two lists as parameters and return a list of tuples where each tupple contains two values: one from each list.

def zipLists(list1, list2):
    list3 = []

    for i in range(len(englishNumbers)):
        testList = []

        x = list1[i]
        y = list2[i]

        testList.append(x)
        testList.append(y)

        list3.append(tuple(testList))        

    return list3


print(zipLists(englishNumbers, spanishNumbers))    








