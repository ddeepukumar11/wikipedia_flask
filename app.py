from flask import Flask,request,render_template
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    a = request.args.get("Query")
    try:
        summary = wikipedia.summary(a)
        return summary
    except:
        return "error"



if __name__ == "__main__":
    app.run()



