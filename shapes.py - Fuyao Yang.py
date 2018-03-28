a=str(raw_input("what shape are you seeking information of?"))
if a== 'rectangle':
    b=str(raw_input("what feature of rectangle are you trying to find?"))
    if b== 'length/width':
        c= str(raw_input("are you given 'perimeter and the other side length', 'area and other side length', or 'diagonal and the other side length'"))
        if c=='perimeter and the other side length':
            d=int(raw_input("what is the perimeter of the rectangle?"))
            e=int(raw_input("what is the length of the other side?"))
            print d-2*e
        elif c== 'diagonal and the other side length':
            f=int(raw_input("what is the diameter of the rectangle?"))
            g=int(raw_input("what is the length of the other side?"))
            print (f**2 - g**2)**0.5
        elif c=='area and the other side length':
            h=int(raw_input("what is the area of the rectangle?"))
            g=int(raw_input("what is the length of the other side?"))
            print h/g
    elif b== 'area':
        i=str(raw_input("are you given the length of two sides? "))
        if i=='yes':
            j=int(raw_input("what is the length of the first side?"))
            k=int(raw_input("what is the length of the second side?"))
            print round( j*k,2) #laura's meddling <-- kk
        else:
            print"please figure out the length of the two sides by starting over."
    elif b== 'perimeter':
        l=str(raw_input("are you given the length of two sides?"))
        if l== 'yes':
            m=int(raw_input("what is the length of the first side?"))
            n=int(raw_input("what is the length of the second side?"))
            print 2*m*n
        else:
            print"please figure out the length of  the two sides by starting over"
    elif b=='diagonal':
        o=str(raw_input("are you given the length of two sides?"))
        if o== 'yes':
            p=int(raw_input("what is the length of the first side?"))
            q=int(raw_input("what is the length of the second side?"))
            print (p**2+q**2)**0.5
        else:
            print"please figure out the length of the two sides by starting over"
    else:
        print"more features comming soon" 
elif a=='triangle':
    r=str(raw_input("what feature of the triangle are you trying to find?"))
    if r== 'height':
        s=str(raw_input("are you given the base and the area"))
        if s=='yes':
            t=int(raw_input("what is the base of the triangle?"))
            u=int(raw_input("what is the area of the triangle?"))
            print (2*u)/t
        else:
            print"more calculations comming soon"
    elif r== 'base':
        v=str(raw_input("are you given the height and the area"))
        if v=='yes':
            w=int(raw_input("what is the height of the triangle?"))
            x=int(raw_input("what is the area of the triangle?"))
            print (2*x)/w
        else:
            print"more calculations comming soon"
    elif r=='area':
            y=str(raw_input("are you given the base and the height?"))
            if y=='yes':
                z=int(raw_input("what is the base of the triangle"))
                aa=int(raw_input("what is the height of the triangle"))
                print 0.5*z*aa
            else:
                print"more calculations comming soon"
    elif r =='perimeter':
            ab=str(raw_input("are you given the length of the three sides?"))
            if ab=='yes':
                ac=int(raw_input("what is the length of side one"))
                ad=int(raw_input("what is the length of side two"))
                ae=int(raw_input("what is the length of side three"))
                print ac+ad+ae
            else:
                print"more calculations comming soon"
    else:
        print"more features comming soon"
else:
    print"more shapes comming soon"
