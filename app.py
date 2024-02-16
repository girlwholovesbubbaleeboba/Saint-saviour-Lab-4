from flask import Flask
import random

app = Flask(__name__)

# Route for rolling a single 20-sided die
@app.route('/roll')
def roll():
    # Roll a single 20-sided die
    result = random.randint(1, 20)
    # Choose a random combat detail from the list
    details = random.choice([
        "You swing your sword with precision, landing a solid hit!",
        "Your attack narrowly misses the target, grazing their armor.",
        "The enemy dodges your strike, narrowly avoiding harm."
    ])
    # Return the result and combat details
    return f"Result for /roll: Rolled a {result}. Combat details: {details}"

# Route for rolling with advantage (rolling two dice and taking the higher result)
@app.route('/roll/advantage')
def roll_advantage():
    # Roll two 20-sided dice
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    # Get the greater result of the two rolls
    greater_result = max(result1, result2)
    # Choose a random combat detail from the list
    details = random.choice([
        "You channel your inner strength, delivering a powerful blow!",
        "Your attack lands, and you gained 2x strength.",
        "With a quick feint, you catch the enemy off balance, opening them up to further attacks."
    ])
    # Return the results and combat details
    return f"Result for /roll.advantage: Rolled {result1} and {result2}. Greater result: {greater_result}. Combat details: {details}"

# Route for rolling with disadvantage (rolling two dice and taking the lower result)
@app.route('/roll/disadvantage')
def roll_disadvantage():
    # Roll two 20-sided dice
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    # Get the lesser result of the two rolls
    lesser_result = min(result1, result2)
    # Choose a random combat detail from the list
    details = random.choice([
        "Your blow is deflected by the opponent's shield.",
        "In a surprising turn of events, your weapon slips from your grasp, leaving you momentarily vulnerable.",
        "The enemy counterattacks with swift ferocity, catching you off guard."
    ])
    # Return the results and combat details
    return f"Result for /roll.disadvantage: Rolled {result1} and {result2}. Lesser result: {lesser_result}. Combat details: {details}"

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
