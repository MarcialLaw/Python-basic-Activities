def ChickensAndRabbits(HeadCount,LegCount):
    for num in range(1,HeadCount+1):
        Rabbits = HeadCount-num
        if (num*2) + (Rabbits*4) == LegCount:
            return{"Rabbits":Rabbits,"Chickens":(num)}
            return {"Rabbits":Failed, "Chikens":Failed}

        
solution = ChickensAndRabbits(35,94)
print("Chickens",solution["Chickens"])
print("Rabbits",solution["Rabbits"])


