class dog:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print(f"Name is :{self.name}")


class labrador(dog):
    def sound(self):
        print("Labrador woofs")


# multilvel inheritance 
class GuideDog(labrador):
    def guide(self):
        print(f"{self.name}Guides the way !!")


dog1 = GuideDog("jimmiy")
dog1.display_name()
dog1.sound()
