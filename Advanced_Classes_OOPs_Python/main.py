class Institute:
    def __init__(self, *teachers):
        # self.strength = strength
        self.teachers = teachers

    def show_teachers(self):
        print(self.teachers)

teachers = input(">").split(',')
print(teachers)
school1 = Institute(teachers,)
school1.show_teachers()
