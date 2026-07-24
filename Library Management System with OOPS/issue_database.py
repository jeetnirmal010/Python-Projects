from issue import Issue
def read():
    issue_list =[]
    try:
        file = open("issue.txt","r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            data = line.split(",")
            issue = Issue(data[0],data[1],data[2],data[3],data[4],data[5])
            issue_list.append(issue)
        file.close()
    except FileNotFoundError:
        pass
    return issue_list
def save(issue_list):
    file = open("issue.txt","w")
    for issue in issue_list:
        file.write(issue.iid+","+issue.mid+","+issue.bid+","+issue.issdate+","+issue.retdate+","+issue.status+"\n")
    file.close()
def add(issue_list,issue):
    issue_list.append(issue)
def view(issue_list):
    if len(issue_list) == 0:
        print("Nothing Issue!...")
    else:
        for issue in issue_list:
            issue.display()
def search(issue_list,iid):
    for issue in issue_list:
        if issue.iid ==iid:
            return issue
    return None
def update(issue_list,iid):
    issue = search(issue_list,iid)
    if issue:
        issue.mid = input("New Member ID: ")
        issue.bid = input("New Book ID: ")
        issue.issdate = input("New Issue Date: ")
        issue.retdate = input("New Return Date: ")
        issue.status = input("New Status: ")
        print("Updated Successfully!..........")
    else:
        print("No Record Found!......")
def delete(issue_list,iid):
    issue = search(issue_list,iid)
    if issue:
        issue.display()
        print("Deleted Successfully!")
        issue_list.remove(issue)
    else:
        print("No Record Found!......")