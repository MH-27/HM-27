def x9(age,path):
    import os
    open1 = open("FH.txt")
    open2 = open("MH.txt")
    x = open1.readlines()
    xx = open2.readlines()
    numx = len(x) - 1
    numxx = len(xx) - 1
    while numx >= 0:
        while numxx >= 0 and numx >= 0:
            write = open("x1.txt","a")
            write.write(f"{x[numx][:-1]}{xx[numxx]}"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}._\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}._\n"
                        f"{x[numx][:-1]}#{xx[numxx]}"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{age[:2]}\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{age[4:8]}\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{age[4:6]}\n"
                        f"{x[numx][:-1]}#{xx[numxx][:-1]}#{age[6:8]}\n"
                        f"{x[numx][:-1]}##{xx[numxx]}"
                        f"{x[numx][:-1]}@{xx[numxx]}"
                        f"{x[numx][:-1]}@@{xx[numxx]}"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}._\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}._\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}\n"
                        f"{x[numx][:-1]}//{xx[numxx][:-1]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[0:1]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[0:1]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[0:1]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[0:1]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[0:1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[0:1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[0:1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[0:1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[0:1]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[1:2]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[1:2]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[1:2]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[1:2]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[1:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[1:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[1:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[1:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[1:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[:2]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[:2]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[:2]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[:2]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[:2]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[2:3]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[2:3]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[2:3]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[2:3]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[2:3]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[2:3]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[2:3]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[2:3]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[2:3]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[3:4]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[3:4]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[3:4]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[3:4]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[3:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[3:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[3:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[3:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[3:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[2:4]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[2:4]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[2:4]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[2:4]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[2:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[2:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[2:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[2:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[2:4]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[4:6]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[4:6]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[4:6]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[4:6]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[4:6]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[4:6]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[4:6]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[4:6]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[4:6]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[6:8]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[6:8]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[6:8]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[6:8]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[6:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[6:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[6:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[6:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[6:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}{age[4:8]}\n"
                        f"{x[numx][:-1]}-{xx[numxx][:-1]}-{age[4:8]}\n"
                        f"{x[numx][:-1]}_{xx[numxx][:-1]}_{age[4:8]}\n"
                        f"{x[numx][:-1]}/{xx[numxx][:-1]}/{age[4:8]}\n"
                        f"{x[numx][:-1]},{xx[numxx][:-1]},{age[4:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}_{age[4:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}-{age[4:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]}/{age[4:8]}\n"
                        f"{x[numx][:-1]}{xx[numxx][:-1]},{age[4:8]}\n"
 )
            numxx -= 1
            write.close()
            if numxx < 0:
                numx -= 1
                numxx = len(xx) - 1
    open1.close()
    open2.close()
    write.close()
    os.remove("FH.txt")
    os.remove("MH.txt")
    os.remove("LH.txt")
    os.rename("x1.txt",path)
    from termcolor import colored
    return (colored("      setup 16/18 is completed     ","red"))


