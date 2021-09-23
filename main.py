import sqlite3


db = sqlite3.connect("data.db")
c = db.cursor()

# Welcome Message
print("************************************************************")
print("================== BANK MANAGEMENT SYSTEM ==================")
print("************************************************************")
print("==========     [1] Balance                      ============")
print("==========     [2] Activity                     ============")
print("==========     [3] Deposit                      ============")
print("==========     [4] Withdraw                     ============")
print("==========     [5] Quit                         ============")
print("************************************************************\n")

 
while True:
    option = int(input("Option: "))

    if option == 1:
        with open("data/bank.txt", "r") as f:
            view = f.read()
        print(f"Your Balance: {view}")

    if option == 2:
        with open("data/logs.txt", "r") as f:
            data = f.read()
        print(data)            

    if option == 3:
        dep_amt = input("Enter Amount: ")
        if dep_amt == 0:
            print("[ERROR] | Deposit Failed!")
        else:
            with open("data/bank.txt", "w") as f:
                dep = f.write(dep_amt)
                print("[PROCESS] | Deposit Successful!")
                with open("data/logs.txt", "w") as f:
                    f.write(f"{dep_amt} | Deposit")
                 
    if option == 4:
        with_amt = int(input("Enter Amount: "))
        with open("data/bank.txt", "r") as f:
            data = f.read()

        if data == 0:
            print("[ERROR] | Withdrawl Failed!")
        if with_amt == 0:
            print("[ERROR] | Withdrawl Failed!")
        else:
            with open("data/bank.txt", "r") as f:
                data = f.read()
            
            data = int(data)
            final = with_amt - data
            final = str(final)
            with open("data/bank.txt", "w") as f:
                f.write(final)
            print("[PROCESS] | Withdrawl Successful!")    
            with open("data/logs.txt", "w") as f:
                f.write(f"{with_amt} | Withdrawl")


    if option == 5:
        break        

