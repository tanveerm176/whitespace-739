from flask import Flask, render_template
import pic_engine

pic_flask = Flask(__name__)
@pic_flask.route('/')
def pic():
        i = pic_engine.get_img()[0]
        t = pic_engine.get_img()[1]
        f = pic_engine.get_img()[2]
        return render_template("finalHome.html", x = i, k = t, h = f)

if __name__ == "__main__":
        pic_flask.debug = True
        pic_flask.run()
