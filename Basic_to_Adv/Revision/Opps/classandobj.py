class Human:
    
    def __init__(self,color,height):
        self.color=color
        self.height=height
        print("running")
        print(color)
    def walk(self):
        print("Walking")
    def run(self):
        print("running")

h1=Human("white",9876)  
h1.walk()
h1.run()

