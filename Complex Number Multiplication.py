import cmath
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a=a.replace("i","j")
        b=b.replace("i","j")
        i=0
        while(i<len(a)):
            if a[i]=="+":
                break
            i+=1
        if a[i+1]=="-":
            a=a[:i]+a[i+1:]
        i=0
        while(i<len(b)):
            if b[i]=="+":
                break
            i+=1
        if b[i+1]=="-":
            b=b[:i]+b[i+1:]
        
        a=complex(a)
        b=complex(b)
        c=a*b
        cx=int(c.real)
        cy=int(c.imag)
        s= str(cx)+"+"+str(cy)+"i"
        return s