from multiprocessing import connection
from re import search
import sqlite3
import csv
import io
from flask import Flask, render_template, request, redirect, url_for, flash, Response

app = Flask(__name__)
app.secret_key = "expense-tracker-secret"

def get_db_connection():
    connection = sqlite3.connect("instance/expenses.db")
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

@app.route("/")
def home():

    search = request.args.get("search", "").strip()
    min_amount = request.args.get("min_amount", "").strip()
    max_amount = request.args.get("max_amount", "").strip()
    from_date = request.args.get("from_date", "").strip()
    to_date = request.args.get("to_date", "").strip()

    connection = get_db_connection()

    # Build expense query
    query = "SELECT * FROM expenses WHERE 1=1"
    params = []

    # Search by title or category
    if search:
        query += " AND (title LIKE ? OR category LIKE ?)"
        params.extend([
            f"%{search}%",
            f"%{search}%"
        ])

    # Minimum amount
    if min_amount:

        try:
            min_amount = float(min_amount)
        except ValueError:
            flash("Minimum amount must be a number.", "error")
            return redirect(url_for("home"))

        if min_amount < 0:
            flash("Minimum amount cannot be negative.", "error")
            return redirect(url_for("home"))

        query += " AND amount >= ?"
        params.append(min_amount)

    # Maximum amount
    if max_amount:

        try:
            max_amount = float(max_amount)
        except ValueError:
            flash("Maximum amount must be a number.", "error")
            return redirect(url_for("home"))

        if max_amount < 0:
            flash("Maximum amount cannot be negative.", "error")
            return redirect(url_for("home"))

        query += " AND amount <= ?"
        params.append(max_amount)

    # Check amount range
    if min_amount and max_amount and min_amount > max_amount:
        flash(
            "Minimum amount cannot be greater than maximum amount.",
            "error"
        )
        return redirect(url_for("home"))

    # From date
    if from_date:
        query += " AND date >= ?"
        params.append(from_date)

    # To date
    if to_date:
        query += " AND date <= ?"
        params.append(to_date)

    # Sort results
    query += " ORDER BY date DESC"

    # Get filtered expenses
    expenses = connection.execute(
        query,
        params
    ).fetchall()

    # Calculate total expenses
    total = connection.execute(
        "SELECT SUM(amount) FROM expenses"
    ).fetchone()[0]

    if total is None:
        total = 0

    # Count expenses
    count = connection.execute(
        "SELECT COUNT(*) FROM expenses"
    ).fetchone()[0]

    # Calculate category totals
    category_totals = connection.execute(
        """
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()
    monthly_totals = connection.execute(
    """
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(amount) AS total
    FROM expenses
    GROUP BY month
    ORDER BY month DESC
    """
).fetchall()

    connection.close()

    return render_template(
    "home.html",
    expenses=expenses,
    total=total,
    count=count,
    category_totals=category_totals,
    monthly_totals=monthly_totals
    )
@app.route("/export")
def export_expenses():

    connection = get_db_connection()

    expenses = connection.execute(
        """
        SELECT id, title, amount, category, date
        FROM expenses
        ORDER BY date DESC
        """
    ).fetchall()

    connection.close()

    output = io.StringIO()

    writer = csv.writer(output)

    # CSV header
    writer.writerow([
        "ID",
        "Title",
        "Amount",
        "Category",
        "Date"
    ])

    # CSV data
    for expense in expenses:

        writer.writerow([
            expense["id"],
            expense["title"],
            expense["amount"],
            expense["category"],
            expense["date"]
        ])

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=expenses.csv"
    )

    return response
@app.route("/add", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        title = request.form["title"].strip()
        amount = request.form["amount"]
        category = request.form["category"].strip()
        date = request.form["date"]

        if not title or not amount or not category or not date:
            flash("All fields are required.", "error")
            return redirect(url_for("add_expense"))

        try:
            amount = float(amount)
        except ValueError:
            flash("Amount must be a number.", "error")
            return redirect(url_for("add_expense"))

        if amount <= 0:
            flash("Amount must be greater than 0.", "error")
            return redirect(url_for("add_expense"))

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO expenses (title, amount, category, date)
            VALUES (?, ?, ?, ?)
            """,
            (title, amount, category, date)
        )

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    return render_template("add_expense.html")
@app.route("/delete/<int:id>")
def delete_expense(id):

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM expenses WHERE id=?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    connection = get_db_connection()

    expense = connection.execute(
        "SELECT * FROM expenses WHERE id=?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        title = request.form["title"]
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]

        connection.execute(
            """
            UPDATE expenses
            SET title=?, amount=?, category=?, date=?
            WHERE id=?
            """,
            (title, amount, category, date, id)
        )

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    connection.close()

    return render_template(
        "edit_expense.html",
        expense=expense
    )
@app.route("/view/<int:id>")
def view_expense(id):

    connection = get_db_connection()

    expense = connection.execute(
        "SELECT * FROM expenses WHERE id=?",
        (id,)
    ).fetchone()

    connection.close()

    if expense is None:
        flash("Expense not found.", "error")
        return redirect(url_for("home"))

    return render_template(
        "view_expense.html",
        expense=expense
    )
if __name__ == "__main__":
    init_db()
    app.run(debug=True)