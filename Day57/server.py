from flask import Flask, render_template
import random
import datetime
import requests
app= Flask(__name__)

@app.route("/")
def homepage():
    random_number= random.randint(1,10)
    current_date= datetime.datetime.now().year
    return render_template("index.html",num=random_number,year=current_date)
@app.route("/guess/<name>")
def get_guess(name):
    name_info= requests.get(f"https://api.genderize.io?name={name}").json()
    return render_template("guess.html",name_info=name_info)
@app.route("/blog")
def get_blog():
    blog_list=requests.get(f"https://www.npoint.io/docs/c790b4d5cab58020d391").json()
    print(blog_list[0])
    return render_template("blog.html",blog_list=blog_list)

if __name__=="__main__":
    app.run(debug=True)