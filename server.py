from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route("/")
def my_info():
    return render_template('index.html')

@app.route("/mail.php")
def my_home():
    return render_template('mail.php')

def write_to_file(data):
    with open('database.txt', mode="a") as database:
        name = data ["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{name},{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'thank you for sending us a message get in touch with you as soon a possible !!'
    else:
        return "something gone run"

