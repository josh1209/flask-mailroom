import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/', methods=['GET', 'POST'])
def all():
#    donations = Donation.select()
    if request.method == 'POST':
        return redirect(url_for('create'))
    return render_template('donations.jinja2', donations=Donation.select())
    
@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if not request.form['name']:
            return redirect(url_for('all'))
        donor_name = Donor.select().where(Donor.name == request.form['name']).get()
        task2 = Donation(value=request.form['donation'], donor=donor_name)
        task2.save()
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
