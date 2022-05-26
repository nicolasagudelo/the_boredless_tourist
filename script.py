# Author: Nicolas Agudelo
# Instructions for this project can be found at: https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-boredless-tourist/projects/the-boredless-tourist

# Global Variables

destinations = ['Paris, France', 'Shanghai, China','Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for destination in destinations]
attractions_with_interest = []

# Functions
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags: attractions_with_interest.append(possible_attraction[0])
    
    return attractions_with_interest

# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# print(get_destination_index('“Hyderabad, India”'))

# test_destination_index = get_traveler_location(test_traveler)

# print(test_destination_index)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)

la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)