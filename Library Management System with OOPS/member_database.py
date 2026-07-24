from member import Member
def read():
    member_list=[]
    try:
        file = open("members.txt","r")
        for line in file:
            line = line.strip()
            if line=="":
                continue
            data = line.split(",")
            member = Member(data[0],data[1],data[2],data[3],data[4],data[5])
            member_list.append(member)
        file.close()
    except FileNotFoundError:
        pass
    return member_list
def save(member_list):
    file = open("members.txt","w")
    for member in member_list:
        file.write(member.mid+","+member.name+","+member.age+","+member.gender+","+member.phone+","+member.email+"\n")
    file.close()
def add(member_list,member):
    member_list.append(member)
def view(member_list):
    if len(member_list) == 0:
        print("No Member Available!..........")
    else:
        for member in member_list:
            member.display()
            print("**********")
def search(member_list,mid):
    for member in member_list:
        if member.mid == mid:
            return member
    return None
def update(member_list,mid):
    member = search(member_list,mid)
    if member:
        member.name = input("New Name: ")
        member.age = input("New Age: ") 
        member.gender = input("New Gender: ")
        member.phone = input("New Phone: ")
        member.email = input("New Email ID :")
        return True
    else:
        return False
def delete(member_list,mid):
    member = search(member_list,mid)
    if member:
        member.display()
        print("Member Deleted Successfully!..........")
        member_list.remove(member)
    else:
        print("No Member Found!..........")