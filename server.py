from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><img ' \
           'src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif"> '


random_number = randint(0, 10)


@app.route('/<int:guess>')
def check_guess(guess):
    if random_number == guess:
        return '<h1 style="color: green">You got it!!</h1><img ' \
               'src=https://media.giphy.com/media/elsol3P5Jt2ASsxLva/giphy.gif> '
    elif random_number > guess:
        return '<h1 style="color: blue">Too low!</h1><img ' \
               'src=https://media.giphy.com/media/2uI9astifwiSUWVOTT/giphy.gif> '
    else:
        return '<h1 style="color: red">Too high!</h1><img ' \
               'src=https://media.giphy.com/media/ekNWOoLSdHQUUurKid/giphy.gif> '


if __name__ == "__main__":
    app.run()
