from flask import Flask, render_template, request
from automata_filter import automata_detect
from ai_model import predict_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        
        # Step 1: Automata filtering
        auto_result = automata_detect(message)
        
        # Step 2: AI classification
        ai_result = predict_message(message)
        
        # Combine results
        if "Spam" in auto_result or "Spam" in ai_result:
            result = f"🚨 Spam Detected!\nAutomata: {auto_result}\nAI: {ai_result}"
        else:
            result = f"✅ Genuine Message.\nAutomata: {auto_result}\nAI: {ai_result}"
    
    return render_template("index.html", result=result)
    
if __name__ == "__main__":
    app.run(debug=True)
