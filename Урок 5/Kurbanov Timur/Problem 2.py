class Bus:
    fuel_capacity = 1
    num_of_seats = 50
    mileage = 1
    cost = 1
    name = 1

    def any(self):
        any_cost = self.num_of_seats * 100
        return any_cost

    def bus(self):
        bus = int(self.any()) + int(self.any()/10)
        return bus

my_bus = Bus()

print("Плата за проезд по умолчанию для любого транспортного средства составляет: ", my_bus.any())
print("Общий тариф на автобус: ", my_bus.bus())
