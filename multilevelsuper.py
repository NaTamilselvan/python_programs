class A:
    
    def fun(self):
        print('A')
        
      
class B(A):

    def fun(self):        
        print('B')
        
     
class C(B):

     def fun(self):
         super(B,self).fun()
         #internally means call parent of c fun mehtood super(c,self)
         print('c')
         
         







c=C()

c.fun()         