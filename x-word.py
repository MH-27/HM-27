import sys
xx = sys.version[:3]
x = ["3.8","3.7","3.9"]
if xx in x :
    pass
else:
    print("")
    print("")
    print("             #  run the program with python3  #   ")
    print("")
    print("")
    exit()
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
from x10 import xxx
from pyfiglet import Figlet
from termcolor import colored
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
x = Figlet(font="standard")
print (colored(x.renderText("          x - word  "),"blue"))
print("")

print("\n\n")
fn = input(colored("      type the first name ==>     ", "red")).strip()
while fn == "" :
    print(colored("               #   you must type the person name   #    ","green"))
    fn = input(colored("      type the first name ==>     ", "red")).strip()
    if fn != None :
        pass
    else:
        print("")

mn   = input(colored("      type the middle name ==>     ","red")).strip()
while mn == "" :
    print(colored("              #    you must type the middle name   #    ","green"))
    mn = input(colored("      type the middle name ==>     ", "red")).strip()
    if mn != None :
        pass
    else:
        print("")
ln   = input(colored("      type the last  name ==>     ","red")).strip()
while ln == "" :
    print(colored("              #    you must type the last name  #     ","green"))
    ln = input(colored("      type the last name ==>     ", "red")).strip()
    if ln != None :
        pass
    else:
        print("")
age  = input(colored("      type the age  ==>     ","red")).strip()
while len(age) != 8 :
    print(colored("                  the birth day must been 8 numpers      ","green"))
    age = input(colored("      type the age  ==>     ", "red")).strip()
    if age == 8 :
        pass
    else:
        print("")
path  = input(colored("      enter the file name to save passwords      ==>     ","red")).strip()
er = "/"
while er in  path :
    print("")
    print(colored("     #   you must type a file name with out the path ex: xx.txt  #    ","green"))
    print("")
    path  = input(colored("      enter the file name to save passwords      ==>     ","red")).strip()
    if er in path :
        pass
    else:
        print("")
while path == "" :
    print(colored("              #    you must type the file name  #     ","green"))
    print("")
    path  = input(colored("      enter the file name to save passwords      ==>     ","red")).strip()
    if path != None :
        pass
    else:
        print("")
print (colored("                            please wait          ","yellow"))
print("")
print(xxx(fn,mn,ln,age,path))
print("")
print("")
print (colored("                          #    Done !    #         ","yellow"))
print("")
print("")
