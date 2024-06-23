class Person :
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hobbies = []


    def update_age(self, years):
        
        self.age = self.age + years
        return self.age
    
    def update_hobbies(self, activity):

        self.hobbies.append(activity)

    def total_hobbies(self):
        return len(self.hobbies)



newperson = input(f'Enter Person Name: ') 
person = Person(newperson)

while person.age > 0:
    
    print (f'Name: {person.name}\n')
    
    new_age = input(f"\n{person.name}\'s New Age: ")
    person.update_age(int(new_age))
    
    new_hobby = input(f'\nEnter the new hobby for {person.name}: ')
    person.update_hobbies(new_hobby)
    
    print(f'Age: {person.age}')
    print(f'Hobbies: {person.hobbies}')
    print(f'{person.name}\'s total hobbies: {person.total_hobbies()}\n')
    