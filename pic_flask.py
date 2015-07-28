from flask import Flask, render_template
import pic_engine

pic_flask = Flask(__name__)
@pic_flask.route('/')
def pic():
        i = pic_engine.get_img()
        t = pic_engine.get_title()
        f = pic_engine.get_expl()
        return render_template("finalHome.html", x = i, k = t, h = f)

if __name__ == "__main__":
        pic_flask.debug = True
        pic_flask.run()
