#IP1 Sannidhya and K
print("****BANK TRANSACTION****")
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="#1sannidhya1801")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
#creating required tables 
mycursor.execute("create table if not exists bank_acc(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date ,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
while(True):
    
    print("1=Create account")
    print("2=Deposit money")
    print("3=Withdraw money")
    print("4=Display account")
    print("5=Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number:"))
        name=input("Enter name(limit 35 characters):")
        city=str(input("Enter city name:"))
        mobileno=str(input("Enter mobile no.:"))
        balance=0
        mycursor.execute("insert into bank_acc (acno,name,city,mobileno,balance)values('{}','{}','{}','{}','{}')'".format('1234','sedwf','Delhi','78393839',0)
        mydb.commit()
        print("Account is successfully created!!!")
