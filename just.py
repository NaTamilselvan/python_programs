def interchange(a):
     
    temp=0
    temp=a[0]
    a[0]=a[-1]
    a[-1]=temp


def main():
    print("hello world")
    a=[10,20,30,40,50]
    interchange(a)
    print(a)




if __name__=="__main__":
   main()
