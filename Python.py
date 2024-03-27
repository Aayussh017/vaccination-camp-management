import csv
import os

def files():
    f=open("D:/Vaccinationcamp.csv",'w',newline="")
    ob=csv.writer(f)
    while True:
        No=input('Enter Children Number : ')
        name=input('Enter Children Name : ')
        Vac=input('Enter Vaccine Name : ')
        age=input('Enter Age of Child : ')
        con=input('Enter Parents Contact Number : ')
        l=[No,name,Vac,age,con]
        ob.writerow(l)
        fn=input('Would you like to continue =====> Y/N ')
        if(fn=='N' or fn=='n'):
            break
    f.close()

def show():
    with open('D:/Vaccinationcamp.csv','r') as f:
        ob=csv.reader(f)
        for i in ob:
            print(i)

def find():
    ad=input('Enter Parents Contact Number => ')
    with open('D:/Vaccinationcamp.csv','r') as f:
        ob=csv.reader(f)
        for i in ob:
            if i[4]==ad:
                print(i)
                break
            else:
                print('Contact not found ')

def remove():
    ad=input("Enter Children Number You Want To Delete ")
    with open('D:/Vaccinationcamp.csv','r') as f:
        l=csv.reader(f)
        t=open("D:/xxx.csv",'a',newline='')
        ob=csv.writer(t)
        for i in l:
            if(i[0]==ad):
                print("Deleted",i)
            else:
                ob.writerow(i)
        t.close()
    os.remove("D:/Vaccinationcamp.csv")
    os.rename("D:/xxx.csv","D:/Vaccinationcamp.csv")

def update():
    ad=input("Enter Children No. to be updated :")
    with open('D:/Vaccinationcamp.csv','r') as f:
        l=csv.reader(f)
        t=open('D:/xxx.csv','w',newline='')
        ob=csv.writer(t)
        for i in l:
            if(i[0]==ad):
                print('Previous data is ',i)
                i[0]=input("Enter Updated Children Number ")
                i[1]=input("Enter Updated Name of children => ")
                i[2]=input("Enter Updated Vaccine Name => ")
                i[3]=input("Enter Updated Age of Children => ")
                i[4]=input("Enter Updated Parent Contact Number => ")
            ob.writerow(i)
        t.close()
    os.remove("D:/Vaccinationcamp.csv")
    os.rename("D:/xxx.csv","D:/Vaccinationcamp.csv")

while True:
    print('*'*80)
    print(' '*10,'\  / |~\   |~~  |~~  ~|~  |\ | |~\  ~|~ ~|~ |~| |\ |')
    print(' '*10,' \/  |--\  |__  |__  _|_  | \| |~~\  |  _|_ |_| | \|')
    print("*"*80)
    print("PRESS 1 : Add New Children ")
    print("PRESS 2 : Display all Children Data ")
    print("PRESS 3 : Search Children Data ")
    print("PRESS 4 : Delete Children Data  ")
    print("PRESS 5 : Update Children Data  ")
    print("PRESS 6: Exit ")
    print('*'*80)
    ab=int(input("Enter your choice...."))

    if ab==1:
        files()
    elif ab==2:
        show()
    elif ab==3:
        find()
    elif ab==4:
        remove()
    elif ab==5:
        update()
    elif ab==6:
        print("Thankyou Visit Again",chr(3)*5)
        break
    else:
        print('Please Check The Number ')






            
        
