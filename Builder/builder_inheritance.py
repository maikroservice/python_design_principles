# builder inheritance
# what we have done before violated the open-close principle
# there is a different approach -> inheritance


class Person:
    def __init__(self):
        self.name = None
        self.job_title = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name}'s birthday is on {self.date_of_birth} and their job title is {self.job_title}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def work_as_a(self, position):
        self.person.job_title = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


personbuilder = PersonBirthDateBuilder()
person = (
    personbuilder.called("Simona").work_as_a("Developer").born("01.01.1970").build()
)

print(person)