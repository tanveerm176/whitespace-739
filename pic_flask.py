from flask import Flask, render_template
import pic_engine

pic_flask = Flask(__name__)
@pic_flask.route('/')
def pic():
<<<<<<< HEAD
        i = pic_engine.get_img()
        t = pic_engine.get_title()
        f = pic_engine.get_expl()
        return render_template("finalHome.html", x = i, k = t, h = f)
=======
	i = pic_engine.get_img()
	t = pic_engine.get_title()
	f = pic_engine.get_expl()
	return render_template("finalHome.html", x = i, k = t, h = f)
>>>>>>> 9486aeef7fc9085288ceb0532a378da157f297bd

if __name__ == "__main__":
        pic_flask.debug = True
        pic_flask.run()
