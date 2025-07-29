
file = open("Fan.txt", 'w')        
file.write("HI HELLO")             
file.close()                      
print("Data is pushed successfully")  


file = open("Fan.txt", 'r')       
data = file.readlines()           
for i in data:                    
    print(i.split())              
file.close()                      
