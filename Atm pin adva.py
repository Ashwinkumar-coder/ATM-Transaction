a=open("D:\FULLSTACK\PYTHON\generate\pin.txt","r")
c=a.read()
pin=int(c)
b=open("D:\FULLSTACK\PYTHON\generate\mainbalance.txt","r")
d=b.read()
mainbalance=int(d)
while(True):
    print("1.withdraw\n2.deposit\n3.balance\n4.exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        yourpin=int(input("Enter your pin"))
        if(pin==yourpin):
            withdraw=int(input("Enter your withdraw amount:"))
        else:
            print("invalid pin")
            break
        if(withdraw>0 and withdraw<=mainbalance):
            print("Take your cash")
            mainbalance=mainbalance-withdraw
            h=str(mainbalance)
            s=open("D:\FULLSTACK\PYTHON\generate\mainbalance.txt","r+")
            t=s.write(h)
            s.close()
            print("After withdraw , mainalance")
            print(mainbalance)
           
        else:
                print("insufficient amount")
    elif(choice==2):
        deposit=int(input("Enter your deposit amount"))
        if(deposit>0):
            mainbalance=mainbalance+deposit
            h=str(mainbalance)
            s=open("D:\FULLSTACK\PYTHON\generate\mainbalance.txt","r+")
            t=s.write(h)
            s.close()
            print("mainbalance after deposit:",mainbalance)
    elif(choice==3):
        print("current mainbalance after deposit:",mainbalance)

    elif choice==4:
        print("Thanks for visiting ATM")
        break        
    else:
        print("Invalid option")
        
    
        
        
    
