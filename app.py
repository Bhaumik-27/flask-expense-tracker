from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Location of CSV file (saved in same folder as app.py)
FILENAME = os.path.join(os.path.dirname(__file__), "expense.csv")
FIELDS = ["Date", "Product", "Amount", "Payer"]

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)

ensure_file()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        date = request.form.get("date", "")
        product = request.form.get("product", "")
        amt = request.form.get("amount", "")
        payer = request.form.get("payer", "")

        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, product, amt, payer])

        return redirect(url_for("view_expenses"))
    return render_template("add.html")

@app.route("/view")
def view_expenses():
    rows = []
    with open(FILENAME, "r", newline="") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if r]  # skip empty lines

    headers = rows[0] if rows else FIELDS
    data = rows[1:] if len(rows) > 1 else []

    # compute total of Amount column (best-effort parsing)
    total = 0.0
    for r in data:
        try:
            total += float(r[2])
        except Exception:
            pass

    return render_template("view.html", headers=headers, rows=data, total=total)

if __name__ == "__main__":
    app.run(debug=True)
