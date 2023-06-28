row_num = int(input("Enter a number of rows: "))
col_num = int(input("Enter a number of columns: "))
list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        list[row][col]= row*col

print(list)
