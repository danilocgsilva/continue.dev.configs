from continue_dev_configs.Database import Database

my_expression = """
This is the first line
This is the second one
"""

class StringMaker:
    def execute(self):
        database = Database()
        database.create()
        print(my_expression)
