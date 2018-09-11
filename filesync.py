#-*- coding:utf-8 -*-
import time
import sys
import os
import hashlib
import operator
import configparser
import logging
import shutil

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')
file_num=config.get('createfile','file_num')
file_path=config.get('createfile','file_path')
file_format = config.get('createfile','file_format')
file_size = config.get('createfile','file_size')
check_md5 =config.get('createfile','check_md5')
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger("")
handler =logging.FileHandler("file.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#对文件夹中的文件进行排序
def compare(x,y):
    stat_x = os.stat(file_path+"/"+x)
    stat_y = os.stat(file_path+"/"+y)
    if stat_x.st_ctime<stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime>stat_y.st_ctime:
        return 1
    else:
        return 0
        
#创建文件
def createfile():
    logger.info("======CREATE FILE BEGIN======")
    for i in range(int(file_num)):
        local_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        temp_name = file_path+str(i)+"-"+str(local_time)+"."+file_format
        bigFile= open(temp_name, 'w')
        bigFile.seek(1024*1024*int(file_size)) #配置文件中无法使用乘法？
        bigFile.write('test')#写文件
        time.sleep(0.1)
        bigFile.close()
        if check_md5 =="on":
            file_md5=get_md5(temp_name)
            #print(file_md5)
            file_name =  file_path+str(i)+"-"+file_md5[0]+"."+file_format
            logger.info(file_name)
            if not os.path.exists(file_name):
                os.rename(temp_name,file_name)
                files=os.listdir(file_path)
                #print(os.stat(file_name).st_ctime)
                #files.sort(key=os.stat(file_name).st_ctime,compare)
        else:
            file_name = temp_name
            logger.info(file_name)
    logger.info("======CREATE FILE END=======")
        
#删除文件      
def deletefile():
    delete_file_num = config.get('deletefile','delete_file_num')
    files = os.listdir(file_path)
    count=0
    for file in files:
        if os.path.isfile(os.path.join(file_path,file)):
            count =count+1
        if count >= int(delete_file_num):
            os.remove(file_path+"\\"+file)#删除文件
            logger.info("======DELETE FILE OK!!!=====")
#删除文件夹全部文件
def delete_all_file():
    files =os.listdir(file_path)
    for file in files:
        os.remove(file_path+"\\"+file)
        logger.info("delete"+file)
    logger.info("======DELETE ALL FILE OK!!!=====")

#计算文件MD5值
def get_md5(filename):
    _FILE_SLIM=100*1024*1024  
    calltimes = 0     #分片的个数  
    hmd5 = hashlib.md5()  
    fp = open(filename, "rb")  
    f_size = os.stat(filename).st_size #得到文件的大小  
    if f_size > _FILE_SLIM:  
        while (f_size > _FILE_SLIM):  
            hmd5.update(fp.read(_FILE_SLIM))  
            f_size /= _FILE_SLIM  
            calltimes += 1  # delete    #文件大于100M时进行分片处理  
        if (f_size > 0) and (f_size <= _FILE_SLIM):  
            hmd5.update(fp.read())  
    else:  
        hmd5.update(fp.read())  
    return (hmd5.hexdigest(), calltimes)
#接收端文件校验
def file_recv():
    if check_md5=="on":
        files =os.listdir(file_path)
        #files.sort(reverse=True,key=os.stat.ctime)
        #logger.debug(files)
        if os.path.exists(file_path+os.sep+files[0]):
            new_file_md5 =get_md5(file_path+os.sep+files[0])
        else:
            logger.info("file not exists!!!")
            sys.exit()
        old_file_md5 =files[0].split(".")[0].split("-")[1]
        if new_file_md5[0] == old_file_md5:
            logger.info("check MD5 OK！！"+"delete-"+file_path+os.sep+files[0])
            os.remove(file_path+"\\"+files[0])
        else:
            bak_path = config.get("createfile",'bak_path')
            if not os.path.exists(bak_path):
                os.mkdir(bak_path)
                shutil.move(file_path+"\\"+files[0],bak_path)
                logger.info("move-"+file_path+"\\"+files[0])
    else:
        deletefile()
          
if __name__ == '__main__':
    sync_mode= config.get('sync_mode','sync_mode')
    if sync_mode =='send':
        helper = '''function:
                        1 create new file
                        2 delete file
                        q quit
        please input number:'''
        while True:
            option =input(helper)
            if operator.eq(option,'1'):
                createfile()
                deletefile()
            elif operator.eq(option,'2'):
                delete_all_file()
            elif operator.eq(option,'q'):
                logger.info("quit!")
                break
            else:
                logger.debug("error input,please try again...")
    else:
        files=os.listdir(file_path)
        count =0
        for file in files:
            count=count+1
            #print(count)
        if count==1:
            file_recv()
        else:
            for i in range(count):
                file_recv()
                count=count-1
                #print(count)
                #if count ==0:
                    #sys.exit()
