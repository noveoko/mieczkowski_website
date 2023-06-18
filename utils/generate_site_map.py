import os
import flask
from flask_sitemapper import Sitemapper

sitemapper = Sitemapper()

app = flask.Flask(__name__)
sitemapper.init_app(app)

# Define the root directory of your Flask app
app_root = os.path.dirname(os.path.abspath(__file__))

@sitemapper.include(lastmod="")
@app.route("/")
def home():
    return flask.render_template("index.html")

@sitemapper.include(lastmod="")
@app.route("/about")
def about():
    return flask.render_template("oferta.html")

@app.route("/sitemap.xml")
def sitemap():
    sitemap_path = os.path.join(app_root, "static", "sitemap.xml")
    return sitemapper.generate(sitemap_path)

if __name__ == "__main__":
    app.run()