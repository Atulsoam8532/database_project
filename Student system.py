import csv
import mysql.connector

my = mysql.connector.connect(host="localhost", user="root", password="Rajputana@8532",database="Hospital_management")

a = my.cursor()
#a.execute("CREATE TABLE Doctor_table(Name CHAR(50), Doctor_id INT(50),Hospital_name varchar(50),Joining_date varchar(50), Salary INT(50),Specialty Varchar(50), Experience varchar(50),Doctor_id varchar(50),CONSTRAINT FK_PersonOrder FOREIGN KEY (Hospital_id) REFERENCES doctor_table(Hospital_id)")
#a.execute("ALTER TABLE _table ADD COLUMN Hospital_Name varchar(50)")


def login():
    print("Want to login(1) or Register(2) :")
    lo = int(input())
    if lo == 1:
        print("You want ")
        u_name = input("Enter your UserName: \n")
        passw = input("Enter your password: \n")
        try:
            a.execute(f"SELECT * FROM login WHERE password = '{passw}' AND (User_name = '{u_name}'or Mobile_Number = '{u_name}')")
            r = bool(a.fetchall())

            if r == False:
                print("Invalid USERNAME and PASSWORD")
            else:
                print("You have successfully logged in")
                print("""
                        *==============================*
                        |     1.Update Patient Data    |
                        |     2.Update Doctor Data     |
                        *==============================*
                """)
                c = int(input("Enter [1 or 2]:\n"))
                if c == 1 or 2:
                    update()
                else:
                    print("Invalid Entry")
        except:
            print("invalid login")
    elif lo == 2:
        hos_id ="Atul_soam"
        count = 0
        while count <3:
            hosp = input("Enter Hospital ID: \n")
            if hosp != hos_id:
                count += 1
                print("Invalid Key")
                if count == 3:
                    print("ran out of chance Try again after some time")
            else:
                print("You have entered right key")
                break
        while True:
            try:
                name = input("Enter your name:\n")
                age = int(input("Enter your age:\n"))
                m_num = int(input("Enter your number:\n"))
                gen = input("Enter your Gender[Male/Female]:\n")
                uname = input("Enter Username:\n")
                while True:
                    passwor = input("Enter a strong password:\n")
                    if val_pass(passwor):
                        con = input("Please re-enter your password: ")
                        if con == passwor:
                            # !!!!!!!!!!!!!!!!!!!!!!
                            # code to add to dictionary goes here
                            # !!!!!!!!!!!!!!!!!!!!!!!
                            print("You've registered successfully!")
                            break
                        else:
                            print("[Error] : Passwords don't match!")
                X = "INSERT INTO login(Name,Age,Mobile_Number,Gender,User_name,Password)VALUE(%s,%s,%s,%s,%s,%s)"
                Y = (name,age,m_num,gen,uname,passwor)
                a.execute(X, Y)
                my.commit()
                break
            except:
                print("You Did something wrong!!!")
def val_pass(passwrd):
    # function to validate password

    spec, num, up, lo = False, False, False, False

    if len(passwrd) >= 8:
        for i in passwrd:
            if i in "~`!@#$%^&*()_-+={}[]|\\:;\"'<,>.?/":
                spec = True
            elif i in "1234567890":
                num = True
            elif i.isupper():
                up = True
            else:
                lo = True

        if all([spec, num, up, lo]):
            return True
        else:
            print("[Error] : Password is weak!")
            return False
    else:
        print("[Error] : Password too short!")


def patient():
    quan = int(input("How many patient you want to add : \n"))
    try:
        for i in range(quan):
            name = input("Enter your name : \n")
            bed = int(input("Enter your bed number: \n"))
            date = input("Enter Admit date : \n")

            id = int(input("Id\n"))
            hospital_name = input("Enter Hospital Name :\n")
            while True:
                try:
                    Hos_id = int(input("Enter Hospital Id : \n"))
                    x = "INSERT INTO patient_table(Id,Hospital_id,Name,Bed_Number,Admit_date,Hospital_Name) VALUE(%s,%s,%s,%s,%s,%s)"
                    y = (id,Hos_id,name, bed, date,hospital_name)
                    a.execute(x, y)
                    my.commit()
                    break
                except:
                    print("Invalid Hospital ID")

    except:
        print("You did something wrong!")
