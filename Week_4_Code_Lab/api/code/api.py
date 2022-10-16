from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/meal')
def get_meal_recommendation():
    meal_recommendation = {
        "PUPU PLATTER: 2 ahi poke bombs, 4 coconut shrimp, 2 sticky ribs, 4pc California roll, steamed edamame, spicy cucumber banchan": "USD 29",
        "Coconut Shrimp: five-spice crispy shrimp, Thai sweet chili sauce": "USD 13",
        "Cabo Calamari: crispy calamari, fried lemon slices, Fresno chile, chipotle aioli": "USD 14",
        "Sticky Ribs: pan-glazed Korean-style pork ribs, sesame seeds, scallions, spicy cucumber banchan": "USD 15",
        "Guaca-Poke: original ahi poke, guacamole, micro cilantro, house-made tortilla chips": "USD 15",
        "Guacamole & Chips": "USD 0",
        "Original Pokes w/ wonton chips: yellowfin ahi tuna, sesame-soy marinade, sweet onion, red pepper flakes": "USD 14",
        "Classic Ceviches w/ tortilla chips: yellowtail, citrus marinade, red onion, cucumber, Fresno chile, cilantro": "USD 14",
        "Korean Surf & Turf: grilled skirt steak, glazed prawns, kimchi fried rice, sunny-side egg, spicy cucumber banchan, glazed shiitake mushrooms, edamame, kimchi, red ginger, pickled carrots": "USD 35",
        "Hawaiian Luau: teriyaki pork ribs, coconut shrimp, original ahi poke, wonton chips, stir fry veggies, sushi rice, pineapple sesame slaw, marinated cucumbers": "USD 32",
        "Japanese Grill: miso-glazed salmon, ahi tataki inari “bombs”, shishito peppers, miso salad, wakame-cucumber salad, steamed edamame": "USD 34",
        "Japanese Wasabi:avocado, wakame seaweed salad, marinated cucumber, pickled ginger, daikon sprouts, furikake, soy-wasabi vinaigrette Base: ½ sushi rice, ½ mixed organic greens": "Regular USD 19.5 | Small USD 17",
        "Asian Chimichurri Salad | Grilled Sea Bass*: roasted cauliflower, avocado, cucumber, tomato, edamame, daikon sprouts, Asian herb chimichurri, miso dressing": "Regular USD 19.5 | Small USD 17", 
        "Westcoast Style | Grilled Salmon*: (VEGAN: SUB TOFU!) roasted cauliflower, avocado, marinated cucumber, radish salad, cilantro-pepita pesto, soy-tahini drizzle |": "Regular USD 19.5 | Small USD 17", 
        "Mexican Grill | Seared Guajillo Shrimp*: citrus-guajillo adobo sauce, “elote” corn, black beans, guacamole, pico de gallo, cotija cheese, cilantro, tortilla chips, tomatillo dressing, lime crema":  "Regular USD 19.5 | Small USD 17"
    }
    return meal_recommendation

if __name__ == '__main__':
    app.run()
