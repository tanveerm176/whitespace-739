import extract
import time_calc
from flask import Flask, request, render_template

orbit= Flask (__name__)

temp = extract.extract_labels()
@orbit.route("/", methods=["POST", "GET"])

def census_taker():
    if request.method == "GET":
        return render_template("base.html", galaxy= "Nothing yet", label= temp)
    elif request.method == "POST":
        tracking= request.form["Select_galaxies"]
        try:
            aging= float(request.form["age"])
        except:
            return render_template("base.html", galaxy= "Nothing yet", label= temp)
        d= extract.select_galax(tracking)
        e= time_calc.time(float(d))
        total_time= e - float(aging)


        return render_template("answer.html", galaxy= tracking, answer= float(d), label= temp, answer2= e, age= total_time)

if __name__ == "__main__":

    orbit.debug= True
    orbit.run(host= '0.0.0.0', port= 12345)

