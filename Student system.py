import csv
import mysql.connector

my = mysql.connector.connect(host="localhost", user="root", password="Rajputana@8532",database="Hospital_management")

a = my.cursor()
#a.execute("CREATE TABLE Doctor_table(Name CHAR(50), Doctor_id INT(50),Hospital_name varchar(50),Joining_date varchar(50), Salary INT(50),Specialty Varchar(50), Experience varchar(50),Doctor_id varchar(50),CONSTRAINT FK_PersonOrder FOREIGN KEY (Hospital_id) REFERENCES doctor_table(Hospital_id)")
#a.execute("ALTER TABLE _table ADD COLUMN Hospital_Name varchar(50)")


def patient():
    quan = int(input("How many patient you want to add : \n"))

    for i in range(quan):
        name = input("Enter your name : \n")
        bed = int(input("Enter your bed number: \n"))
        date = input("Enter Admit date : \n")
        Hos_id = int(input("Enter Hospital Id : \n"))
        id = int(input("Id\n"))
        hospital_name = input("Enter Hospital Name :\n")
        x = "INSERT INTO patient_table(Id,Hospital_id,Name,Bed_Number,Admit_date,Hospital_Name) VALUE(%s,%s,%s,%s,%s,%s)"
        y = (id,Hos_id,name, bed, date,hospital_name)
        a.execute(x, y)
        my.commit()
def Doctor():
    quant = int(input("How much doctor you want to add: \n"))
    for i in range(quant):
        d_name = input("Enter your Name: \n")
        d_id = input("Enter your ID :\n")
        h_name = input("Enter your Hospital Name :\n")
        Jo_da = input("Enter Joining Date :\n")
        salary = int(input("Enter the salary:\n"))
        special = input("Enter your specialty :\n")
        exp = input("Enter your experience Year: \n")
        hos_id = input("Enter Hospital ID: \n")
        x = "INSERT INTO doctor_table(Doctor_name,Doctor_id,Hospital_name,Joining_date,Salary,Specialty,Experience,Hospital_id) VALUE(%s,%s,%s,%s,%s,%s,%s,%s)"
        y = (d_name,d_id,h_name,Jo_da,salary,special,exp,hos_id)
        a.execute(x, y)
        my.commit()
def update():
    while True:
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


def Show():

    ch = int(input("Press 1 for all data press 2 for specify data :\n"))
    table = input("Enter the table you want to update:\n")
    if ch == 2:
        id = input("enter the row you want to see:\n")
        a.execute(f"SELECT * FROM {table} where  doctor_id = '{id}'")
        r = a.fetchall()
        for i in r:
            print(i)

    elif ch == 1:
        a.execute(f"SELECT * FROM {table} ")
        r = a.fetchall()
        for i in r:
            print(i)


    else:
        print("Enter valid Input!")


print("               \n              ----- WELCOME_TO_HCL_HOSPITAL_SERVICES -----\n\n")

while True:

    print("""         *----------------------------------------------------*

             -                1.SEE DOCTOR TABLE                  -

             -                2.SEE PATEINT TABLE                 -

             -                3.ADD DOCTOR                        -

             -                4.ADD PATEINT

             -                5.   EXIT                           -

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

        break

    else:

        print("\n INVALID  OPTION ")












