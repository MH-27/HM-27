def x5(name):
    return f"{name}\n" \
           f"{name.upper()}\n" \
           f"{name.capitalize()}\n" \
           f"{name[0:1].lower()}{name[1:2].upper()}{name[2:].lower()}\n" \
           f"{name[0:2].lower()}{name[2:3].upper()}{name[3:].lower()}\n" \
           f"{name[0:3].lower()}{name[3:4].upper()}{name[4:].lower()}\n" \
           f"{name[0:4].lower()}{name[4:5].upper()}{name[5:].lower()}\n" \
           f"{name[0:5].lower()}{name[5:6].upper()}{name[6:].lower()}\n" \
           f"{name[0:6].lower()}{name[6:7].upper()}{name[7:].lower()}\n" \
           f"{name[0:7].lower()}{name[7:8].upper()}{name[8:].lower()}\n" \
           f"{name[0:8].lower()}{name[8:9].upper()}{name[9:].lower()}\n" \
           f"{name[0:9].lower()}{name[9:10].upper()}{name[10:].lower()}\n" \
           f"{name[0:10].lower()}{name[10:11].upper()}{name[11:].lower()}\n" \
           f"{name[0:11].lower()}{name[11:12].upper()}{name[12:].lower()}\n" \
           f"{name[0:1].upper()}{name[1:].lower()}\n" \
           f"{name[0:2].upper()}{name[2:].lower()}\n" \
           f"{name[0:3].upper()}{name[3:].lower()}\n" \
           f"{name[0:4].upper()}{name[4:].lower()}\n" \
           f"{name[0:5].upper()}{name[5:].lower()}\n" \
           f"{name[0:6].upper()}{name[6:].lower()}\n" \
           f"{name[0:7].upper()}{name[7:].lower()}\n" \
           f"{name[0:8].upper()}{name[8:].lower()}\n" \
           f"{name[0:9].upper()}{name[9:].lower()}\n" \
           f"{name[0:10].upper()}{name[10:].lower()}\n" \
           f"{name[0:11].upper()}{name[11:].lower()}\n" \
           f"{name[0:12].upper()}{name[12:].lower()}\n" \
           f"{name[0:1].upper()}{name[1:].upper()}\n" \
           f"{name[0:2].upper()}{name[2:].upper()}\n" \
           f"{name[0:3].upper()}{name[3:].upper()}\n" \
           f"{name[0:4].upper()}{name[4:].upper()}\n" \
           f"{name[0:5].upper()}{name[5:].upper()}\n" \
           f"{name[0:6].upper()}{name[6:].upper()}\n" \
           f"{name[0:7].upper()}{name[7:].upper()}\n" \
           f"{name[0:8].upper()}{name[8:].upper()}\n" \
           f"{name[0:9].upper()}{name[9:].upper()}\n" \
           f"{name[0:10].upper()}{name[10:].upper()}\n" \
           f"{name[0:11].upper()}{name[11:].upper()}\n" \
           f"{name[0:12].upper()}{name[12:].upper()}\n" \
           f"{name.lower()}\n" \
           f"{name[0:1].lower()}{name[1:].upper()}\n" \
           f"{name[0:1].upper()}{name[1:2].lower()}{name[2:].lower()}\n" \
           f"{name[0:2].upper()}{name[2:3].lower()}{name[3:].upper()}\n" \
           f"{name[0:3].upper()}{name[3:4].lower()}{name[4:].upper()}\n" \
           f"{name[0:4].upper()}{name[4:5].lower()}{name[5:].upper()}\n" \
           f"{name[0:5].upper()}{name[5:6].lower()}{name[6:].upper()}\n" \
           f"{name[0:6].upper()}{name[6:7].lower()}{name[7:].upper()}\n" \
           f"{name[0:7].upper()}{name[7:8].lower()}{name[8:].upper()}\n" \
           f"{name[0:8].upper()}{name[8:9].lower()}{name[9:].upper()}\n" \
           f"{name[0:9].upper()}{name[9:10].lower()}{name[10:].upper()}\n" \
           f"{name[0:10].upper()}{name[10:11].lower()}{name[11:].upper()}\n" \
           f"{name[0:11].upper()}{name[11:12].lower()}{name[12:].upper()}\n" \
           f"{name[0:1].lower()}{name[1:].upper()}\n" \
           f"{name[0:2].lower()}{name[2:].upper()}\n" \
           f"{name[0:3].lower()}{name[3:].upper()}\n" \
           f"{name[0:4].lower()}{name[4:].upper()}\n" \
           f"{name[0:5].lower()}{name[5:].upper()}\n" \
           f"{name[0:6].lower()}{name[6:].upper()}\n" \
           f"{name[0:7].lower()}{name[7:].upper()}\n" \
           f"{name[0:8].lower()}{name[8:].upper()}\n" \
           f"{name[0:9].lower()}{name[9:].upper()}\n" \
           f"{name[0:10].lower()}{name[10:].upper()}\n" \
           f"{name[0:11].lower()}{name[11:].upper()}\n" \
           f"{name[0:12].lower()}{name[12:].upper()}\n" \
           f"{name[0:2].lower()}{name[2:].upper()}\n" \
           f"{name[0:3].lower()}{name[3:].upper()}\n" \
           f"{name[0:4].lower()}{name[4:].upper()}\n" \
           f"{name[0:5].lower()}{name[5:].upper()}\n" \
           f"{name[0:2].upper()}{name[2:].lower()}\n" \
           f"{name[0:3].upper()}{name[3:].lower()}\n" \
           f"{name[0:4].upper()}{name[4:].lower()}\n" \
           f"{name[0:5].upper()}{name[5:].lower()}\n" \
           f"{name[0].lower()}{name[1:3].upper()}{name[3:].lower()}\n"


def x5_(name):
       from x5 import x5
       openx = open("MH.txt","a")
       openx.write(x5(name))
       openx.close()
       from termcolor import colored
       return (colored("      setup 10/18 is completed     ","red"))
