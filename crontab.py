import os
import datetime
import sys

#sys.setrecursionlimit(5000)

today=datetime.date.today().strftime('%Y%m%d')
remove_date=(datetime.date.today() + datetime.timedelta(days=-30)).strftime('%Y%m%d')
#print(remove_date)

def mkdir():
    path=((r"C:\Users\ezhawud\Downloads\ERBS\testdata\\") + today)
    folder = os.path.exists(path) 
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---" +path)
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---" +path)
        
def remove(path):
    folder =os.path.exists(path)
    if not folder:
        print("--- There is no this folder! ---" +path)
    #else:
        #os.rmdir(path)
        #print("--- remove folder!---"+path)
    else:
        if os.path.isfile(path):
            try:
                os.remove(path)
            except Exception as e:
                print(e)
        elif os.path.isdir(path):
            for i in os.listdir(path):
                path_file =os.path.join(path,i)#取文件绝对路径
                #print(path_file)
                remove(path_file)
                try:
                    os.rmdir(path)
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
    mkdir()
    path=((r"C:\Users\ezhawud\Downloads\ERBS\testdata\\") + remove_date)
    remove(path)
