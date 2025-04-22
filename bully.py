def bully(ele):
    global co
   
    ele-=1
    co=ele+1
   
    print(f"Present Co-ordinator is {co}")
   
    hp=[]
    for i in range(ele+1,n):
        if status[i]==1:hp.append(i+1)
    if hp:
        print(f"p{ele+1} will send message to P{hp}")
       
        for i in range(ele+1,n):
            print(f"Message sent from p{ele+1} to {i+1}")
            if status[i]==1:
                print(f"OK message is sent from {i+1} to {ele+1}")
                bully(i+1)
    else:
        print("No greater process Present which is Active")    
   
   
   
   


n=int(input("Enter the Number of Process in the System"))
status=[1]*n
process=list(range(n))


co=0
cl=1


choice =True


print(f"Present Cordinator is P:{n}")


while choice:
    print("\n Choose An Option...")
    print(" choose 1 for crash a Process...")
    print(" choose 2 for recovering a Process...")
    print(" choose 3 for exit")
    ch=int(input(" >"))
   
    if ch==1:
        c=int(input("Enter the process to crash"))
        status[c-1]=0
        cl=1
        print(f"Process P{c} is Crashed ")
       
    elif ch==2:
        c=int(input("Enter the process to recover..."))
        status[c-1]=1
    elif ch==3:
        choice=False
        cl=0
    else:
        print("Invalid Option Selection")
   
    if cl==1:
        ele=int(input("Enter the intiator process: "))
        print('Election lgorithm Started....')
        bully(ele)
    print("Present Status is:")
    for i in range(0,n):
         print(f"P{i+1}: {status[i]}")
    print(f"Final Cordinator is P{co}")
   
       

