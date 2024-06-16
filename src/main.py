import zipfile
with zipfile.ZipFile("../resources/system/default/maths.res") as zf:
    zf.extractall("M")
with zipfile.ZipFile("../resources/system/default/test.res") as zf2:
    zf2.extractall()
with zipfile.ZipFile("../resources/system/default/useredit.res") as zf2:
    zf2.extractall()
from M.math.src import math # type: ignore
from useredit.src import useredit # type: ignore
import shutil
Mathfuncs = {"add": math.add, "mul": math.mul, "pom": math.pom, "sub": math.sub, "div": math.div, "init": math.init}
add = Mathfuncs["add"]
mul = Mathfuncs["mul"]
pom = Mathfuncs["pom"]
sub = Mathfuncs["sub"]
div = Mathfuncs["div"]
minit = Mathfuncs["init"]
Userfuncs = {"addData": useredit.addData, "retData": useredit.retData, "remData": useredit.remData, "init": useredit.init}
addData = Userfuncs["addData"]
retData = Userfuncs["retData"]
remData = Userfuncs["remData"]
uinit = Userfuncs["init"]
if minit():
    print("MATH_RES: OK")
else:
    print("MATH_RES: FAILED")
if uinit():
    print("USER_RES: OK")
else:
    print("USER_RES: FAILED")
addData("test", hex(1))
addData("test", hex(2))
addData("test", hex(3))
addData("test", hex(4))
addData("test", hex(5))
addData("test", hex(6))
addData("test", hex(7))
addData("test", hex(8))
addData("test", hex(9))
addData("test", hex(10))
addData("test", hex(11))
addData("test", hex(12))
from useredit.data import default # type: ignore
for i in default.userdata.data:
    print(str(i) + ": " + retData(i))
shutil.rmtree("M")
shutil.rmtree("test")
shutil.rmtree("useredit")