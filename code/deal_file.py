import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    rename in single file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

path = "D:\\!\\todo\\10月"
path = "C:\\Users\\Administrator\\Desktop\\10月"
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
count=0
# for file in filelist:
#     print(file)
# for file in filelist:   #遍历所有文件
#     Olddir=os.path.join(path,file)   #原来的文件路径
#     print(Olddir)
#     '''
#     if os.path.isdir(Olddir):   #如果是文件夹则跳过
#         continue
#     '''
#     filename=os.path.splitext(file)[0]   #文件名
#     filename = filename.replace('[爱迅播www.ixunbo.com]', '')
#     filename = filename.replace('(1)', '')
#
#     filetype=os.path.splitext(file)[1]   #文件扩展名
#
#     Newdir=os.path.join(path,filename+filetype)  #用字符串函数zfill 以0补全所需位数
#     print(Newdir)
#     os.rename(Olddir,Newdir)#重命名
#     count+=1



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    rename in many file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def traverse(path, filelist):
    for file in filelist:   #遍历所有文件
        dirPath = os.path.join(path, file)   #原来的文件路径

        if os.path.isdir(dirPath):   #如果是文件夹则跳过
            innerfilelist = os.listdir(dirPath)
            traverse(dirPath, innerfilelist)
        else:
            if (file.endswith('mp3')):
                pathes = path.split("\\")
                len = pathes.__len__()
                filename = os.path.splitext(file)[0]    # 文件名
                filetype = os.path.splitext(file)[1]  # 文件扩展名
                lastpathname = pathes[len - 1]             # 存放文件的文件夹名
                os.rename(dirPath,  os.path.join(path, filename + '-' + lastpathname + filetype))

traverse(path, filelist)