# if you need more than one builder to build
# an object because it is so complex, you can
# use a facet


class Person:
    def __init__(self, name="John Doe"):
        self.name = name
        self.street = None
        self.zipcode = None
        self.city = None
        self.country = None

        self.company = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            + f"Address: {self.street}, {self.zipcode}, {self.city} in {self.country} \n"
            + f"Working at: {self.company} as {self.position} making ${self.annual_income} per year"
        )


# builder for person
class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    def create(self):
        return self.person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


# we also need an address builder
class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street):
        self.person.street = street
        return self

    def with_zipcode(self, zipcode):
        self.person.zipcode = zipcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

    def in_country(self, country):
        self.person.country = country
        return self


personbuilder = PersonBuilder()
person = (
    personbuilder.lives.at("123 Way of ways")
    .in_city("Munich")
    .in_country("Germany")
    .with_zipcode("12345")
    .works.at("Celonis")
    .as_a("Partner Manager")
    .earning(123456)
    .create()
)

print(person)