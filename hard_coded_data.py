from data_models import Destination

all_trip_categories = ['Destination', 'Transportation', 'Restaurant', 'Entertainment']

all_transportations = ['train', 'car', 'bus', 'boat', 'airplane']

all_destinations = []
all_destinations.append(Destination('the Wisconsin Dells',
    ['Paul Bunyan', 'Dells Pizza Lab', 'Triple Play', 'High Rock Cafe', 'Monk\'s'],
    ['go rock climbing', 'go hiking', 'visit a water park', 'go camping', 'go kayaking']))
all_destinations.append(Destination('Chicago', 
    ['Gino\'s East', 'The Purple Pig', 'Luella\'s Southern Kitchen','Jade Court', 'Kasama'],
    ['visit the Aquarium', 'watch the Chicago Marathon', 'visit the Bean', 'visit the Planetarium','visit the Field Museum']))
all_destinations.append(Destination('New York City',
    ['Famous Amadeus Pizza', 'Olio e Piu', 'Bleeker Street Pizza', 'Boucherie West Village', 'Spot Dessert Bar'],
    ['watch a Broadway play', 'visit the Museum of Modern Art','watch the NYC marathon', 'visit Central Park', 'visit Times Square']))
all_destinations.append(Destination('Phoenix',
    ['Breakfast Club', 'Cornish Pasty Company', 'CiBO', 'The Churchill', 'Monroe\'s Hot Chicken'],
    ['go for a desert hike','visit the Archeological Park','go for a trail ride', 'visit the Musical Instrument Museum','visit the nature preserve']))
all_destinations.append(Destination('Salt Lake City',
    ['Tamarind', 'The Bayou', 'Sapa Sushi Bar', 'La-Cai Noodle House', 'Guras Spice House'],
    ['visit the USA Climbing Team gym','go rock climbing', 'go hiking', 'vist the Planetarium', 'vist the Natural History Museum']))