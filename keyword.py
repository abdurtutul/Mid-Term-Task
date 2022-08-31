class dictionary:
    def __init__(self):
        while True:
            print("Choose an option:")
            print("1. Insert a dictionary.")
            print("2. Update a dictionary.")
            print("3. Delete a dictionary.")
            print("4. Search a dictionary.")
            print("5. Display")
            print("6. Exit")

            choice = int(input("Enter a number(1-6) to begin:"))

            if choice == 1:
                self.insert()
            elif choice == 2:
                self.update()
            elif choice == 3:
                self.delete()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.display()
            else:
                break

#Function of insert 
    def insert(self):
        while True:
            try:
                dictionary = input("Enter a dictionary:")
                description = input("Enter description of the dictionary:")

                class_dict = {}
                class_dict[dictionary] = description

                with open("C:\\Users\\User\\Desktop\\dictionary.txt", 'a') as file_object:
                    file_object.write(f"{class_dict}")
                    file_object.write(f" \n")
                break
            except:
                print("Unexpected error!")
                break
#Function of update
    def update(self):
        with open("C:\\Users\\User\\Desktop\\dictionary.txt", 'r+') as file_object:
            search = input("dictionary you want to update:")
            str = ' '
            while(str):
                str = file_object.readline()
                linelist = str.split(" , ")
                if len(str)> 0:
                    if linelist[0] == "Name:"+search:
                        dictionary = input("Enter a dictionary:")
                        description = input("Enter description of the dictionary:")

                        class_dict = {}
                        class_dict[dictionary] = description
                        file_object.write(f"{class_dict}")

            else:
                print("No data found!")
#Function of search
    def search(self):
        with open("C:\\Users\\User\\Desktop\\dictionary.txt", 'r') as file_object:
            search = input("dictionary  want to search:")
            for i in file_object:
                if search in i:
                    print(i)
#function of Delete
    def delete(self):
        with open('C:\\Users\\User\\Desktop\\dictionary.txt', 'r') as file_object:
            lines = file_object.readlines()

            search = input("Enter a dictionary  want to delete:")

            with open('C:\\Users\\User\\Desktop\\dictionary.txt', 'w') as file_object:
                for line in lines:
                    if line.find(f"{search}") == -1:
                        file_object.write(line)
        print("Deleted")
#Function of display
    def display(self):
        with open("C:\\Users\\User\\Desktop\\dictionary.txt", 'r') as file_object:
            dict = file_object.read()
        print(dict)
        

test = dictionary()