#Python Program to validate an IP address using ReGex
#import re 
def g(ip):
    ip=str(input("Enter The IP  -- "))
    for x in range(255):
        for y in range(255):
            for z in range(255):
                for a in range(255):
                    b="%s.%s.%s.%s"%(x,y,z,a)
                    print(b)
                    if ip==b:
                        print("Valid")
                    else:
                        print("Not Valid")
ip="1.2.3.4"
print(g(ip))

                    
                    
#    c="[0-9]+.+[0-9]+.+[9-0]+.+[0-9]"
#    if re.match(c,e):
#        return True
#    return False
#e="1.1.1.1"
#print(g(e))  
 


       
    