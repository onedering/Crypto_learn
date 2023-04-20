import function

print("nummber alogoritm")
print("1 - evklid")
print("2 - bin evklid")
print("3 - ext_gcd")
vibor = int(input())

if vibor == 1:
    a=int(input("num a:"))
    b=int(input("num b:"))
    function.evklid_algoritm(a, b)
elif vibor == 2:
    a = int(input("num a:"))
    b = int(input("num b:"))
    function.evlkid_bin_algoritm(a, b)
elif vibor == 3:
    a = int(input("num a:"))
    b = int(input("num b:"))
    x,y,g=function.ext_gcd(a,b)
    print(f"({x})*{a} + ({y})*{b} = {g}")
else:
    print("err")