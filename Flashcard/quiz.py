from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__) #application instance
app.secret_key = 'supersecretkey'  # Required for session

# questions for now #CONSIDER: Possibly provide list of questions and answer via file which turns into dictionary
#Below can be updated, more questions and its answers can be added
flashcards = [
    {"question": "What does AI stand for?", "answer": "Artificial Intelligence"},
    {"question": "What does OOP stand for?", "answer": "Object Oriented Programming"},
    
]

@app.route("/", methods=["GET", "POST"])
def home():
        # to know: SESSION is a way to temporarily store data per user — like a short-term memory while they’re using your app.
        #This will be used to keep track of users scores
    
    if "index" not in session or session["index"] >= len(flashcards): #checkes if user started quiz and ensures we continue even if session out of range[session will keep counting despit us restarting]
        session["index"] = 0 # refer to question num
        session["score"] = 0 # refer to results score that will be tallied toward the end

    
    current = flashcards[session["index"]]
    response = "" # kept empty,this well tell user whether answer is correct or not

    
    if request.method == "POST":
        
        

        answer = request.form["answer"] #CHANGE: How to ignore upper and lower case?
        correct = current["answer"]

        if answer.upper() == correct.upper():
            session["score"] += 1 #kept score now on 1
            response = "Correct!"
        else:
            response = f"Incorrect! Correct answer: {current['answer']}"

        session["index"] += 1 #updated question number
        #prevent going out of range
        if session["index"] >= len(flashcards):
            session["index"] = 0
        current = flashcards[session["index"]]

        

    return render_template("home.html", question=current["question"], response=response)

    #return render_template('home.html')


    





    


if __name__ == '__main__': #will run flas on terminal and open window
    app.run(debug=True)
