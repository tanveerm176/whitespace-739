from flask import Flask, render_template
import pic_engine
import exo
import time_calc
import galax
import star
import quoteList

pic_flask = Flask(__name__)
@pic_flask.route('/')
def pic():
    b = pic_engine.get_img()
    i = b[0]
    t = b[1]
    f = b[2]
    d = quoteList.generate()
    return render_template("finalHome.html", x = i, k = t, h = f, b = d)


@pic_flask.route('/main/')
def main():
    jk = exo.labels()
    kj = exo.distly()
    return render_template("finalBase.html", l = jk, z = kj)

@pic_flask.route('/galaxy/')
def galaxy():
    kk = galax.labels1()
    kl = galax.distly1()
    return render_template("finalBase.html", l = kk, z = kl)

@pic_flask.route('/stars/')
def stars():
    gg = star.labels2()
    jj = star.distly2()
    return render_template("finalBase.html", l = gg, z = jj)
'''
@pic_flask.route('/extra/')
def extra():
    gh = exo.labels()
    vv = galax.labels1()
    hh = star.labels2()
    return render_template("extra.html",l = vv, s = gh, a = hh)
'''

if __name__ == "__main__":
    pic_flask.debug = True
    pic_flask.run(host = '0.0.0.0')
