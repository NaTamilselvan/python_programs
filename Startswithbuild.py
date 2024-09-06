#i have a one string list its contain no of string list 
#To check each string start value is equal or not 


lst=["https://google.com ","http://yahoo.com","https.youtube.com"]


for i in lst:
    #THer is build in method
    if  i.startswith("https"):
         print(i)
        
