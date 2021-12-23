class heap:
    def __init__(self):
        self.arr=[]
        self.len=0
    def swap(self,a,b):
        self.arr[a],self.arr[b]=self.arr[b],self.arr[a]
    def check(self,child,parent):
        if(self.arr[child]>self.arr[parent]):
            return(False)
        return(True)
    def swapping(self,node):
        if(node==0):
            return
        parent=(node-1)//2
        if(self.check(node,parent)==True):
            return
        else:
            self.swap(node,parent)
            self.swapping(parent)
    def insert(self,number):
        self.arr.append(number)
        self.len+=1
        node=len(self.arr)-1
        self.swapping(node)
    def printheap(self):
        print(self.arr[:self.len])
    def printfullheap(self):
        print(self.arr)
    def swappingdown(self,node):
        left=(node*2)+1
        right=(node*2)+2
        maxv=node
        if(node>=(self.len//2)+1):
            return
        if(left<self.len and self.arr[left]>self.arr[node]):
            maxv=left
        if(right<self.len and self.arr[right]>self.arr[maxv]):
            maxv=right
        if(maxv!=node):
            self.swap(node,maxv)
            self.swappingdown(maxv)
    def deletenode(self):
        self.swap(0,self.len-1)
        self.len-=1
        self.swappingdown(0)
obj=heap()
obj.insert(9)
obj.insert(10)
obj.insert(18)
obj.insert(20)
obj.insert(5)
obj.insert(28)
obj.insert(30)
obj.insert(53)
obj.insert(50)
obj.printheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()
obj.deletenode()
obj.printfullheap()