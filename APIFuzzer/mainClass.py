from flask import Flask, render_template,request
import SeleniumCases
import SearchForProductCase
import OrderSummaryCase
import TrackOurOrderPackageCase
import KnowYourBrowsingHistory
import TodaysDealsCase
import CheckPrimeMemberShipCase
import unittest


app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index2.html")


@app.route('/welcome', methods=['GET','POST'])
def welcome():
    if request.method == 'POST':
        return render_template("home.html")


@app.route('/index', methods=['GET','POST'])
def index():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=SeleniumCases)
    return render_template('index2.html')


@app.route('/searchcase', methods=['GET','POST'])
def searchcase():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=SearchForProductCase)
    return render_template('index2.html')


@app.route('/ordersummary', methods=['GET','POST'])
def ordersummary():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=OrderSummaryCase)
    return render_template('index2.html')

@app.route('/trackpackage', methods=['GET','POST'])
def trackpackage():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=TrackOurOrderPackageCase)
    return render_template('index2.html')

@app.route('/knowhistory', methods=['GET','POST'])
def knowhistory():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=KnowYourBrowsingHistory)
    return render_template('index2.html')

@app.route('/checkprime', methods=['GET','POST'])
def checkprime():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=CheckPrimeMemberShipCase)
    return render_template('index2.html')

@app.route('/todaysdeal', methods=['GET','POST'])
def todaysdeal():
    if request.method=='POST':
        #unittest.main(module=ReportGenerator)
        unittest.main(module=TodaysDealsCase)
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True)

