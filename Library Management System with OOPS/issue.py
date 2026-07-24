class Issue:
    def __init__(self,iid,mid,bid,issdate,retdate,status):
        self.iid = iid
        self.mid = mid
        self.bid = bid
        self.issdate = issdate
        self.retdate= retdate
        self.status = status
    def display(self):
        print("Issue ID   :",self.iid)
        print("Member ID  :",self.mid)
        print("Book ID    :",self.bid)
        print("Issue Date :",self.issdate)
        print("Return Date:",self.retdate)
        print("Status     :",self.status)
        