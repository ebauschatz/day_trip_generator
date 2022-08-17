class Destination:
    def __init__(self, name, restaurants, entertainments):
        self.name = name
        self.restaurants = restaurants
        self.entertainments = entertainments

class Trip:
    def __init__(self, destination, transportation, restaurant, entertainment):
        self.destination = destination
        self.transportation = transportation
        self.restaurant = restaurant
        self.entertainment = entertainment