#Write the solution of problem two in this file
а = [7,16,43,27,49,97,81]
flag=True
for x in a:
    for num in range(2, x/2+1):
        if(x%num==0):
            flag=False 
            break
    if flag:
        print(x, 'простое число')
    else:
        print(x, 'не простое число')
