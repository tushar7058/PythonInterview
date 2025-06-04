
'''
Single inheritance : Child class inherit from single parent class.

'''

class hello:
    
    def babes(self):
        print("The name is Tushar kale")
    
    def name(self):
        print("This is Refers to the name -> ")



class hello1(hello):

    def sirname(self):
        print("This is going to print sirname of person.")



s = hello1() # creating object 
s.name() # acces the method through single inheritance from class 'hello'


