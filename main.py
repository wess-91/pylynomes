from math import *

def degre0():
    print('L equation est de la forme a.x = 0')
    a =int(input('Entrez la valeur de a:'))
    print("La solution de l équation {}.x = 0 est : 0 ".format(a) )
    
def degre1():
    print('L equation est de la forme a.x + b = 0')
    a =int(input('Entrez la valeur de a:'))
    b =int(input('Entrez la valeur de b:'))
    s = (-b)/a
    print("La solution de l équation {}.x + {} = 0 est : 0 ".format(a,b,s) )
    
    
def degre2():
    print('L equation est de la forme a.x^2 + b.x + c = 0')
    a =int(input('Entrez la valeur de a:'))
    b =int(input('Entrez la valeur de b:'))
    c =int(input('Entrez la valeur de c:'))
    D = (b**2)-(4*a*c)
    if D==0:
        s = (-b)/(2*a)
        print("La solution de l équation {}.x^2 {}.x + {} = 0 est : {} ".format(a,b,c,s) )
    elif D>0:
        s1 = (-b+sqrt(D))/(2*a)
        s2 = (-b-sqrt(D))/(2*a)
        print("Les solutions de l équation {}.x^2 {}.x + {} = 0 sont : {} et {} ".format(a,b,c,s1,s2) )
    elif D<0:
        rs1 = (-b)/(2*a)
        is1 = sqrt(-D)/(2*a)
        print("Les solutions de l équation {}.x^2 {}.x + {} = 0 sont : {} + i{} et {} - i{} ".format(a,b,c,rs1,is1,rs1,is1) )



def degre3():
    print('L equation est de la forme a.x^3 + b.x^2 + c.x + d = 0')
    a =int(input('Entrez la valeur de a:'))
    b =int(input('Entrez la valeur de b:'))
    c =int(input('Entrez la valeur de c:'))
    d =int(input('Entrez la valeur de d:'))
    
    #Delta de la dérivée
    D= ((2*b)**2) - (4*(3*a)*c)
    print("D={}".format(D))
    #Si le Delta de la dérivée est négatif, la dérivée est strictement monotone, il n'y a donc qu'une seule solution 
    if D < 0:
        if d ==0:
            print ("0 est la solution")
        x1=1
        x2=-1     
        y1 = a*(x1**3) + b*(x1**2) + c*x1 + d
        y2 = a*(x2**3) + b*(x2**2) + c*x2 + d
        #Tant que les deux ordonnées sont du meme signe on écarte la tranche 
        while (y1>0 and y2>0 ) or (y1<0 and y2<0 ):
            x1=x1+1
            x2=x2-1
            y1 = a*(x1**3) + b*(x1**2) + c*x1 + d
            y2 = a*(x2**3) + b*(x2**2) + c*x2 + d
            print("f({}) = {}".format(x1,y1))
            print("f({}) = {}".format(x2,y2))
        
        #si une des valeur est a 0 on la retourne
        if (y1==0):
            print("{} est la solution de l'équation".format(x1))
        elif (y2==0):
            print("{} est la solution de l'équation".format(x2))
        
        #quelle valeur est proche de de 0, on fais une tranche autour de la valeur la plus proche
        if (abs(y1)<abs(y2)):
            x2=x1-1
            y2 = a*(x2**3) + b*(x2**2) + c*x2 + d
            print("f({}) = {} et f({})={} la solution est entre {} et {}".format(x1,y1,x2,y2,x1,x2))
        elif (abs(y2)<abs(y1)):
            x1=x2+1
            y1 = a*(x1**3) + b*(x1**2) + c*x1 + d
            print("f({}) = {} et f({})={} la solution est entre {} et {}".format(x1,y1,x2,y2,x1,x2))
    else:
        print("le cas n'as pas encore été traité")
    
    
def degre4():
    print('L equation est de la forme a.x^4 + b.x^3 + c.x^2 + d.x + e= 0')


degre = int(input('Entrez le degré de l équation :'))
if degre==0:
    degre0()
elif degre==1:
    degre1()
elif degre==2:
    degre2()
elif degre==3:
    degre3()
elif degre==4:
    degre4()
