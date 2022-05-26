# Author: Nicolas Agudelo
# Instructions for this project can be found at: https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-boredless-tourist/projects/the-boredless-tourist

destinations = ['Paris, France', 'Shanghai, China','Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# print(get_destination_index('“Hyderabad, India”'))

test_destination_index = get_traveler_location(test_traveler)

print(test_destination_index)