def Doctor():

    while True:
        try:
            d_name = input("Enter your Name: \n")
            d_id = input("Enter your ID :\n")
            h_name = input("Enter your Hospital Name :\n")
            Jo_da = input("Enter Joining Date :\n")
            salary = int(input("Enter the salary:\n"))
            special = input("Enter your specialty :\n")
            exp = input("Enter your experience Year: \n")
            try:
                hos_id = input("Enter Hospital ID: \n")
                x = "INSERT INTO doctor_table(Doctor_name,Doctor_id,Hospital_name,Joining_date,Salary,Specialty,Experience,Hospital_id) VALUE(%s,%s,%s,%s,%s,%s,%s,%s)"
                y = (d_name,d_id,h_name,Jo_da,salary,special,exp,hos_id)
                a.execute(x, y)
                my.commit()
                break
            except:
                print("Invalid Hospital ID")
        except:
            print("You did something wrong")
def update():
    while True:
        try:
            table = input("Enter the table you want to update:\n")
            req = input("What do you want to update: \n")
            req1 = input("Enter the Update: \n")
            if table == "patient_table":
                id = input("Select the ID: \n")
                upd = a.execute(f"UPDATE {table} SET {req} = '{req1}' WHERE id = {id}")
                my.commit()
                a.execute(f"SELECT * FROM {table}")
                r = a.fetchall()
                for i in r:
                    print(i)
                break
            elif table == "doctor_table":
                id = input("Enter the Doctor_ID: \n")
                upd = a.execute(f"UPDATE {table} SET {req} = '{req1}' WHERE doctor_id = {id}")
                my.commit()
                a.execute(f"SELECT * FROM {table}")
                r = a.fetchall()
                for i in r:
                    print(i)
                break
            else:
                print("Invalid Choice!")
        except:
            print("You did something wrong!")


def Show():
    while True:
        try:
            ch = int(input("Press 1 for all data press 2 for specify data :\n"))
            table = input("Enter the table you want to See:\n")
            if ch == 2:
                if table == "doctor_table":
                    id = input("Enter the row you want to see:\n")
                    a.execute(f"SELECT * FROM {table} where  doctor_id = '{id}'")
                    r = a.fetchall()
                    for i in r:
                        print(i)
                    break
                else:
                    id = input("Enter the row you want to see:\n")
                    a.execute(f"SELECT * FROM {table} where  id = '{id}'")
                    r = a.fetchall()
                    for i in r:
                        print(i)
                    break

            elif ch == 1:
                a.execute(f"SELECT * FROM {table} ")
                r = a.fetchall()
                for i in r:
                    print(i)
                break
            else:
                print("Enter valid Input!")
        except:
            print("you did something Wrong!")


print("               \n              ----- WELCOME_TO_HCL_HOSPITAL_SERVICES -----\n\n")

while True:

    print(""" 
             *----------------------------------------------------*

             -                1.SEE DOCTOR TABLE                  -

             -                2.SEE PATEINT TABLE                 -

             -                3.ADD DOCTOR                        -

             -                4.ADD PATEINT                       -
             
             -                5.Hospital Login                    -

             -                 6. Exit                             -
             *----------------------------------------------------*\n""")

    choice = int(input("ENTER YOUR CHOICE :_>__<_: "))

    if choice == 1:
        Show()
    elif choice == 2:
        Show()
    elif choice == 3:
        Doctor()
    elif choice == 4:
        patient()
    elif choice == 5:
        login()
    elif choice == 6:
        break
    else:
        print("\n INVALID  OPTION ")

