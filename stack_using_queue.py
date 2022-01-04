class queue:
    def __init__(self):
        self.arr=[]
        self.front=0
        self.rear=0
    def enque(self,ele):
        self.arr.append(ele)
        self.rear+=1
    def deque(self):
        if(self.rear==self.front):
            return(None)
        ret=self.arr[self.front]
        self.front+=1
        return(ret)
    def ret_rear(self):
        if(self.rear==self.front):
            return(None)
        else:
            return(self.arr[self.front-1])
    def que_len(self):
        return(self.rear-self.front)
            
class MyStack(object):

    def __init__(self):
        self.q1=queue()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q2=queue()
        q2.enque(x)
        n=self.q1.que_len()
        while(n>0):
            q2.enque(self.q1.deque())
            n-=1
        self.q1=q2
        
    def pop(self):
        """
        :rtype: int
        """
        return(self.q1.deque())

    def top(self):
        """
        :rtype: int
        """
        return(self.q1.ret_rear())

    def empty(self):
        """
        :rtype: bool
        """
        if(self.q1.rear==self.q1.front):
            return(True)
        else:
            return(False)
s=MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
