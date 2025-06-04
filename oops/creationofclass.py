# Defines with class keyword

class Dog:
    species = "Animal" 
    '''
        Here name is Class attribute 
        attribute-> varible inside the class
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def barking(self):
        print("The Dog is barking")


dog1 = Dog("Tushar",22) # creating object 
dog2 =Dog("Mayur",24)
print(dog2.name)
dog1.barking()

# updating name
print("going to update instance var name !! ")
dog1.name = "Max"
print(dog1.name)


