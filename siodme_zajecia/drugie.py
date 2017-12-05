#korzystajac z modulu subprocess napisz program ktory tworzy strukture katalogow podana w formie:
import subprocess
dirStr='''K1
    K2
    K3
        K4
K5
    K6
'''
print dirStr

pwd=subprocess.call(["pwd"],shell=True)

out=subprocess.call(["mkdir K1"],shell=True)
out=subprocess.call(["mkdir K5"],shell=True)
out=subprocess.call(["cd K1"],shell=True)

out=subprocess.call(["mkdir K2"],shell=True)
out=subprocess.call(["mkdir K3"],shell=True)
out=subprocess.call(["cd K3"],shell=True)

out=subprocess.call(["mkdir K4"],shell=True)
out=subprocess.call(["cd %s"%pwd],shell=True)
out=subprocess.call(["cd K5"],shell=True)
out=subprocess.call(["mkdir K6"],shell=True)

