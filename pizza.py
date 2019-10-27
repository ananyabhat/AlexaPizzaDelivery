import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

sizes = ['personal', 'small', 'medium', 'large', 'extra large']
possible_toppings = [
    'cheese',
    'salami', 
    'pepperoni', 
    'pineapple', 
    'ham', 
    'basil', 
    'mozzarella',
    'feta cheese', 
    'parmesan', 
    'sausage', 
    'mushrooms', 
    'tomatoes', 
    'bell peppers',
    'jalapenos', 
    'onions', 
    'olives', 
    'artichokes', 
    'anchovies', 
    'beef', 
    'chicken',
    'spinach', 
    'garlic', 
    'bacon', 
    'crushed red pepper', 
    'no toppings', 
    'nothing'
    ]
pizzas = []

@ask.launch

def new_order():
    welcome_msg = render_template('welcome')
    while (len(pizzas) > 0):
        pizzas.pop()

    return question(welcome_msg)

@ask.intent("YesIntent")

def ask_for_size():
    session.attributes['size'] = ""
    session.attributes['toppings'] = []
    size_msg = render_template('size')

    return question(size_msg)

@ask.intent("SizeIntent", convert={'size':str})

def ask_for_toppings(size):
    session.attributes['size'] = size

    if size in sizes:
        msg = render_template('toppings', size = session.attributes['size'])

    return question(msg)

@ask.intent("ToppingsIntent", convert={'firstTopping': str, 'secondTopping': str, 'thirdTopping': str, 'fourthTopping': str})

def set_order(firstTopping, secondTopping, thirdTopping, fourthTopping):
    toppings = []
    if firstTopping != "" and firstTopping in possible_toppings:
        toppings.append(firstTopping)
    if secondTopping != "" and secondTopping in possible_toppings:
        toppings.append(secondTopping)
    if thirdTopping != "" and thirdTopping in possible_toppings:
        toppings.append(thirdTopping)
    if fourthTopping != "" and fourthTopping in possible_toppings:
        toppings.append(fourthTopping)
    session.attributes['toppings'] = toppings
    order_msg = render_template('order', size = session.attributes['size'], toppings = session.attributes['toppings'])
    pizzas.append([session.attributes['size'], session.attributes['toppings']])
    return question(order_msg)

@ask.intent("CancelIntent")

def cancel():
    pizzas.pop()
    cancel_msg = render_template('cancel')
    return question(cancel_msg)

@ask.intent("NoIntent")

def confirm():    
    num_pizzas = len(pizzas)

    if num_pizzas == 0:
        return question("You have ordered no pizzas. Please say confirm to confirm your order.")

    confirm_msg = "You have ordered one "

    for i, pizza in enumerate(pizzas):
        if i > 0:
            confirm_msg += " and one "

        size = pizza[0]
        toppings = pizza[1]

        confirm_msg += size + " pizza with "

        confirm_msg += " and ".join(toppings)
    
    confirm_msg += ". Please say confirm to confirm your order."
    
    return question(confirm_msg)

@ask.intent("CorrectIntent")

def thanks():

    thanks_msg = render_template('thanks')

    return statement(thanks_msg)

if __name__ == '__main__':

    app.run(debug=True)
