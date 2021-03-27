def InsertionSort(list):
    for i in range(len(list)):
        value = list[i]
        k = i - 1
        while (k >= 0) and (list[k] > value):
            list[k+1] = list[k]
            k = k -1
        list[k+1] = value
    return list

def DoubleCheck(listCheck):
    for i in range(len(listCheck)):
        for k in range(len(listCheck)):
            if i != k and listCheck[i] > listCheck[k]:
                InsertionSort(listCheck)
    return True

def GetInput(Type, Position):
    UserInput = 0
    if Type == "Max":
        try:
            UserInput = eval(input("How many values do you want to sort? "))
        except NameError:
            print("Invalid input")
            return GetInput(Type, Position)
        except SyntaxError:
            print("Invalid input")
            return GetInput(Type, Position)
        
        if isinstance(UserInput, int):
            return UserInput
        else:
            print("Invalid input")
            return GetInput(Type, Position)
        
    elif Type == "Value":
        try:
            UserInput = eval(input("Please enter a value for poistion " + str(Position) + ": "))
        except NameError:
            print("Invalid input")
            return GetInput(Type, Position)
        except SyntaxError:
            print("Invalid input")
            return GetInput(Type, Position)
        
        if isinstance(UserInput, int):
            return UserInput
        else:
            print("Invalid input.")
            return GetInput(Type, Position)

def ProduceList(Max):
    list = []
    Type = "Value"
    for i in range(0, Max):
        list.append(GetInput(Type, i))
    print(list)
    return list

def main():
    Type = "Max"
    Max = GetInput(Type, None)
    UnsortedList = ProduceList(Max)
    print("Unsorted List: " + str(UnsortedList) + "\n")
    SortedList = InsertionSort(UnsortedList)
    print("Sorted List: " + str(SortedList) + "\n")

main()
        
