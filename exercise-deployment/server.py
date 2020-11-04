from flask import Flask, request, render_template
app = Flask(__name__)
import numpy as np
from model import model

@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        v1 = float(request.form['1'])
        v2 = float(request.form['2'])
        v3 = float(request.form['3'])
        v4 = float(request.form['4'])
        v5 = float(request.form['5'])
        v6 = float(request.form['6'])
        v7 = float(request.form['7'])
        v8 = float(request.form['8'])
        v9 = float(request.form['9'])
        v10 = float(request.form['10'])
        v11 = float(request.form['11'])
        v12 = float(request.form['12'])
        v13 = float(request.form['13'])
        data = np.array([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]])
        output = str(round(model.predict(data)[0],2))
        return render_template('result.html', result= output)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)