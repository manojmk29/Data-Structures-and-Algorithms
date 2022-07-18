file2 = open(r"customer.txt","w+")

def create_user():
        name=input("enter the name")
        num=input("enter the number")
        cname=name[:3]+num[-2:]
        pwd="srec"
        user[cname]=pwd
def all_user(self):
    for i in self.user:
        print("name==",i)
def day_cal(self):
    u_name=input("enter the username")
    days=input("enter the number of days user stayed")
    if u_name not in self.user:
        print("the given username is not present")
    else:
        self.day[u_name]=days

def cal_cost(self):
    u_name=input("enter the username")
    if u_name not in self.user:
        print("the given username is not present")
        return 0
    else:
        days=int(self.day[u_name])
        gst=0.18
        tot=days*1000
        tot+=(gst*tot)
        return tot