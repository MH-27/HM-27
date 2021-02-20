
def x7(age,path):
    open1 = open("FH.txt")
    open2 = open("MH.txt")
    open3 = open("LH.txt")
    x = open1.readlines()
    xx = open2.readlines()
    xxx = open3.readlines()
    numx = len(x) - 1
    numxx = len(xx) - 1
    numxxx = len(xxx)-1
    while numx >= 0:
        while numxxx >= 0 and numxx >= 0 and numx >= 0 :
            write = open(path,"a")
            write.write(f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx]}"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx]}"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx]}"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx]}"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[0:1]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[0:2]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[1:2]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[2:3]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[3:4]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[2:4]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[4:6]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[6:8]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{xxx[numxxx][:-1]}-{age[4:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age}\n"     
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[0:1]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[0:2]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[1:2]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[2:3]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[3:4]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[2:4]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[4:6]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[6:8]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{xxx[numxxx][:-1]}{age[4:8]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age}_\n"     
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[0:1]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[0:2]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[1:2]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[2:3]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[3:4]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[2:4]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[4:6]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[6:8]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[4:8]}_\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age}\n"     
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[0:1]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[0:2]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[1:2]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[2:3]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[3:4]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[2:4]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[4:6]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[6:8]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age[4:8]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{xxx[numxxx][:-1]}_{age}_\n"     
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[0:1]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[0:2]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[1:2]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[2:3]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[3:4]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[2:4]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[4:6]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[6:8]}_\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{xxx[numxxx][:-1]}#{age[4:8]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age}_\n"     
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[0:1]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[0:2]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[1:2]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[2:3]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[3:4]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[2:4]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[4:6]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[6:8]}_\n"
                        f"{x[numx][:-1]}@{xx[numxx][:-1]}@{xxx[numxxx][:-1]}@{age[4:8]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}@{age}_\n"     
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[0:1]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[0:2]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[1:2]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[2:3]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[3:4]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[2:4]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[4:6]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[6:8]}_\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{xxx[numxxx][:-1]}/{age[4:8]}_\n"





                        )
            numxxx -= 1
            write.close()
            if numxxx < 0:
                numxx -= 1
                numxxx = len(xxx) - 1
                write.close()
            if numxx < 0:
                numx -= 1
                numxx = len(xx)-1
                numxxx = len(xxx)-1
                write.close()
    from termcolor import colored
    return (colored("      setup 14/18 is completed     ","red"))









