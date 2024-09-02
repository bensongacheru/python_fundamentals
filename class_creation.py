class Car:
    def __init__(self, make, model, year):
        """Initializes a Car instance with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Prints the car's information."""
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")