def CGPAinput():
    l3=[]
    print("Enter the your grade for the respective subjects:")
    eng=input("HS3152:")
    math=input("MA3151:")
    phy=input("PH3151:")
    chem=input("CY3151:")
    python=input("GE3151:")
    tamil=input("GE3152:")
    pylab=input("GE3171:")
    pclab=input("BS3171:")
    englab=input("GE3172:")
    l1=[eng,math,phy,chem,python,tamil,pylab,pclab,englab]
    l2=[items.upper() for items in l1]
    for i in l2:
        if i=="O":
            l3.append(10)
        elif i=="A+":
            l3.append(9)
        elif i=="A":
            l3.append(8)
        elif i=="B+":
            l3.append(7)
        elif i=="B":
            l3.append(6)
        else:
            l3.append(0)
    return(l3)

def CGPAcal(l3):
    l4=[3,4,3,3,3,1,2,2,1]
    sum=0
    for i in range(9):
        if l3[i] == 0:
            print("You have RA in one or more subjects. CGPA calculation skipped.")
            return
        sum+= l3[i] * l4[i]
    cgpa=sum/22
    print("Your CGPA is:",cgpa)
    
#mains
lst=CGPAinput()
CGPAcal(lst)
