from flask import Flask, request, render_template
from text_processor import TextProcessor  # tavo logika čia

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    if request.method == "POST":
        text = request.form.get("text", "")
        if text:
            processor = TextProcessor(text)
            report = processor.generate_report()
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")