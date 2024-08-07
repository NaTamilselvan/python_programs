def AmstrongNumber(num):
       
        k=num
        sum=0
        n=len(str(num))
        print(n)
        while num>0 :
                    num2=num%10
                    print("num2 is ",num2)
                    sum=sum+(num2*num2*num2)
                    num=num//10
        if sum==k :
            print(k,"THis number is amstrong number ")
        else:
            print(k,"This  number is  not amstrong number ")
def main():
      
       r=int(input("enter the number"))
       AmstrongNumber(r)



if __name__=="__main__":
                main()


