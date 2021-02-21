def clear(file):
    import os
    creator = open("not_clear.txt","a")
    open1 = open("not_clear.txt")
    open2 = open(file)
    x = open2.readlines()
    xx = open1.read()
    num = 0
    for i in x :
        openxx = open(file)
        x = openxx.readlines()
        openxss = open("not_clear.txt")
        xx = openxss.read()
        if x[num] in xx :
            openxx.close()
            openxss.close()
            open2.close()
            open1.close()
            pass
        else:
            write = open("not_clear.txt","a")
            write.write(f"{x[num]}")
            write.close()
            open1.close()
            open2.close()
            openxss.close()
            openxx.close()
        num +=1
    open1.close()
    creator.close()
    open2.close()
    openx = open("not_clear.txt")
    x = openx.readlines()
    num = len(x)-1
    for i in x :
        write = open(file,"a")
        write.write(f"{x[num]}")
        write.close()
        num -= 1 
    os.remove("not_clear")
    from termcolor import colored
    return (colored("      setup 2/18 is completed     ","red"))

