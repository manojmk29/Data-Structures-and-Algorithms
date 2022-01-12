class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self,cap):
        self.head=None
        self.tail=None
        self.length=0
        self.cap=cap
    def append_left(self,node):
        if(self.head is None):
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.head.prev=None
        self.length+=1
        self.check()
    def check(self):
        if(self.length>self.cap):
            temp=self.tail.prev
            temp.next=None
            self.tail=temp
            self.length-=1
    def delete_node(self,node):
        if(node.prev==None):
            temp=node.next
            temp.prev=None
            self.head=temp
        elif(node.next==None):
            temp=node.prev
            temp.next=None
            self.tail=temp
        else:
            prev_node=node.prev
            next_node=node.next
            prev_node.next=next_node
            next_node.prev=prev_node
        node.val=-1
        self.length-=1
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hmap={}
        self.dll=dll(capacity)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value=self.hmap[key].val
        self.dll.delete_node(self.hmap[key])
        self.hmap[key]=node(value)
        self.dll.append_left(self.hmap[key])
        return(value)
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hmap:
            self.dll.delete_node(self.hmap[key])
            self.hmap[key]=node(value)
            self.dll.append_left(self.hmap[key])
        else:
            self.hmap[key]=node(value)
            self.dll.append_left(self.hmap[key])
            
o=LRUCache(2)
o.put(1,1)
o.put(2,2)
print(o.get(1))
o.put(3,3)       
print(o.get(2))
o.put(4,4)    
print(o.get(1))
print(o.get(3))
print(o.get(4))
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)