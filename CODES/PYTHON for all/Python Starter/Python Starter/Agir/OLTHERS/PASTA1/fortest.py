conv = "a minha amiga Jaque"
a=0
convl=conv.split()
for i in conv:
    if (i == "a"):
        a= a+1
        print(convl[-1])

print(a, convl[-1])




for i in range(0,21,1):
    
    if i%2 != 0:
        print(i)