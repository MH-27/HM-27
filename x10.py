
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
    
    print(x1_(x,MH))
    print(clear(MH))
    print(xx1_(xx,MH))
    print(clean(MH))
    print(xxx1_(xxx,MH))
    print(cleanx(MH))
    print(x3(xxxx,MH))
    print(x4_(x))
    print(clearx("FH.txt"))
    print(x5_(xx))
    print(clearxx("MH.txt"))
    print(x6_(xxx))
    print (clearxxx("LH.txt"))
    print(x7(xxxx,MH))
    print(x8(xxxx,MH))
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
    return (colored(f"      al-ghonime  make {len(x)} passwords in {MH}     ","red")) 
