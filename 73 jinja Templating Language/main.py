from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1,10)
    cur_year = datetime.datetime.now().year
    return render_template("index.html", num=random_num, year=cur_year)

@app.route("/guess/<pname>")
def guess(pname):
    url_gender = f"https://api.genderize.io?name={pname}"
    gender_response = requests.get(url_gender)
    gender_data = gender_response.json()
    gen = gender_data["gender"]
    url_age = f"https://api.agify.io?name={pname}"
    age_response = requests.get(url_age)
    age_data = age_response.json()
    ag = age_data["age"]
    return render_template("guess.html", name=pname, age=ag , gender=gen)

@app.route("/blog/")
def get_blog():
    blog_url = "https://api.npoint.io/118dd27667f13155fbbb"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)