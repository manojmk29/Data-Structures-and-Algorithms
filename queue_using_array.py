class queue:
    def __init__(self):
        self.arr=[]
        self.front=0
        self.rear=0
        self.size=0
        self.maxi=6
    def enque(self,ele):
        if(self.rear-self.front==self.maxi):
            print("overflow")
            return
        self.arr.append(ele)
        self.rear+=1
    def deque(self):
        if(self.front==self.rear):
            print("underflow")
            return
        ret=self.arr[self.front]
        self.front+=1
        return(ret)
    def que_len(self):
        return(self.rear-self.front)
    def pri_que(self):
        for i in range(self.front,self.rear):
            print(self.arr[i])
s=queue()
s.enque(1)
print("que--")
s.pri_que()
s.enque(2)
print("que--")
s.pri_que()
s.enque(3)
print("que--")
s.pri_que()
s.enque(4)
print("que--")
s.pri_que()
s.enque(5)
print("que--")
s.pri_que()
s.enque(6)
print("que--")
s.pri_que()
s.enque(7)
print("que--")
s.pri_que()
s.enque(8)
print("que--")
s.pri_que()
s.enque(9)
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
s.deque()
print("que--")
s.pri_que()
print("len==",s.que_len())