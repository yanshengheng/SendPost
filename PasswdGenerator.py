#	generate password for sit OA
#	password has 6 bit 000000-999999
#	but we can reduce it to:
#	_   _   _   _   _   _
#	10  4   10  10  10  5

#depond on id card rules
#this indicate a female id card last 6 numbers;
def PwdGenerator(i1,i2,i3,i4,i5,i6):
    first = ['0','1','2','3','4','5','6','7','8','9']
    second =['0','1','2','3']
    third2fifth = ['0','1','2','3','4','5','6','7','8','9']
    female_num = ['0','2','4','6','8']
    pwd = first[i1] + second[i2] + third2fifth[i3] + third2fifth[i4] + third2fifth[i5] + female_num[i6]
    print pwd
    return pwd

def PwdCracker():
    pwd_ls = []
    for i6 in range(0,5):#gender number
        for i5 in range(0,10):
            for i4 in range(0,10):
                for i3 in range(0,10):#date
                    for i2 in range(0,4):#date
                        for i1 in range(0,10):#month
                            if i2 == 0 and i3 ==0:#no month:00 date exist 
                                continue
                            if i2 == 3 and i3 > 1:# data cannot be bigger than 31
                                continue
                            if (i1 == 4 or i1 == 6 or i1 == 9) and i2 == 3 and i3 >0:
                                continue
                            pwd = PwdGenerator(i1,i2,i3,i4,i5,i6)
                            pwd_f.write(pwd+"\n")
							#pwd_ls.append(pwd)				
    

if __name__=="__main__":
	
    pwd_f = open("pwd_dty.txt","w")
 
    PwdCracker()
    pwd_f.close()
