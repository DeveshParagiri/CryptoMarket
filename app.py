from flask import Flask,render_template
import coins

labels = []
values = []
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    labels1, values1 = coins.labels1, coins.values1
    labels2, values2 = coins.labels2, coins.values2
    return render_template('home.html', values1=values1, labels1=labels1, values2=values2, labels2=labels2)

@app.route('/market')
def market_page():
    return render_template('market.html', items=coins.items)

@app.route('/helpfulinks')
def helpfulinks_page():
    return render_template('helpfulinks.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
