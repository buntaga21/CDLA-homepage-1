from flask import Flask, render_template
import os
import random
from cdla import reigning_champ, champions_list, team_list, reigning_champ_players, team0, mvp, dpoy, smoty, mip, roy, team_history

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
  mv = mvp()
  dp = dpoy()
  sm = smoty()
  mi = mip()
  ry = roy()
  return render_template('history.html',
                         imgrand=imgrand,
                         champs=champs,
                         teams=teams,
                         mvp=mv,
                         dpoy=dp,
                         smoty=sm,
                         mip=mi,
                         roy=ry)


@app.route("/rules")
def cdla_rules():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  return render_template('rules.html', imgrand=imgrand, teams=teams)


@app.route("/0")
def rio():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 0
  roster = team0(tid)
  history = team_history(tid)
  return render_template('0.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/1")
def nyb():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 1
  roster = team0(tid)
  history = team_history(tid)
  return render_template('1.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/2")
def phi():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 2
  roster = team0(tid)
  history = team_history(tid)
  return render_template('2.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/3")
def chi():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 3
  roster = team0(tid)
  history = team_history(tid)
  return render_template('3.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/4")
def mxc():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 4
  roster = team0(tid)
  history = team_history(tid)
  return render_template('4.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/5")
def bkn():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 5
  roster = team0(tid)
  history = team_history(tid)
  return render_template('5.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/6")
def tok():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 6
  roster = team0(tid)
  history = team_history(tid)
  return render_template('6.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/7")
def was():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 7
  roster = team0(tid)
  history = team_history(tid)
  return render_template('7.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/8")
def mia():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 8
  roster = team0(tid)
  history = team_history(tid)
  return render_template('8.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/9")
def bei():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 9
  roster = team0(tid)
  history = team_history(tid)
  return render_template('9.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/10")
def tor():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 10
  roster = team0(tid)
  history = team_history(tid)
  return render_template('10.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/11")
def dal():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 11
  roster = team0(tid)
  history = team_history(tid)
  return render_template('11.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/12")
def lon():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 12
  roster = team0(tid)
  history = team_history(tid)
  return render_template('12.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/13")
def min():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 13
  roster = team0(tid)
  history = team_history(tid)
  return render_template('13.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/14")
def sea():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 14
  roster = team0(tid)
  history = team_history(tid)
  return render_template('14.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/15")
def lal():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 15
  roster = team0(tid)
  history = team_history(tid)
  return render_template('15.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/16")
def lv():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 16
  roster = team0(tid)
  history = team_history(tid)
  return render_template('16.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/17")
def sac():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 17
  roster = team0(tid)
  history = team_history(tid)
  return render_template('17.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/18")
def cgy():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 18
  roster = team0(tid)
  history = team_history(tid)
  return render_template('18.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


@app.route("/19")
def mem():
  imgrand = random.sample(imgs, k=4)
  teams = team_list()
  tid = 19
  roster = team0(tid)
  history = team_history(tid)
  return render_template('19.html',
                         imgrand=imgrand,
                         teams=teams,
                         roster=roster,
                         tid=tid,
                         history=history)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
