
#_________________________________++++++++++++++++++++++++++++++++++++++++++++++____________________________________-------------------------------
def inptcal(n1,n2):
    x=n1
    y=n2


    dm=list(x)
    dm.sort()

    dn=list(y)
    dn.sort()

    ex=x=len(dm)
    ey=y=len(dn)

    em=dm
    en=dn
    i=0
    while i < ((ex+ey)/2):
        for om in em:
            for on in en:
                if om == on:
                    en.remove(on)
                    em.remove(om)
        em=em
        en=en
        i=i+1   
 #   print(em,en)


    jn=em+en
#    print(jn)
    otpt=len(jn)
    return otpt


#_________________________________++++++++++++++++++++++++++++++++++++++++++++++____________________________________-------------------------------

def fcalc(inpt):
    cntr=0

    a=[1,2,3,4,5,6,0]
    b=[0,0,0,0,0,0,0]
    #loop for in which it is decresing till one ---______
    s=6
    
    while s >= 2 :

        
        n=inpt
        
        #------------------------#
        i=0
        y=n
        while i < y :
            if y <=s:
                i=i+1
            elif y>s :
                i=0
                y=y-s
                continue
    #       print(i)
        cntr=i

#        print("counter---",cntr)
        #------------------------#
        de=cntr-1
        a[de]=0
        
        j=de+1
        ok=0
        while a[j]!=0 :
            b[ok]=a[j]
            ok=ok+1
            j=j+1
        j=0
        
        while a[j]!=0 :
            b[ok]=a[j]
            j=j+1
            ok=ok+1
            
        a=b    

        b=[0,0,0,0,0,0,0]
        s=s-1
        ok=0
        j=0
    
    
    b=a
    
    
    if a[0]==1:
        print("F......friends huh")
    if a[0]==2:
        print("L...hmmmmmm hmmmmm")
    if a[0]==3:
        print("A.....not bad")
    if a[0]==4:
        print("M....ohh ohh")
    if a[0]==5:
        print("E.....too bad")
    if a[0]==6:
        print("S.....haha hehe")


#_________________________________++++++++++++++++++++++++++++++++++++++++++++++____________________________________-------------------------------
def messpr(passvar):
    print("OK........ Lets's See the number\nIt is..........",passvar)
    print("NOW let's see what letter u get")


def printer(x0,y0):
    passvar=inptcal(x0,y0)
    messpr(passvar)
    fcalc(passvar)

nmip1=str(input("Enter your name : "))
nmip2=str(input("Enter their name : "))
printer(nmip1,nmip2)




