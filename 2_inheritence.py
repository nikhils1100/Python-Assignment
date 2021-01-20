from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, gender):
        self.gender = gender
        super().__init__()

    @abstractmethod
    def get_gender(self):
        pass

class Male(Person):
    gender = 'male'

    def __init__(self):
        super().__init__(self.gender)

    # Commenting out this method will throw error
    def get_gender(self):
        print('Male')

class Female(Person):
    gender = 'female'

    def __init__(self):
        super().__init__(self.gender)

    # Commenting out this method will throw error
    def get_gender(self):
        print('Female')

m = Male()
f = Female()

m.get_gender()
f.get_gender()