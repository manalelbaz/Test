#print out the console the integer numbers from 30 to 300 
for num in range(30, 300):
    #multiples of 7
    if (num%7==0 and num%13!=0):
        print num, "-->", "abc"
    #multiples of 13
    elif(num%13==0 and num%7!=0):
        print num, '-->', 'xyz'
    #multiples of 7 and 13
    elif(num%7==0 and num%13==0):
        print num, '-->', 'a-z'
    #if not
    else:
        print num
            


