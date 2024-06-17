from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        piles_str = request.form['piles']
        hours_str = request.form['hours']

        if piles_str == '' or hours_str == '':
            return render_template('index.html', error_msg='Invalid input. Please provide valid values.')

        try:
            piles = list(map(int, piles_str.split(',')))
            h = int(hours_str)
            min_speed = minEatingSpeed(piles, h)
            return render_template('result.html', min_speed=min_speed)
        except ValueError:
            return render_template('index.html', error_msg='Invalid input. Please provide valid values.')

    return render_template('index.html')


def minEatingSpeed(piles, h):
    def canFinish(speed):
        hours = 0
        for bananas in piles:
            hours += (bananas + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if canFinish(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    app.run(debug=True)
