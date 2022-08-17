from cmath import exp
import os
from edit import ed
from pickletools import long4
import readchar
class fil:
    def ls():
        try:
            fl = os.listdir()
            lenfl = len(fl)
            i = 0
            while(True):
                tpp = os.path.isfile(fl[i])
                if tpp == True:
                    type = "file"
                else:
                    type = "dir"
                print(i," : ",fl[i]," ",type)
                i += 1
                if(i >= lenfl):
                    print()
                    print(i," files")
                    return fl
        except:
            os.system("cls")
            print()
            print("0 files!")
            return fl
    def fil():
        os.system("cls")
        print("name? ",end = '')
        inp = input()
        f = open(inp, "a")
        f.close()
    def rm(fl):
        try:
            print()
            print("idex? ",end = '')
            i = input()
            i = int(i)
            x = fl[i]
            os.remove(x)
            print(x," gone!")
            print("press any key")
            print(repr(readchar.readkey()))
        except:
            try:
                x = os.getcwd()
                x = x + "/" + fl[i]
                os.rmdir(x)
                x = fl[i]
                print(x,"directory is gone!")
                print("press any key")
                print(repr(readchar.readkey()))
            except:
                print("some thing went wrong")
                input()
    def up():
        os.chdir('..')
    def dwn():
        print("index? ",end = '')
        x = input()
        x = int(x)
        fl = os.listdir() 
        print(fl[x])
        os.chdir(fl[x])
    def dir():
        print("name? ", end = "")
        nam = input()
        os.mkdir(nam)
    
        
