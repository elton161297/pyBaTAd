#convert two list into single dict
a=[1,2,3]
b=['krishna','praveen','rre']
#{1:'krishna',2:'praveen',3:'rre'}
c=dict(zip(a,b))
print(c)