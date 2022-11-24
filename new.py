i=0
while i<6:
    i+=1
    if i==5:
        continue
    print(i)
    j=0
    while j<6:
        j+=1
        if i==5:
            break
        print(j)