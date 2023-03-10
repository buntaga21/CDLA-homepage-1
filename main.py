from flask import Flask, render_template
import os
import random
from cdla import reigning_champ, champions_list

app = Flask(__name__)

imgs = os.listdir('static/nav_imgs')
imgs = ['nav_imgs/' + file for file in imgs]


@app.route("/")
def hello_world():
  imgrand = random.sample(imgs, k=4)
  reigning = reigning_champ()
  return render_template('home.html', imgrand=imgrand, reigning=reigning)


@app.route("/history")
def cdla_history():
  imgrand = random.sample(imgs, k=4)
  champs = champions_list()
  return render_template('history.html', imgrand=imgrand, champs=champs)


@app.route("/rules")
def cdla_rules():
  imgrand = random.sample(imgs, k=4)
  return render_template('rules.html', imgrand=imgrand)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
