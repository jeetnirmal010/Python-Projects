class Transact:
    def __init__(self,tid,tdate,accnum,particular,ttype,amt,bat):
        self.tid = tid
        self.tdate = tdate
        self.accnum = accnum
        self.particular = particular
        self.ttype = ttype
        self.amt = amt
        self.bat = bat
    def display(self):
        print(self.tid,"    ",self.tdate,"    ",self.particular,"    ",self.amt,"    ",self.ttype,"    ",self.bat)