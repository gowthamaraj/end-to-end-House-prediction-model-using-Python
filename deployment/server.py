from flask import Flask, request, render_template
app = Flask(__name__)
import numpy as np
from model import model

@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        e = int(request.form['experience'])
        t = int(request.form['test_score'])
        i = int(request.form['interview_score'])
        data = np.array([[e,t,i]])
        output = str(round(model.predict(data)[0],2))
        return render_template('result.html', result= output)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)