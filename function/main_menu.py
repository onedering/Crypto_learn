
import function
key = "true"
def help_menu():
    print("alogoritm's list")
    print(" 1 - evklid")
    print(" 2 - bin evklid")
    print(" 3 - ext_gcd")
    print(" 4 - brute_force_decomposition")
    print(" 5 - Fermat's factorization method")
    print(" 0 - exit")
    print(" 999 - help menu")


help_menu()

while key!=0:
    key = int(input("key: "))
    if key== 0:
        print(" It's end")
    elif key == 1:
        a=int(input("num a:"))
        b=int(input("num b:"))
        function.evklid_algoritm(a, b)
    elif key == 2:
        a = int(input("num a:"))
        b = int(input("num b:"))
        function.evlkid_bin_algoritm(a, b)
    elif key == 3:
        a = int(input("num a:"))
        b = int(input("num b:"))
        x,y,g=function.ext_gcd(a,b)
        print(f"({x})*{a} + ({y})*{b} = {g}")
    elif key == 4:
        function.brute_force_decomposition(int(input("Number: ")))
    elif key == 5:
        function.fermats_factorization_method(int(input("Number: ")))
    elif key == 999:
        help_menu()
    else:
        print("err")