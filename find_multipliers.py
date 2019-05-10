# find multipliers of an integer from a given list (simple logic)

A = [2,4,1,6,5,10,40]
L = len(A)
y = 0
k = 0

for i in A:
    for m in A:
        if i*m == 20:
            print(i, m)

