from flask import Flask,url_for,request, redirect
from flask import render_template as rt
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return rt('index.html')

@app.route('/works')
def works():
    return rt('works.html')

@app.route('/about')
def about():
    return rt('about.html')

@app.route('/contact')
def contact():
    return rt('contact.html')


def write_file(data):
	with open('database.txt', mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f'{email},{subject},{message}\n')

def write_file_csv(data):
	with open('databasee.csv', mode='a') as database_csv:
		email1=data['email']
		subject1=data['subject']
		message1=data['message']
		file_csv=csv.writer(database_csv,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		file_csv.writerow([email1,subject1,message1])

@app.route('/submit_f', methods=['POST', 'GET','PATCH'])
def submit_f():
    if request.method == "POST":
       data=request.form.to_dict()
       write_file(data)
       write_file_csv(data)
       return  rt('submit_f.html')
    else:
       return 'something went wrong please try again'
