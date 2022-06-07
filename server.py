import sys
import os
import json

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer  # Added
from flaskext.markdown import Markdown

# Some configuration, ensures
# 1. Pages are loaded on request.
# 2. File name extension for pages is Markdown.
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
app.config["FREEZER_DESTINATION"] = "docs"
pages = FlatPages(app)
freezer = Freezer(app)  # Creates a frozen object of the flask app
markdown_manager = Markdown(app, extensions=["fenced_code"], output_format="html5",)

posts = [page for page in list(pages) if not page.path.startswith("r/")]
reviews = [page for page in list(pages) if page.path.startswith("r/")]
review_tags = set([tag for page in list(reviews) for tag in page.meta["tags"]])

# URL Routing - Home Page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts/")
def posts():
    return render_template("posts.html", pages=pages)


@app.route("/projects/")
def projects():
    with open("data/projects.json") as projects_json:
        projects_data = json.load(projects_json)
        return render_template("projects.html", projects=projects_data)


# @app.route("/about/")
# def about():
#     return render_template("about.html", pages=pages)


@app.route("/resume/")
def resume():
    return render_template("resume.html", pages=pages)


# URL Routing - Flat Pages
# Retrieves the page path and
@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


@app.errorhandler(404)
def page_not_found(path):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


# Main Function, Runs at http://0.0.0.0:8000
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()  # creates set of static files from the flask app
    else:
        app.run(port=8000)
