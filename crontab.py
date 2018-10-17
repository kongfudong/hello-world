import os
import datetime
import sys
import logging.config
import json

def setup_logging(default_path = "logging.json",default_level = logging.INFO,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)


#sys.setrecursionlimit(5000)

today=datetime.date.today().strftime('%Y%m%d')
remove_date=(datetime.date.today() + datetime.timedelta(days=-30)).strftime('%Y%m%d')
#print(remove_date)

def mkdir():
    path=((r"C:\Users\ezhawud\Downloads\ERBS\testdata\\") + today)
    folder = os.path.exists(path) 
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        logger.info("new folder..." +path)
        logger.info("OK")
    else:
        logger.info("There is this folder!" +"<"+path+">")
        
def remove(path):
    folder =os.path.exists(path)
    if not folder:
        logger.info("There is no this folder!"+"<"+path+">")
    #else:
        #os.rmdir(path)
        #print("--- remove folder!---"+path)
    else:
        if os.path.isfile(path):
            try:
                os.remove(path)
                #logger.info("remove file:"+path)
            except Exception as e:
                logger.debug(e)
        elif os.path.isdir(path):
            for i in os.listdir(path):
                path_file =os.path.join(path,i)#取文件绝对路径
                #print(path_file)
                remove(path_file)
                logger.info("remove path:"+path_file)
                try:
                    os.rmdir(path)
                    logger.info("rmdir:"+path)
                except Exception as e:
                    print(e)
                #if os.path.isfile(path_file):
                    #os.remove(path_file)
                    #os.rmdir(path)
                    #print("--- remove folder!---"+path)
                #else:
                    #remove(path_file)
                    #os.rmdir(path)
                    #print("--- remove folder!---"+path)
        
if __name__ == '__main__':
    setup_logging(default_path = "logging.json")
    mkdir()
    path=((r"C:\Users\ezhawud\Downloads\ERBS\testdata\\") + remove_date)
    remove(path)
