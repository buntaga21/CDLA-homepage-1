from flask import Flask, render_template
import os
import random
from cdla import reigning_champ, champions_list, team_list, reigning_champ_players, team0, team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16, team17, team18, team19

app = Flask(__name__)

imgs = os.listdir('static/nav_imgs')
imgs = ['nav_imgs/' + file for file in imgs]


@app.route("/")
def hello_world():
  imgrand = random.sample(imgs, k=4)
  reigning = reigning_champ()
  teams = team_list()
  players = reigning_champ_players()
  return render_template('home.html',
                         imgrand=imgrand,
                         reigning=reigning,
                         teams=teams,
                         players=players)


@app.route("/history")
def cdla_history():
  imgrand = random.sample(imgs, k=4)
  champs = champions_list()
  teams = team_list()
  return render_template('history.html',
                         imgrand=imgrand,
                         champs=champs,
                         teams=teams)


@app.route("/rules")
def cdla_rules():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  return render_template('rules.html', imgrand=imgrand, teams=teams)


@app.route("/0")
def rio():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team0()
  return render_template('0.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/1")
def nyb():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team1()
  return render_template('1.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/2")
def phi():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team2()
  return render_template('2.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/3")
def chi():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team3()
  return render_template('3.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/4")
def mxc():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team4()
  return render_template('4.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/5")
def bkn():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team5()
  return render_template('5.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/6")
def tok():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team6()
  return render_template('6.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/7")
def was():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team7()
  return render_template('7.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/8")
def mia():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team8()
  return render_template('8.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/9")
def bei():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team9()
  return render_template('9.html', imgrand=imgrand, teams=teams, roster=roster)


@app.route("/10")
def tor():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team10()
  return render_template('10.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/11")
def dal():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team11()
  return render_template('11.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/12")
def lon():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team12()
  return render_template('12.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/13")
def min():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team13()
  return render_template('13.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/14")
def sea():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team14()
  return render_template('14.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/15")
def lal():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team15()
  return render_template('15.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/16")
def lv():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team16()
  return render_template('16.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/17")
def sac():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team17()
  return render_template('17.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/18")
def cgy():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team18()
  return render_template('18.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


@app.route("/19")
def mem():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  roster = team19()
  return render_template('19.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
