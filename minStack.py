class MinStack(object):
    def __init__(self):
        self.arr=[]
        self.min=None
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(len(self.arr)==0):
            self.arr.append((val,val))
            self.min=val
        else:
            self.min=min(self.min,val)
            self.arr.append((val,self.min))
    def pop(self):
        """
        :rtype: None
        """
        if(len(self.arr)==0):
            return
        self.arr.pop()
    def top(self):
        """
        :rtype: int
        """
        if(len(self.arr)==0):
            return
        return(self.arr[-1][0])
    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.arr)==0):
            return
        return(self.arr[-1][1])
obj=MinStack()
print(obj.push(2147483646))
print(obj.push(2147483646))
print(obj.push(2147483647))
print(obj.top())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.push(2147483647))
print(obj.top())
print(obj.getMin())
print(obj.push(-2147483648))
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())