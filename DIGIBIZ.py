#!/usr/bin/env python
# coding: utf-8

# In[1]:


#---------------------------------------------------------------------

#TAKING EMPTY DATA TYPES AND LIBRARIES

import random as rd
li=[]
l2=[]
l7=[[[0, 0], [0, 0]]]
addsum=[]
d={} #STORES ALL THE PURCHASE
db={} #STORES ALL THE BILLING
emp=[]

#---------------------------------------------------------------------

#PASSWORD

lp=input("PASSWORD: ")
lp1=lp.lower()
if lp1=="opendz":

#---------------------------------------------------------------------

#INTRO

    print("*WELCOME TO DIGIBIZ*")
    print()
#---------------------------------------------------------------------

#MAKING THE OUTER LOOP FOR FREE FLOW

    nS=5
    i=0
    while i in range(nS):
        print("*MAIN MENU*")
        val_1=int(input("""PRESS 1 TO OPEN STOCK SYSTEM:
PRESS 2 TO OPEN BILLING SYSTEM: 
PRESS 3 TO SHUTDOWN: """))
        print()
#--------------------------------------------------------------------

#STORING

        while val_1==1:
            print("WELCOME TO AUTOMATIC STORING SYSTEM")
            print()
            print("***************STOCK***************")
            print()
            che=str(input("""PRESS 1 TO ADD STOCK:
PRESS 2 TO CHECK STOCK: 
PRESS 3 TO CHECK SIZE OF ITEM:
PRESS 4 TO GO BACK: """))
            print()
#---------------------------------------------------------------------

#GO BACK

            if che=="4":
                break
#---------------------------------------------------------------------

#ADD STOCK

            while che=="1":
                print("***********ADD STOCK***************")
                print()
                d.update({input("ID: "):[int(x) for x in input("PURCHASE RATE PER BOX/NUMBER OF BOXES: ").split("/")]})
                a=(d.values())
                l7.append(list(a))
                n2=input("""PRESS 1 TO END: 
PRESS 2 TO CONTINUE: """)
                if n2=="2":
                    continue
                elif n2=="1":
                    break
            print("****************END****************")

#---------------------------------------------------------------------

#CHECK STOCK

            while che=="2":
                print("WELCOME TO AUTOMATIC STORING SYSTEM")
                print("**********CHECK STOCK**************")
                print()
                nI=str(input("ITEM TAG NUMBER: "))
                if nI in d:
                    print("ITEMS IN STOCK: ",d.get(nI)[1])
                elif nI not in d:
                    print("ITEM NOT IN STOCK")
                n3=input("""PRESS 1 TO END:
PRESS 2 TO CONTINUE: """)
                if n3=="2":
                    continue
                elif n3=="1":
                    break

#---------------------------------------------------------------------

#CHECK SIZE

            while che=="3":
                print("**********CHECK SIZE*************")
                print()
                add1=str(input("PRODUCT ID:     "))
                print("SIZE OF ITEM: ", add1[-1])
                n4=input("""PRESS 1 TO END: 
PRESS 2 TO CONTINUE: """)
                if n4=="2":
                    continue
                elif n4=="1":
                    break
            print()

#---------------------------------------------------------------------

#BILLING

        while val_1==2:

#---------------------------------------------------------------------

    #LOGO
            n=3
            for i in range(0,n+1,1):
                for space in range(i-1,0,-1):
                    print("*",end="")
                for j in range(i,0,-1):
                    print('D',end="")
                    for space1 in range(0,j,1):
                        print(" ",end="Z")
                print()
            for i in range(n,-1,-1):
                for space in range(0,i,1):
                    print("*",end="")
                for j in range(i,-1,-1):
                    print("D",end="")
                    for space1 in range(j,-1,-1):
                        print(" ",end="Z")
                print()
            print()

            print("""*WELCOME TO AUTOMATED BILLING SYSTEM*
PLEASE ENTER THE VALUES ACCURATELY""")
            print()

#---------------------------------------------------------------------

    #DATE MODULE

            from datetime import datetime
            now=datetime.now()
            da_te=now.strftime("%d/%m/%y")
            print("BILL DATE:",da_te)

            print("UNIQUE ID: ",rd.randint(10000,999999))
#---------------------------------------------------------------------

            print("***************BILL***************")
            add1=str(input("PRODUCT ID           :   "))
            qty=int(input("NUMBER OF ITEMS      :   "))
            pr_p=float(input("PRICE PER ITEM       :   "))
            dis=float(input("DISCOUNT PERCENTAGE  :   "))
            tax=float(input("TAX PERCENTAGE       :   "))
            amt1=(qty*pr_p)
            dis_amt=((amt1*dis)/(100))
            sub_total=(amt1-dis_amt)
            tax_amt=((sub_total*tax)/100)
            total_amt=sub_total+tax_amt
            print("***************BILL***************")
            print("QUANTITY SOLD           :   ", qty)
            print("PRICE PER ITEM          :   ",pr_p)
            print("         --------------")
            print("AMOUNT                  :   ",amt1)
            print("DISCOUNT                :   ",dis_amt)
            print("         --------------")
            print("DISCOUNTED TOTAL        :   ",sub_total)
            print("TAX                     :   ",tax_amt)
            print("         --------------")
            print("TOTAL AMOUNT TO BE PAID :   ",total_amt)
            print("***************END***************")
            print("*HAVE A NICE DAY*")
            print("***************END***************")
            print()
            l2.append(total_amt)
            db.update({add1:[qty,total_amt]})
            n1=input("""PRESS 1 TO END: 
PRESS 2 TO CONTINUE: """)
            if n1=="1":
                break
            if n1=="2":
                continue
        print("****************END****************")

#---------------------------------------------------------------------

        if val_1==3:
            print("*THANKS FOR USING DIGIBIZ*")
            break
    print("****************END****************")

#---------------------------------------------------------------------

    for I in range(len(l7[-1])):
        for J in range(len(l7[-1][I])-1):
            emp.append((l7[-1][I][J]*l7[-1][I][J+1]))

#---------------------------------------------------------------------

    print("TOTAL SALE: ",sum(l2))
    print("TOTAL PURCHASE: ",sum(emp))
    print("REVENUE GENERATED: ",sum(l2)-sum(emp))
    print("REVENUE GENERATED = TOTAL SALE - TOTAL PURCHASE")


#---------------------------------------------------------------------

else:
    print("WRONG PASSWORD")
    
#---------------------------------------------------------------------


# In[ ]:




