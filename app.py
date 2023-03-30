from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Berlin',
  'salary': 50000,
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Lyiv',
  'salary': 30000,
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'Warsaw',
  'salary': 40000,
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
