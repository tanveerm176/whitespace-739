from flask import Flask, render_template
import pic_engine

pic_flask = Flask(__name__)

@pic_flask.route('/')
def pic():
	i = pic_engine.get_img()
	t = pic_engine.get_title()
	#i = "http://apod.nasa.gov/apod/image/1507/MWAurora_hang_960.jpg"
	return render_template("pic_img.html", x = i, k = t)

if __name__ == "__main__":
	pic_flask.debug = True
	pic_flask.run()
