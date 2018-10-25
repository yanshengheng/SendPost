import urllib
import time

PIC_FOLDER_URL = "http://ems.sit.edu.cn:85/files_upload/photo/teacher/"
LOCAL_FOLDER = "/Users/yanyu/Pictures/" #local mathine path, depend on your os
#url_:is a picture url, path: where the picture saved, with file'name.
#this func wound download contain of "url_" and saved to the path;
def GetPic(url_,path):
    try:
        res=urllib.urlopen(url_)#url conflict
    except IOError:
        print "IOError occured." 
    time.sleep(1)
    if res.getcode()==200:
        right_dir = path
	print "Found     "
	pic_f = open(right_dir,"wd")
	pic_f.write(res.read()) 
        pic_f.close() 
#generate right picture's name 
def GetTeacherPicNames():
    t = []
    for i in range(0,10000):
        if i<10:
            t.append("000"+str(i)+".jpg")
        elif i>10 and i<100:
            t.append("00"+str(i)+".jpg")
        elif i>100 and i<1000:
            t.append("0"+str(i)+".jpg")
        else:
            t.append(str(i)+".jpg")#here I found press '.' vim wound repeat what you do.
    return t
        
if __name__=="__main__":
    pic_list = GetTeacherPicNames()
    pic_url = PIC_FOLDER_URL + pic_list[1]
    local_path = LOCAL_FOLDER + pic_list[1] #press ctrl+[ exit vim mode
    GetPic(pic_url,local_path)
