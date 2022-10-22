from random import randint
from flask import Flask, jsonify
import json
import os
import psycopg2

app = Flask(__name__)

def get_db_connect():
    psycopg2.connect(host=os.environ.get('DB_HOST'), port=5432, database=db, user=admin@admin.com, password="pass")

def get_rec_from_db():
    q = """
    SELECT MealName, MealPrice FROM meals ....
    """

    conn = get_db_connect()
    cursor = conn.cursor()
    cursor.execute(q)
    mr = cursor.fetchall()

    conn.close()
    return ml

def get_meal_recommendation():

    meals = [
        {'name':'PUPU PLATTER: 2 ahi poke bombs, 4 coconut shrimp, 2 sticky ribs, 4pc California roll, steamed edamame, spicy cucumber bancha', 'price':29},
        {'name':'Coconut Shrimp: five-spice crispy shrimp, Thai sweet chili sauce', 'price':13},
        {'name':'Cabo Calamari: crispy calamari, fried lemon slices, Fresno chile, chipotle aioli','price':14},
        {'name':'Sticky Ribs: pan-glazed Korean-style pork ribs, sesame seeds, scallions, spicy cucumber banchan','price':15},
        {'name':'Guaca-Poke: original ahi poke, guacamole, micro cilantro, house-made tortilla chips', 'price':15},
        {'name':'Guacamole & Chips', 'price':0},
        {'name':'Original Pokes w/ wonton chips: yellowfin ahi tuna, sesame-soy marinade, sweet onion, red pepper flakes',  'price':14},
        {'name':'Classic Ceviches w/ tortilla chips: yellowtail, citrus marinade, red onion, cucumber, Fresno chile, cilantro', 'price':14},
        {'name':'Korean Surf & Turf: grilled skirt steak, glazed prawns, kimchi fried rice, sunny-side egg, spicy cucumber banchan, glazed shiitake mushrooms, edamame, kimchi, red ginger, pickled carrots', 'price':35},
        {'name':'Hawaiian Luau: teriyaki pork ribs, coconut shrimp, original ahi poke, wonton chips, stir fry veggies, sushi rice, pineapple sesame slaw, marinated cucumbers', 'price':32},
        {'name':'Japanese Grill: miso-glazed salmon, ahi tataki inari “bombs”, shishito peppers, miso salad, wakame-cucumber salad, steamed edamame', 'price':34},
        {'name':'Japanese Wasabi:avocado, wakame seaweed salad, marinated cucumber, pickled ginger, daikon sprouts, furikake, soy-wasabi vinaigrette Base: ½ sushi rice, ½ mixed organic greens', 'price':19.5},
        {'name':'Asian Chimichurri Salad | Grilled Sea Bass*: roasted cauliflower, avocado, cucumber, tomato, edamame, daikon sprouts, Asian herb chimichurri, miso dressing', 'price':19.5},
        {'name':'Westcoast Style | Grilled Salmon*: (VEGAN: SUB TOFU!) roasted cauliflower, avocado, marinated cucumber, radish salad, cilantro-pepita pesto, soy-tahini drizzle', 'price':19.5},
        {'name':'Mexican Grill | Seared Guajillo Shrimp*: citrus-guajillo adobo sauce, “elote” corn, black beans, guacamole, pico de gallo, cotija cheese, cilantro, tortilla chips, tomatillo dressing, lime crema', 'price':19.5}
        ]

    return meals[randint(0,(len(meals)-1))]

@app.route('/')
@app.route('/recommendation/')
def index():
    return jsonify(get_meal_recommendation())

app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))
