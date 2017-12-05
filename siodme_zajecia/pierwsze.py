#napisz program ktory kompiluje kod c++ a nastepnie uruchamia go i sprawdza czy jego dzialanie nie konczy sie bledem
import subprocess

try:
    out1 = subprocess.check_call([" g++ -o program program.cpp"], shell=True)
    out2=subprocess.check_call(["./program"], shell=True)
except subprocess.CalledProcessError as e:
     print e
print out1
print out2