# AlexaPizzaDelivery
This Alexa Skill simulates a typical pizza delivery system. The skill logic is built in python and can be found at pizza.py. Alexa's templated responses are located in templates.yaml.

# Intents
There are six different custom intents in this skill.

### YesIntent
   - indicates: user would like to order a pizza
   - triggers: `ask_for_size()`, which asks a user to select a size for their pizza
### SizeIntent
   - indicates: user has selected a size and would like to move on to adding toppings
   - triggers: `ask_for_toppings()`, which asks a user to select up to four toppings for their pizza
### ToppingsIntent
   - indicates: user has selected toppings and would like to move on to confirming their order, canceling their order, or          adding a new order
   - triggers: `set_order()`, which asks the user if they would like to add a new order or confirm and finish their current          order
### CancelIntent
   - indicates: user would like to remove their current pizza from the overall order
   - triggers: `cancel()`, which confirms that the current order has been cancelled and asks if the user would like to add a        new order instead
### NoIntent
   - indicates: user would not like to add a new pizza and would like to move onto confirming their order
   - triggers: `confirm()`, which repeats all pizzas the user has ordered and asks the user to confirm that what they have          repeated is correct
### CorrectIntent
   - tells the user how long they will have to wait for their order, lets them know how to trigger the skill again, and            finally thanks the user

# Slot Types
There are two custom slot types in this skill: SIZE and TOPPINGS. The two slots are used in the SizeIntent and ToppingsIntent, respectively. Below are the accepted values for each custom slot type. 
  ### SIZE
  - extra large
  - personal
  - large
  - medium
  - small
  ### TOPPINGS
  - nothing
  - no toppings
  - spinach
  - garlic
  - bacon
  - parmesan
  - basil
  - feta cheese
  - crushed red pepper
  - artichokes
  - anchovies
  - pineapple
  - beef
  - ham
  - chicken
  - onions
  - jalapenos
  - bell peppers
  - olives
  - mushrooms
  - tomatoes
  - sausage
  - mozzarella
  - salami
  - pepperoni

# Sample Utterances
Below are the sample utterances I have encoded into my skill.

### YesIntent
"Yes"
"Sure"
"Yeah"
"I want to order a pizza"
"Order"
"Ok"
"Alright"
"Go"
"Start a new order"
 "Start a new pizza"
"Start a new pizza order"
"New order"
"New pizza"

### SizeIntent
  - "{size}"
  -  "I would like a {size} pizza"
  - "I want a {size} pizza"
  - "A {size} pizza please"
  - "{size} pizza"
  -  "{size} pizza please"
  - "Order a {size} pizza"
  - "Can I have a {size} pizza"
### ToppingsIntent
  - "{firstTopping}"
  - "{firstTopping} {secondTopping}"
  - "{firstTopping} and {secondTopping}",
  - "{firstTopping} {secondTopping} {thirdTopping}"
  -  "{firstTopping} {secondTopping} and {thirdTopping}"
  -  "{firstTopping} {secondTopping} {thirdTopping} {fourthTopping}"
  - "{firstTopping} {secondTopping} {thirdTopping} and {fourthTopping}"
  - "I would like {firstTopping}"
  -  "I would like {firstTopping} and {secondTopping}"
  -  "I would like {firstTopping} {secondTopping} and {thirdTopping}"
  - "I would like {firstTopping} {secondTopping} {thirdTopping} and {fourthTopping}"
  -  "I want {firstTopping}"
  - "I want {firstTopping} and {secondTopping}"
  - "I want {firstTopping} {secondTopping} and {thirdTopping}"
  - "I want {firstTopping} {secondTopping} {thirdTopping} and {fourthTopping}"
### CancelIntent
  - "Remove"
  - "Remove order"
  - "Remove this pizza"
  - "Cancel"
  - "Cancel my order"
  - "I don't want to continue this order"
  - "Cancel my current order"
  - "Stop"
  - "I don't want this pizza"
  - "I don't want this pizza anymore"
  - "Cancel this pizza"
  - "Cancel this order"
  - "Remove my order"
  - "No that's wrong"
### NoIntent
  - "No"
  - "No thanks"
  - "No I don't want to order another pizza"
  - "No more"
  - "No I don't want any more"
  - "No I don't think so"
  - "No thank you"
  - "That's all for now"
  - "That's all"
  - "That's it"
  - "I'm ok"
  - "No I don't want another pizza"
  - "No I don't want more"
  - "No I don't want more pizza"
  - "Not right now"
  - "I'm good"
### CorrectIntent
  - "Confirm"
  - "Correct"
  - "That is correct"
  - "That's correct"
  - "Sounds good"

