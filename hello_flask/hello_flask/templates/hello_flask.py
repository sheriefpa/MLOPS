import flask
import pandas as pd
# Create the application.

df=pd.read_csv("../templates/LoanApprovalPrediction.csv")
print(df.head())
dict=df.to_dict()
print(dict)
app = flask.Flask(__name__,template_folder='../templates')


@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
