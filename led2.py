from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

led_pin = LED(17)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/<led>/<action>")
def action(led, action):
    if led == "led1":
        if action == "on":
            led_pin.on()  # Turn LED 1 on
        elif action == "off":
            led_pin.off()  # Turn LED 1 off
    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)