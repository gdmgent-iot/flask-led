from flask import Flask, render_templatefrom gpiozero import LED


app = Flask(__name__)


led_pin = LED(18)


@app.route("/")def main():

    return render_template('main.html')

@app.route("/<led>/<action>")def action(pin, action):

    if led == "led1":

        if action == "on":

            led_pin.on()  # Turn LED 1 onelif action == "off":

            led_pin.off()  # Turn LED 1 offreturn render_template('main.html')

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5050)