class stack:
    def __init__(self,maxi=None,arr=None):
        if(maxi is None):
            self.maxi=6
        else:
            self.maxi=maxi
        if(arr is None):
            self.arr=[]
        else:
            self.arr=arr
        self.top=len(self.arr)-1
    def pop(self):
        if(self.check_stack_underflow()):
            print("sorry the element cant be added because overflow")
        else:
            self.arr.pop()
            self.top-=1
    def push(self,ele):
        if(self.check_stack_overflow()):
            print("sorry the element cant be added because overflow")
        else:
            self.arr.append(ele)
            self.top+=1
    def check_stack_underflow(self):
        if(len(self.arr)==0):
            return(True)
        else:
            return(False)
    def check_stack_overflow(self):
        if(len(self.arr)==self.maxi):
            return(True)
        else:
            return(False)
    def top_pos(self):
        print("top is in",self.top)
    def pri_arr(self):
        return(self.arr)
s=stack(maxi=6,arr=[1,2,3])
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.pop()
s.pop()
s.pop()
s.pop()
print(s.pri_arr())