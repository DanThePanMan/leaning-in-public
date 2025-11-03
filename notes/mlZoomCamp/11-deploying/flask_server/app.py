from flask import Flask

app = Flask('app')

@app.route("/predict", methods = ['GET'])
def test():
    return "asdf"

if __name__ == "__main__": 
    app.run(debug=True, host = '0.0.0.0', port = 3000)
    
    
    
# we can test this in the browser or using curl