class bicycle:
    myvalue = 1
    def pedal(self):
        print("helps the bicycle to move forward")
    def gears(self):
        print("the engine of the bicycle")
    def handles(self):
        print("helps us to control the bicycle")
    def incrementvalue(self):
        myvalue = 0
        myvalue = myvalue + 1
        print("myvalue is : " , (myvalue))
        print("self.myvalue is : ", (self.myvalue))

        
x = bicycle()
x.incrementvalue()
x.myvalue = 41
x.incrementvalue()
x.pedal()
x.gears()
x.handles()

y = bicycle()
y.incrementvalue()
        
        
