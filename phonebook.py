phone_book={}
pb1={'name':'x', 'Address':'Dhaka','Email':'x@gmail.com','Phone_no':['019000000', '0132232222']}
pb2={'name':'abv', 'Address':'Barishal','Email':'abv@gmail.com','Phone_no':['012000000', '0120111111']}
pb3={'name':'mns', 'Address':'Chittagong','Email':'tzx@gmail.com','Phone_no':['01711111', '011114557']}
list_conct=[pb1,pb2,pb3]
for i in range(1,len(list_conct)+1):
    phone_book[i]= list_conct[i-1]


#display all the contact in the phonebook
def display(phone_book):
    print('\n--------All the contact list--------')
    temp = len(phone_book)
    for key ,value in phone_book.items():
        print("Contact Number :",key)
        for k,v in value.items():
            print(k+": ",v)
        print('\n')
    menu()  


 #add new contact in the phonebook   
def add_user(phone_book):
    phone_books={}
    phone_no=[]
    phn_no=' '
    name =input("Please enter name: ")
    name = name.title()
    address =input("Please enter address: ")
    email =input("Please enter email: ")
    print("Please enter Phone no: ", end ='')
    while phn_no != '':
        phn_no = input()
        phone_no.append(phn_no)

    phone_books['Name']= name
    phone_books['Address']= address
    phone_books['Email']= email
    phone_books['Phone_no']= phone_no[:-1]
    temp = len(phone_book)
    phone_book[temp+2]= phone_books
    print("New contact added successfully!")
    store(phone_book)
    
    
    
#search for contact in contact list
def search(phone_book):
    
    found = False
    name=input("Enter name to search :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Found!')
                for i,j in phone_book[key].items():
                    print(i+": ",j)
                found =True
                menu()
        
    if found == False:
        print("There's no contact Record in Phone Book with name = " + name )
        msg = input("Do you Want to add new contact? [y or n]")
        msg=msg.lower()
        if msg == 'y':
            add_user(phone_book)
        else:
            menu()
            

#update contact in the phonebook
def update(phone_book):
    found = False
    name=input("Enter name to update :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Contact Found!')
                for i,j in phone_book[key].items():
                    print(i+": ",j)
                temp = input('\nWhat do you want to update?\n1.Name\n2.Address\n3.Email\n4.Phone no\n')
                if temp == '1':
                    new_name=input('Enter name :')
                    phone_book[key]['name']=new_name
                if temp == '2':
                    new_add=input('Enter address :')
                    phone_book[key]['Address']=new_add
                if temp == '3':
                    new_email=input('Enter Email :')
                    phone_book[key]['Email']=new_email
                if temp == '4':
                    phone_no=[]
                    phn_no=' '
                    print('Enter new Phone no :',end ='')
                    while phn_no != '':
                        phn_no = input()
                        phone_no.append(phn_no)
                    phone_book[key]['Phone_no']= phone_no[:-1]
                found =True
                store(phone_book)
                break
    
    if found == False:
        print("There's no contact Record in Phone Book with name = " + name )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            update(phone_book)
        else:
            menu()


#delete contact in the phonebook
def delete(phone_book):
    found = False
    t= 0
    name=input("Enter name to delete :")
    name=name.title()
    for key ,value in phone_book.items():
        for k in value.values():
            if(k==name):
                print('Found!')
                temp = input("Are you sure you want to delete? [Y or N] : ")
                temp=temp.title()
                if temp == 'Y':
                    t = key  
                found =True
            
    if t != 0:
        del phone_book[t]
        print('your Contact deleted successfully!')
        display(phone_book)
    if found == False:
        print("There's no contact Record in PhoneBook with name : " + name )
        msg = input("Want to try again? [y or n]")
        msg = msg.lower()
        if msg=='y':
            delete(phone_book)
        else:
            menu()

#save all the contact of Phonebook in a text file
def store(phone_book):
     with open("phonebook.txt", 'w') as p:
         for value in phone_book.values():
             p.write(str(value))
             p.write("\n")
     print( "All the contact saved successfully!")
     display(phone_book)


def menu():
    msg = '''\n   ---------- PhoneBook---------\n
          Enter key 1 for "Display All Contacts Records"\n 
          Enter key 2 for "Add a New Contact Record"\n
          Enter key 3 for "Search your contacts"\n
          Enter key 4 for "Update your contacts"\n
          Enter key 5 for "Delete your contacts"\n
          Enter key 6 for "Save your contacts"\n
          Enter key 7 for "Quit"\n'''
    print(msg)

    
#input choice call functions
    user_input = input("Enter your choice: ")
    if user_input == "1":
        display(phone_book)
        
    elif user_input == "2":
        add_user(phone_book)
        
    elif user_input == "3":
        search(phone_book)
        
    elif user_input == "4":
        update(phone_book)
        
    elif user_input == "5":
        delete(phone_book)
        
    elif user_input == "6":
        store(phone_book)
        
    elif user_input == "7":
        print("Welcome to the PhoneBook")

    else:
        print("Wrong choice, Please Enter [1 to 7]\n")
        temp = input("Press Enter to continue ...")
        menu()
menu()
