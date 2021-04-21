# DIP
# high level classes / modules should not depend on low level modules,
# they should depend on abstractions -> interfaces over direct implementations
from enum import Enum

class Relationship(Enum)
  PARENT = 0
  CHILD = 1
  SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

# low level module -> Relationships -> it handles the storage and "search&return"
class Relationships: 
    def __init__(self):
        self.relations = [] # this is the underlying issue - if you change the implementation
                            # of the relations storage (say change it from a list to a dict)
                            # then that would break the implementation of the lookup (line 34ff)

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

# high level module -> Research
class Research:
    def __init__(self, relationships): # one issue with the code is that it relies on the implementation of relations
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}.')


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

"""
In order to abide to the Dependency Inversion Principle we should define a visible interface (RelationshipLookup) 
that will lead to the lookup being part of the Relationship-class and thus freeing the developer from the need to know
how the lookup was implemented because they can depend on the interface.
"""

class RelationshipLookup:
    @abstractmethod
    def find_all_children_of(self, parent):
        pass

class ImprovedRelationships(RelationshipLookup):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, parent):
        for r in self.relations:
            if r[0].name == parent and r[1] == Relationship.PARENT:
                yield r[2]

class ImprovedResearch:
    def __init__(self, lookup):
        for child in lookup.find_all_children_of("John"):
            print(f"John has a child called {child}")

            
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = ImprovedRelationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

ImprovedResearch(relationships)
