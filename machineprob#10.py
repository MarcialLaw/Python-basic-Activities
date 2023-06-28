i=input("Please input text! :")
def odd__values__string(str):
    result=""
    for i in range(len(str)):
        if i%2 == 0:
            result = result + str[i]
    return result
print(odd__values__string('H1e2l3l4o5w6o7r8l9d'))
