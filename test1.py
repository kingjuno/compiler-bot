arg="""
size = int(input())
for a in range(0, size): 
    for b in range(a, size): 
        print(" ", end = "") 
    for b in range(1, (a * 2)):  
        print("*", end = "")  
    print("")  
for a in range(size, int(size / 2) - 1 , -2): 
    for b in range(1, size - a, 2):   
        print(" ", end = "") 
    for b in range(1, a + 1):  
        print("*", end = "") 
    for b in range(1, (size - a) + 1):  
        print(" ", end = "") 
    for b in range(1, a):  
        print("*", end = "") 
    print("")
"""
arg="try:"+arg.replace('\n','\n\t')+"\nexcept:\n\tprint(\"Error\")"
print(r'%s' %arg)