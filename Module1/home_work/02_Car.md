'''
class Car:

    def __init__(self, gas, capacity, gas_per_km, race=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.race = race
        self.current_gas_per_km = gas_per_km

    def fill(self, litres):
        if litres > (self.capacity - self.gas):
            self.gas = self.capacity
            print('There is not enough space')
        else:
            self.gas += litres
    
    def ride(self, distance):
        max_distance = self.gas / self.current_gas_per_km
        real_distance = (max_distance, distance)[distance < max_distance]
        self.gas -= self.current_gas_per_km * real_distance
        self.update_gas_per_km()
        print(f'We have drove {real_distance} km')

    def update_gas_per_km(self):
        # Я предположила, что механизм будет подобен начислению сложных процентов
        self.current_gas_per_km = self.gas_per_km * (1.05 ** (self.race / 1000))
'''
