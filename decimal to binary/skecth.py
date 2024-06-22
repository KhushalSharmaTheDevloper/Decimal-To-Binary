# Small COde for decimal to binary
n = int(input("Enter Number To Convert"))#input
l = list()#conveting into list
while n!=0:         #while loop for work unitil value is -0
    r=n%2                   
    l.append(r) #append
    n=n//2      #divide
l.reverse()     #reverse numbers
for ele in l:
    print(ele,end = "") #removes commas and list format ([1,2,3]) => 123