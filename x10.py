
def xxx(x,xx,xxx,xxxx,MH):
    import sys
    import os
    from x1 import x1_
    from xx1 import xx1_
    from xxx1 import xxx1_
    from x3 import x3
    from x4 import x4_
    from x5 import x5_
    from x6 import x6_
    from x7 import x7
    from x8 import x8
    from x9 import x9
    from clear import clear
    from clearx import clearx
    from clearxx import clearxx
    from clearxxx import clearxxx
    from clean import clean 
    from cleanx import cleanx 
    x = str(x)
    xx = str(xx)
    xxx = str(xxx)
    xxxx = str(xxxx)
    MH = str(MH)
    print(x1_(x))
    print(clear("x1.txt"))
    print(xx1_(xx))
    print(clean("xx1.txt"))
    openx = open("xx1.txt")
    x1 = openx.readlines()
    num = len(x1)-1
    for i in x1 :
        open1 = open("x1.txt","a")
        open1.write(f"{x1[num]}")
        open1.close
        num -=1
    openx.close()
    open1.close()
    os.remove("xx1.txt")
    print(xxx1_(xxx))
    print(cleanx("xxx1.txt"))
    openx = open("xxx1.txt")
    x2= openx.readlines()
    num = len(x2)-1
    for i in x2 :
        open1 = open("x1.txt","a")
        open1.write(f"{x2[num]}")
        open1.close
        num -=1
    openx.close()
    open1.close()
    os.remove("xxx1.txt")
    print(x3(xxxx))

    print(x4_(x))
    print(clearx("FH.txt"))
    print(x5_(xx))
    print(clearxx("MH.txt"))
    print(x6_(xxx))
    print (clearxxx("LH.txt"))
    print(x7(xxxx,"x1.txt"))
    print(x8(xxxx,"x1.txt"))
    print(x9(xxxx,MH))
    from termcolor import colored
    print (colored("      setup 17/18 is completed     ","red"))
    print (colored("      setup 18/18 is completed     ","red"))
    openx = open(MH)
    xx = openx.read()
    print(xx)
    openx.close()
    open2 = open(MH)
    x = open2.readlines()
    open2.close()
    print("")
    print("")
    from termcolor import colored
    return (colored(f"      x-word  make {len(x)} passwords in {MH}     ","red")) 
