class Box2D:
	def __init__(self, length,breadth):
		self.length=length
		self.breadth=breadth
	def surfacearea(self):
		print("The area is :",(self.length * self.breadth))

class Box3D(Box2D):
   def __init__(self):
       super().__init__(10,20)

       self.height=10

   def volume(self):
        print("The volume is :", (self.length * self.breadth * self.height))


if __name__ == "__main__":
    box = Box3D()
    box.volume()
    box.surfacearea()