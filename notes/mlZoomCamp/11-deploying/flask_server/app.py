from flask import Flask
from flask import request
from flask import jsonify

app = Flask('churn')

# setup with the pickle file
import pickle

model_file = f"model_C=1.0.bin"
with open(model_file, 'rb') as f_in: #rb is read byte
    dv, model = pickle.load(f_in)
    



@app.route("/predict", methods = ['POST'])
def predict(customer):
    customer = request.get_json()
    
    # the core logic should be in a seperate function, starting here
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= .5
    
    
    result = {
        'churn_probability': float(y_pred), # this is because we need to turn the numpy float into a regular float
        'churn' : bool(churn)               # this is because we need to turn the numpy bool into a regular bool
    }
    
    # and ending here
    
    
    return jsonify(result)

if __name__ == "__main__": 
    app.run(debug=True, host = '0.0.0.0', port = 3000)
    
