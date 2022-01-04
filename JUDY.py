#@NOIR_noir
#NOIR THFAR.py
import pyfiglet
#========================#

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
#=========================#
logo = pyfiglet.figlet_format('S c r e a m')
print(C+logo)
#==========================#
print ("\033[1;33mWelcome to the test, please write the answer ( small ) ")
print ("\033[2;34m==========================")
print (" \033[2;35mYou get 3 attempts")
print ("\033[2;34m===========================")
#==========================#
secret_answer = "cairo"
answer = "" 
count = 0 
limit = 3 
lose = False
while secret_answer != answer and not lose:
    if count < limit:
        answer = input("\033[2;36mWhat Is The Capital Of Egypt ؟   ")
        count += 1
    else:
        lose = True
print ("")
if lose:
    print(" \033[1;31mYour attempts are over [X] 	")
else:
    print("\033[2;32mThe answer is correct [√]")