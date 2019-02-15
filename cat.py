class Cat:

    """ A class representing a felis catus (domestic cat) """

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return "Cat: {}".format(self.name)

    def eats_at(self):
        # time string
        time_am_pm = None
        # numbers 1 to 11
        # 1 for 1 AM, 2 for 2 AM, and so forth
        if self.meal_time in range(1,12):
            time_am_pm = "{} AM".format(self.meal_time)
        # numbers 13 to 23
        # 13 for 1 PM, 14 for 2 PM and so forth
        elif self.meal_time in range(13,24):
            time_am_pm = "{} PM".format(self.meal_time - 12)
        # special case
        elif self.meal_time == 0:
            time_am_pm = "12 AM"
        # special case
        elif self.meal_time == 12:
            time_am_pm = "12 PM"

        return time_am_pm

    def meow(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preferred_food, self.eats_at())

# 2 cats (instances of the Cat class) created
saba = Cat("Saba", "chicken", 7)
moris = Cat("Moris", "tuna", 12)
print(saba)
print(moris)

# testing the .eats_at() instance method
print()
print(saba.eats_at())
print(moris.eats_at())

# testing out the .meow() instance method
print()
print(saba.meow())
print(moris.meow())
