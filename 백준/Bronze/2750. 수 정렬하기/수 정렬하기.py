N = int(input())
array = []
for k in range(N) :
    array.append(int(input()))

for j in range (1, N) :
    for i in range (N-j) :
        if array[i] > array[i+1] :
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
for i in range(N) :
    print(array[i])