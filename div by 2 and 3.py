#PYTHON PROGRAM THAT PRINT ALL THE NUMBERS
#DIVISIBLE BY 2 AND 3 FOOR A GIVEN NUMBER
#RESULT FUNCTION WITH N

for i in range(2,21):
    if i%2==0:
        print(i, '\t' 'div by 2')
    elif i%3==0:
        print(i, '\t' 'div by 3')
    elif i%1==0:
        print(i, '\t' 'neither')
else:
    print(i, '\t' 'both')
