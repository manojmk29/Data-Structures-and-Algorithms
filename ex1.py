class ex1:
    ab=0
    def __init__(self):
        self.a=0
    def inc(self,cls):
        self.a+=1
        cls.ab+=1
    def pri(self):
        print(self.a)
obj1=ex1()
obj2=ex1()
obj1.inc()
obj1.inc()
obj1.pri()
obj2.pri()