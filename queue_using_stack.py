class stack:
    def __init__(self):
            self.arr=[]
            self.top=-1
    def pop(self):
        if(self.check_stack_underflow()):
            return(None)
        else:
            self.top-=1
            return(self.arr.pop())
    def push(self,ele):
        self.arr.append(ele)
        self.top+=1
    def check_stack_underflow(self):
        if(self.top==-1):
            return(True)
        else:
            return(False)
    def top_pos(self):
        return(self.top)
    def top_pos_val(self):
        if(self.top==-1):
            return(None)
        else:
            return(self.arr[self.top])
class MyQueue:
    def __init__(self):
        self.s1=stack()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        temp=stack()
        while((self.s1.top_pos())>-1):
            temp.push(self.s1.pop())
        temp.push(x)
        while((temp.top_pos())>-1):
            self.s1.push(temp.pop())   
    def pop(self):
        """
        :rtype: int
        """
        return(self.s1.pop())

    def peek(self):
        """
        :rtype: int
        """
        return(self.s1.top_pos_val())

    def empty(self):
        """
        :rtype: bool
        """
        if(self.s1.top_pos()==-1):
            return(True)
        else:
            return(False)
m1=MyQueue()
print(m1.empty())