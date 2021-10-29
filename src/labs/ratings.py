"""Restaurant rating lister."""


# put your code here


# define a function that accepts an input text file
# open the input file
# create an empty dictionary
# iterate through the input file
# define the line so that we can iterate through them
# define a delimiter of ":"
#Store restaraunt names as the key in our dictionary
# store ratings as the value for our keys
# put our dictionary items into a list
# sort the list
# iterate through the list
# return each item in the list in a sentence:
# "{restaraunt_name} is rated at {rating}."

def restaurant_ratings(filename):
    file = open(filename, "r")
    restaurant_dic = {}
    restaurant_list = []
    while True:
        line = file.readline().strip()
        if line == None or line == "": 
            break
        restaurant_rating = line.split(":")
        
        restaurant_dic[restaurant_rating[0]] = restaurant_rating[1]
        restaurant_list.append(restaurant_rating[0])
    
    restaurant_list.sort()
    print_restaurants(restaurant_dic, restaurant_list)
    
    while True:
        restaurant_input = input("Restaurant name: ")
        if restaurant_input == None:
            break
        rating_input = input("Rating: ")
        restaurant_dic[restaurant_input] = rating_input
        restaurant_list.append(restaurant_input) 
        restaurant_list.sort()
        print_restaurants(restaurant_dic, restaurant_list)



def print_restaurants(restaurant_dic, restaurant_list):
    for restaurant in restaurant_list:
        print(f'{restaurant} is rated at {restaurant_dic[restaurant]}')



restaurant_ratings("scores.txt")

        

