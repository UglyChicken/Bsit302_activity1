dota = []

lol = True

while lol:
    
    print (" lol.exe")
    
    print("1.Remove an Student")
    print("2.Add an Student")
    print("3.Update the List")
    print("4.Check the list")
    
    dota2 = int(input("Enter an Number of choice:"))
    
    if dota2 == 1:
        name = input("Remove an Student")
        
        dota.remove(name)
        
    elif dota2 == 2: 
        name = input ("Enter an Name")
        
        dota.append(name)
        
    elif dota2 == 3:
            print(dota)
            kent = int(input("Which name?"))
            print("Change" + dota[kent]+"to?")
            
            keny = input()
            dota[kent] = keny
            print("Succes")
            
    elif dota2 == 4:
                print(dota)
    break
