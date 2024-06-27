row = int(input("Row:\n"))
column = int(input("Column:\n"))

for _ in range(row):
    for _ in range(1, column + 1):
        print("#", end=" ")
    print()    
    
