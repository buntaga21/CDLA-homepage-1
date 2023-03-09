from flask import Flask, render_template
import os
import random

app = Flask(__name__)

imgs = os.listdir('static/nav_imgs')
imgs = ['nav_imgs/' + file for file in imgs]


@app.route("/")
def hello_world():
  imgrand = random.sample(imgs, k=4)
  return render_template('home.html', imgrand=imgrand)


@app.route("/history")
def cdla_history():
  imgrand = random.sample(imgs, k=4)
  return render_template('history.html', imgrand=imgrand)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
