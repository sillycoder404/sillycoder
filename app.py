from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_eligibility():
    result = None
    if request.method == "POST":
        # Get form values
        attendance = int(request.form["attendance"])
        fee_paid = request.form.get("fee") == "yes"
        assignment_submitted = request.form.get("assignment") == "yes"
        no_disciplinary = request.form.get("discipline") == "yes"

        # Logic: Eligibility = p ∧ q ∧ r ∧ s
        eligible = (attendance >= 75 and fee_paid and assignment_submitted and no_disciplinary)
        result = "✅ Eligible for exam" if eligible else "❌ Not eligible"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/truth")
def truth_table():
    # Propositions: p, q, r, s
    table = []
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                for s in [True, False]:
                    eligible = p and q and r and s
                    table.append({
                        "p": p, "q": q, "r": r, "s": s,
                        "eligible": eligible
                    })
    return render_template("truth.html", table=table)
@app.route("/", methods=["GET", "POST"])
def check_eligibility():
    result = None
    if request.method == "POST":
        attendance = int(request.form["attendance"])
        fee_paid = request.form.get("fee") == "yes"
        assignment_submitted = request.form.get("assignment") == "yes"
        no_disciplinary = request.form.get("discipline") == "yes"
        medical_certificate = request.form.get("medical") == "yes"

        # Logic: (p ∧ q ∧ r ∧ s) ∨ (m ∧ q ∧ r ∧ s ∧ attendance ≥65)
        eligible = ((attendance >= 75 and fee_paid and assignment_submitted and no_disciplinary) or
                    (attendance >= 65 and medical_certificate and fee_paid and assignment_submitted and no_disciplinary))

        result = "✅ Eligible for exam" if eligible else "❌ Not eligible"

    return render_template("index.html", result=result)
