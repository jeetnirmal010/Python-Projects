from transaction import Transact
from datetime import date

transaction_list =[]
def read():
    transaction_list=[]
    try:
        file = open("transactions.txt","r")
        for line in file:
            line = line.strip()
            if line =="":
                continue
            data = line.split(",")
            transaction = Transact(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            transaction_list .append(transaction)
        file.close()
    except FileNotFoundError:
        pass
    return transaction_list
def save(transaction_list):
    file = open("transactions.txt","w")
    for trasaction in transaction_list:
        file.write(str(trasaction.tid)+","+str(trasaction.tdate)+","+str(trasaction.accnum)+","+str(trasaction.particular)+","+str(trasaction.ttype)+","+str(trasaction.amt)+","+str(trasaction.bat)+","+"\n")
    file.close()
def view(transaction_list,accnum):
    print("====== Transaction History ======\n")
    print("Account Number:",accnum)
    for transaction in transaction_list:
        if accnum == transaction.accnum:
            transaction.display()
def search(transaction_list,tid):
    for transaction in transaction_list:
        if tid == transaction.tid:
            return True
    return False
def add(transaction_list,transaction):
    today = date.today()
    transaction.tdate = today
    transaction_list.append(transaction)