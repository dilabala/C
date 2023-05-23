class Car:
    def __init__(self, brand, model, year, fuel_type, engine_displacement, horsepower, top_speed, acceleration, price, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.engine_displacement = engine_displacement
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.price = price
        self.mileage = mileage

    def calculate_average_fuel_consumption(self, distance_traveled, fuel_consumed):
        average_consumption = fuel_consumed / distance_traveled
        return average_consumption

    def start_engine(self):
        # Méthode pour démarrer le moteur
        pass

    def accelerate(self):
        # Méthode pour accélérer
        pass

    def brake(self):
        # Méthode pour freiner
        pass

    def park(self):
        # Méthode pour se garer
        pass
