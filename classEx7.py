class JustCounter:
    __secretCount = 0
    #secretCount = 0
    def Count(self):
        self.__secretCount += 1
        #print (self.__secretCount)

Counter = JustCounter()
Counter.Count()
Counter.Count()
#print (Counter.__secretCount)

print (Counter._JustCounter__secretCount)

