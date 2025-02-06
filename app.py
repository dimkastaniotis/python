from flask import Flask, jsonify
import random

app = Flask(__name__)

# Λίστα με τυχαία γεγονότα
facts = [
    "Η Python δημιουργήθηκε από τον Guido van Rossum το 1991.",
    "Η λέξη 'Python' προέρχεται από τους Monty Python, όχι από το φίδι.",
    "Η Python χρησιμοποιείται από εταιρείες όπως η Google, το Facebook και η NASA.",
    "Οι λευκοί κενοί χαρακτήρες (indentation) είναι υποχρεωτικοί στην Python.",
    "Το Django είναι ένα framework της Python για ανάπτυξη ιστοσελίδων."
]

@app.route("/api/fact")
def get_fact():
    fact = random.choice(facts)
    return jsonify({"fact": fact})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
