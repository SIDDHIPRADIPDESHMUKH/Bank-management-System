class User():
    usercount=0

    def __init__(s,name,gender,salary):    #here __init__ constructor is use to initialize the attributes of class  User
        s.name=name
        s.gender=gender
        s.salary=salary
        User.usercount=User.usercount +1  #It increment usercount each time when new user is created.
        s.account_no=User.usercount

    def showdetails(s):
        print(f'Name: {s.name}\nGender: {s.gender}\nSalary: {s.salary}\nAccount no: {s.account_no}')

class Bank(User):     #class Bank inherite the properties of class User
    __bankname='SPD BANK'.center(50)
    __balance=0
    
    def __init__(s,name,gender,salary,pin):
        super().__init__(name,gender,salary)   # super() allows you to reuse and extend the functionality of the parent class.
        s.__balance=0
        s.__pin=pin

    def deposite(s,amount):
        s.amount=amount
        s.__balance=s.__balance+s.amount
        return f'Deposited amount: {s.amount}'

    def withdraw(s,amount):
        s.amount=amount
        if s.amount>s.__balance:
            return f'Insufficient balance, Current balance: {s.__balance}'
        elif s.amount>=100 and s.amount<=s.__balance:
            s.__balance=s.__balance-s.amount
            return f'Thank you for visiting, Current Balance: {s.__balance}'
        else:
            return f'Cannot withdraw less than Rs.100, Current Balance: {s.__balance}'

    def viewbalance(s):
        s.showdetails()
        return( f'Current Balance: {s.__balance}')

    def transfer(s,amt,user):
        s.amt=amt
        s.user=user
        if s.amt>s.__balance:
            return f'Insufficient Balance, Current Balance: {s.__balance}'
        elif s.amt>=1 and s.amt<=s.__balance:
            s.__balance=s.__balance-s.amt
            s.user.__balance=s.user.__balance+s.amt
            return f'Amount transfer successfully,Current Balance: {s.__balance}'
        elif s.amt<1:
            return f'you cannot transfer less than 1, Current balance: {s.__balance}'

    def change_pin(s,new_pin):
        s.__pin=new_pin

    def getusername(s):
        return s.name

    def getpin(s):
        return s.__pin

    def logindata(s):
        return [s.name,s.__pin]

users={}
while(True):
    print('Welcome to SPD BANK'.center(50))
    print('1.Create Account\n2.Login\n3.Exit')
    #Above menu is given where user can create account or login if have already created account 
    c=input('Enter your selection: ')

    if c=='1':
        while True:
            name=input('Enter your name: ')
            if name.isalpha():
                break
            print('Invalid username')
         #this will ensure the name contains alphabates only
        while True:
            gender=input('Enter your gender: ')
            if gender.isalpha():
                break
            print('Invalid')
        salary=int(input('Enter your salary: '))
        pin=input('Set your password: ')
        users[name]=Bank(name,gender,salary,pin)#here we update dict by adding key-name with values as name,pin of object define in class Bank
    elif c=='2':
        name=input('Enter your name: ')
        pin=input('Enter your password: ')
        obj=users.get(name,0)
        if obj==0:
            print('\nNo match found\n')
            continue 
        else:
            obj=users[name]  #here user can logged in if account is created
        data=obj.logindata() #create variable-data for that particular user having logindata
        if [name,pin] in [data]:
            
            print('\nAccess granted\n')
            while True:
                print('Menu:\n1.Check balance\n2.Deposite\n3.Withdraw\n4.Tranfer\n5.Change pin\n6.Logout')
                a=int(input('Enter your selection: '))
                if a==1:
                      print(obj.viewbalance())
                elif a==2:
                    
                    obj.amount=int(input('Enter amount to be deposited: '))
                    
                    print(f'{obj.deposite(obj.amount)}')
                    
                elif a==3:
                    obj.amount=int(input('Enter amount to be withdraw: '))
                    
                    print(f'{obj.withdraw(obj.amount)}')
                elif a==4:
                    amount=int(input('Enter amount to be transfer: '))
                    recipient=input('Enter recipient name: ')
                    recipient_user=users.get(recipient)
                    if recipient_user:
                        print(obj.transfer(amount,recipient_user))
                    else:
                        print('Recipient not found')
                elif a==5:
                    new_pin=input('Enter your new password: ')
                    obj.change_pin(new_pin)
                    print('Password changed successfully.')
                elif a==6:
                    print('Logging out')
                    break
                      
            
        else:
            print('Access denied')
    elif c=='3':
        break
    
        

