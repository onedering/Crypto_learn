
def evklid_algoritm(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
        print(a, b)
    else:
        print("answer", a)
        return a, b


def evlkid_bin_algoritm(a, b):
    k = 1
    while a!=b or a!=0 or b!=0 :
        if a%2==0 and b%2 == 0:
            k*=2
            a//=2
            b//=2

        elif a%2==0 and b%2 != 0:
            a//=2

        elif a%2!=0 and b%2 == 0:
            b//=2

        elif a%2!=0 and b%2 != 0 and a>b:   
            a-=b

        elif a%2!=0 and b%2 != 0 and a<b:
            a,b = b,a
            a-=b
        else:
            print("k =" ,k," a =", a," b =", b)
            print("answer", k* a)
            return (a,b)
        print("k =" ,k," a =", a," b =", b)
    return(a,b)


def ext_gcd(a, b):

        if a == 0: return 1, 1, b
        if b == 0: return 1, 1, a
        if not a&1 | b&1:
            # ��� ������ - x � y �� �������, gcd ���������
            x, y, g = ext_gcd(a>>1, b>>1)
            return x, y, g<<1
        elif not a&1:
            # a - ������, b - ��������
            x, y, g = ext_gcd(a>>1, b)
            return (x-b>>1, y+(a>>1), g) if x&1 else (x>>1, y, g)
        elif not b&1:
            # a - ��������, b - ������
            x, y, g = ext_gcd(a, b>>1)
            return (x+(b>>1), y-a>>1, g) if y&1 else (x, y>>1, g)
        elif b > a:
            # ��� ��������
            x, y, g = ext_gcd(a, b-a)
            return x-y, y, g
        else:
            # ��� ��������
            x, y, g = ext_gcd(a-b, b)
            return x, y-x, g
