import pandas as pd
from flask import Flask, request, render_template



app = Flask(__name__)


# ... (Rest of your Flask application code remains the same)
# Load your dataset from CSV
df = pd.read_csv(r"C:\Users\ansha\Downloads\Chatbot-20231221T063917Z-001\new_alumni_data.csv")

@app.route("/")
def home():
    return render_template("index.html")

    
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]

    # Check if the user's message is a name in the dataset
    matching_names = df[df['Your Name'].str.lower().str.contains(user_message.lower())]

    if not matching_names.empty:
        # If there is a match, provide details for the first matching name
        details = matching_names.iloc[0].to_dict()
        response = f"Details for {details['Your Name']}:\nPhone Number: {details['Phone Number']}\nBatch: {details['Batch']}\nAddress: {details['Your Permanent Address']}"
    else:
        response = "I'm sorry, I don't have details for that name."

    return response

if __name__== "__main__":
    app.run()