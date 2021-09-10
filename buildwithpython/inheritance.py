class UniversityPeople:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullname(self):
        print(self.fname + " " + self.lname)

class Students(UniversityPeople):
    pass
class Teachers(UniversityPeople):
    def __init__(self, fname, lname, email,salary):
        super().__init__(fname,lname,email) # super() use for get information from parent class
        self.salary=salary
student1=Students("Vishwa","Praveen","vishwapraveen4618@gmail.com")
student2=Students("Chathun","Janeesha","chathunjaneesha30145@gmail.com")
englsh_teacher=Teachers("Upali","Hapuarachchi","upalihapu@gmail.com","9700 USD")

englsh_teacher.fullname()
student2.fullname()
print(student1.fname)
print(englsh_teacher.salary)

print("")
#nested inheritance
class math_teacher(Teachers): # this class is inherited to teachers so it also inherited to uniersitypeople class
    pass
#checking whether an instance belong to a class or not
print(isinstance(student1,Students))

#checking whether a sub class belong to a parent class or not
print(issubclass(Students,UniversityPeople))

print(" ")
#polymorphism
#In Python, Polymorphism lets us define methods in
# the child class that have the same name as the methods in the parent class.

for people in (student1,student2,englsh_teacher): #polymorphism use in methods
    people.fullname()
#polymorphism use in functions
def printfirstname(name):
    print(name.fname)

print("")
printfirstname(student1)
printfirstname(student2)
printfirstname(englsh_teacher)



































































































































































































































































































































































































































































































































