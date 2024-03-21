def increment(lst: list[int], position: int) -> list[int]:
    lst[position] = lst[position] + 1
    if lst[position] > 2:
        lst[position] = 0
        lst = increment(lst, position - 1)
    return lst
        
combinations = [[0,0,0,0,0]]

for i in range(3**5 - 1):
    combinations.append(increment(combinations[-1].copy(), 4))
    
f = open("dfive.txt", "r")
dictionary = f.readlines()
f.close()

for x in range(len(dictionary)):
    dictionary[x] = dictionary[x][:5]
    
