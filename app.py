from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {'id':1,'title': 'Front-End Developer','experience':'1+ Year','location':'Remote'},
  {'id':2,'title': 'Back-End Developer','experience':'2+ Year','location':'Remote'},
  {'id':3,'title': 'Graphics Designer','experience':'1+ Year','location':'Remote'},
  {'id':4,'title': 'Business Development executive','experience':'2+ Year','location':'Remote'},
  {'id':5,'title': 'Data Analyst','experience':'2+ Year','location':'Remote'}
]


@app.route("/")
def hello_world():
  return render_template('index.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
