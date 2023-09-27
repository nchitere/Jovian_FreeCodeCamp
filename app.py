from flask import Flask, render_template, jsonify

app = Flask(__name__)
jobs =[
  {'id' : 1,
  'title':'Data analyst',
  'location':'Nairobi,Kenya',
  'salary':'Ksh 350,000'},
    {'id' : 2,
  'title':'Data scientist',
  'location':'Nairobi,Kenya',
  'salary':'Ksh 500,000'},
    {'id' : 3,
  'title':'Front end Engineer',
  'location':'Remote',
  'salary':'Ksh 1050,000'},
      {'id' : 4,
  'title':'Back end Engineer',
  'location':'Montana US',
  'salary':'$ 300,000'}
]

@app.route("/")
def Data_Engineer():
  return render_template('home.html',jobs=jobs, company_name ="Jovian")


@app.route("/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
