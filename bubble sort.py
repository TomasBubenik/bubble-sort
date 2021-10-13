def bubble_sort(val):
    for i in range(len(val)):
        for x in range(len(val) - 1):
            if val[x] > val[x+1]:
                val[x],   val[x+1] = val[x+1], val[x]
val = [12,4,5,7,9]
bubble_sort(val)
print(val)
