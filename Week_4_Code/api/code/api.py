from flask import Flask, redirect, url_for, request
import random
import json
import os

app = Flask(__name__)

@app.route('/meal')
def get_meal_recommendation():
    meal_recommendation = [
        {"Name": "PUPU PLATTER: 2 ahi poke bombs, 4 coconut shrimp, 2 sticky ribs, 4pc California roll, steamed edamame, spicy cucumber banchan",
         "Price": "USD 29"},
        {"Name": "Coconut Shrimp: five-spice crispy shrimp, Thai sweet chili sauce",
         "Price": "USD 13"},
        {"Name": "Cabo Calamari: crispy calamari, fried lemon slices, Fresno chile, chipotle aioli",
         "Price": "USD 14"},
        {"Name": "Sticky Ribs: pan-glazed Korean-style pork ribs, sesame seeds, scallions, spicy cucumber banchan",
         "Price":"USD 15"},
        {"Name": "Guaca-Poke: original ahi poke, guacamole, micro cilantro, house-made tortilla chips",
         "Price": "USD 15"},
        {"Name": "Guacamole & Chips",
         "Price": "USD 0"},
        {"Name": "Original Pokes w/ wonton chips: yellowfin ahi tuna, sesame-soy marinade, sweet onion, red pepper flakes",
         "Price": "USD 14"},
        {"Name": "Classic Ceviches w/ tortilla chips: yellowtail, citrus marinade, red onion, cucumber, Fresno chile, cilantro", 
         "Price": "USD 14"},
        {"Name": "Korean Surf & Turf: grilled skirt steak, glazed prawns, kimchi fried rice, sunny-side egg, spicy cucumber banchan, glazed shiitake mushrooms, edamame, kimchi, red ginger, pickled carrots",
         "Price": "USD 35"},
        {"Name": "Hawaiian Luau: teriyaki pork ribs, coconut shrimp, original ahi poke, wonton chips, stir fry veggies, sushi rice, pineapple sesame slaw, marinated cucumbers",
         "Price": "USD 32"},
        {"Name": "Japanese Grill: miso-glazed salmon, ahi tataki inari “bombs”, shishito peppers, miso salad, wakame-cucumber salad, steamed edamame",
         "Price": "USD 34"},
        {"Name": "Japanese Wasabi:avocado, wakame seaweed salad, marinated cucumber, pickled ginger, daikon sprouts, furikake, soy-wasabi vinaigrette Base: ½ sushi rice, ½ mixed organic greens",
         "Price": "Regular USD 19.5 | Small USD 17"},
        {"Name": "Asian Chimichurri Salad | Grilled Sea Bass*: roasted cauliflower, avocado, cucumber, tomato, edamame, daikon sprouts, Asian herb chimichurri, miso dressing",
         "Price": "Regular USD 19.5 | Small USD 17"}, 
        {"Name": "Westcoast Style | Grilled Salmon*: (VEGAN: SUB TOFU!) roasted cauliflower, avocado, marinated cucumber, radish salad, cilantro-pepita pesto, soy-tahini drizzle |",
         "Price": "Regular USD 19.5 | Small USD 17"}, 
        {"Name": "Mexican Grill | Seared Guajillo Shrimp*: citrus-guajillo adobo sauce, “elote” corn, black beans, guacamole, pico de gallo, cotija cheese, cilantro, tortilla chips, tomatillo dressing, lime crema",
         "Price": "Regular USD 19.5 | Small USD 17"}
    ]
    meal = random.choice(meal_recommendation)
    return json.dumps(meal)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
