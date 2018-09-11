import os
import datetime

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
        
def remove():
    path=((r"C:\Users\ezhawud\Downloads\ERBS\testdata\\") + remove_date)
    folder =os.path.exists(path)
    if not folder:
        print("--- There is no this folder")
    else:
        os.rmdir(path)
        print("--- remove folder!---"+path)
if __name__ == '__main__':
    mkdir()
    remove()
