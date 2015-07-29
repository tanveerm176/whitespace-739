from flask import Flask, render_template
import pic_engine
import exo
import time_calc
import galax
import star

pic_flask = Flask(__name__)
@pic_flask.route('/')
def pic():
        i = pic_engine.get_img()[0]
        t = pic_engine.get_img()[1]
        f = pic_engine.get_img()[2]
        return render_template("finalHome.html", x = i, k = t, h = f)


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

if __name__ == "__main__":
        pic_flask.debug = True
        pic_flask.run(host = '0.0.0.0')
