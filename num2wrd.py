a = 0
num2wrd = {1: 'one',2:'two',3:'three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',
           12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eightteen',19:'Nineteen',
           20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',
           100: 'Hundred',1000:'Thoushand'}

while (a <= 10000):
    a= a + 1
    if (num2wrd.get(a) != None):
        print(a, "in words is",num2wrd.get(a))

    elif(a%100 == 0 and a/100 <10 ):
            a = str(a)
            if(len(a) < 4):
                print(a[0],a[1],a[2])
                if(a[1] == '0' and a[2] == '0'):
                    print(a,"in words is",num2wrd.get(int(a[0])), num2wrd.get(100))
            a = int(a)
    elif (a%1000 == 0):
            a = str(a);
            if(len(a) < 5 and (a[1] =='0' and a[2] == '0' and a[3] == '0')):
                print(a, "in words is ",num2wrd.get((int(a[0]))), num2wrd.get(1000))
            else:
                if(len(a) < 5 and a[1] != '0' and a[2] != '0' and a[3] == '0'):
                    b= a[2] + a[3]
                    print(a, 'in words is ', num2wrd.get(int(a[0])), num2wrd.get(1000),num2wrd.get(int(int(a[1]))),num2wrd.get(100),num2wrd.get(int(b)))
                elif(len(a) < 5 and a[1] != '0' and a[2] == '0' and a[3] == '0'):
                    print(a, 'in words is ', num2wrd.get(int(a[0])), num2wrd.get(1000), num2wrd.get(int(int(a[1]))),num2wrd.get(100));
                elif(len(a) == 5 and a[1] == '0' and a[2] == '0' and a[3] == '0' and a[4] == '0'):
                    b= a[0] + a[1]
                    print(a,'in words is ', num2wrd.get(int(b)), num2wrd.get(1000))
            a = int(a);
    else:
            a= str(a)
            if(len(a) == 4 and a[2] == '1'):
                    b = a[2] + a[3]
                    print(a, 'in words is ', num2wrd.get(int(a[0])), num2wrd.get(1000), num2wrd.get(int(a[1])),
                          num2wrd.get(100), num2wrd.get(int(b)))
            elif(len(a) == 4 and a[2]!= '1'):
                  b= a[2] + '0'
                  print(a, 'in words is', num2wrd.get(int(a[0])), num2wrd.get(1000),num2wrd.get(int(a[1])),num2wrd.get(100),num2wrd.get(int(b)),num2wrd.get(int(a[3])))
            else:
                if(len(a) == 3 and a[1]!=0):
                    b= a[1] + a[2]
                    print(a,"in words is", num2wrd.get(int(a[0])),num2wrd.get(100),num2wrd.get(int(b)))
                elif(len(a) == 3 and a[1] == 0):
                    print(a,'in words is ', num2wrd.get(int(a[0])),num2wrd.get(100),num2wrd.get(int(a[2])))
                else:
                    if(len(a) == 2 ):
                        b= a[0] + '0'
                        print(a,'in words is',num2wrd.get(int(b)),num2wrd.get(int(a[1])))
            a = int(a);
