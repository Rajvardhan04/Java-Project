# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "✅ Chatbot server is running for Payroll System!"

# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     data = request.get_json()
#     message = data['message'].lower()

#     # Meaningful replies based on Payroll System
#     if "salary" in message:
#         reply = "💰 Full-time employees get a fixed monthly salary. Part-time employees are paid hourly based on their working hours."
#     elif "leave balance" in message or "leaves" in message:
#         reply = "🗓️ You have 12 paid leaves per year. For exact balance, check with HR or Payroll System records."
#     elif "holiday" in message or "holidays" in message:
#         reply = "🎉 We follow national holidays. The upcoming holiday is Independence Day on 15th August."
#     elif "employee list" in message or "all employees" in message:
#         reply = "👥 You can view the employee list in the Payroll System main menu under 'Display Employees'."
#     elif "policy" in message:
#         reply = "📃 Our company policy allows flexible work timings with prior approval from your manager."
#     elif "bye" in message or "exit" in message:
#         reply = "👋 Goodbye! Feel free to ask anytime."
#     else:
#         reply = "❓ Sorry, I didn't understand that. Please ask about salary, leaves, holidays, employee list, or policies."

#     return jsonify(reply)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy employee data
employees = {
    "101": {"name": "Rajvardhan Singh", "type": "Full Time", "salary": 5000, "leaves": 12},
    "102": {"name": "Atharav Shotriya", "type": "Part Time", "salary": 30*15, "leaves": 10}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    emp_id = request.form['emp_id']
    if emp_id in employees:
        return redirect(url_for('home', emp_id=emp_id))
    else:
        return "Invalid Employee ID"

@app.route('/home/<emp_id>')
def home(emp_id):
    emp = employees[emp_id]
    return render_template('home.html', emp=emp, emp_id=emp_id)

@app.route('/edit/<emp_id>')
def edit(emp_id):
    emp = employees[emp_id]
    return render_template('edit.html', emp=emp, emp_id=emp_id)

app.route('/update/<emp_id>', methods=['POST'])
def update(emp_id):
    emp = employees[emp_id]
    emp['name'] = request.form['name']
    emp['type'] = request.form['type']
    emp['salary'] = float(request.form['salary'])
    emp['leaves'] = int(request.form['leaves'])
    return f"✅ Profile updated for {emp['name']}! <a href='/home/{emp_id}'>Go back to Home</a>"

@app.route('/dashboard/<emp_id>')
def dashboard(emp_id):
    emp = employees[emp_id]
    return render_template('dashboard.html', emp=emp, emp_id=emp_id)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message'].lower()

    if "hello" in message or "hi" in message or "hey" in message:
        reply = "Hello! How can I assist you with your payroll queries today?"
    elif "salary" in message:
        reply = "Full-time employees get a fixed monthly salary. Part-time employees are paid hourly based on their working hours."
    elif "leave balance" in message or "leaves" in message:
        reply = "You have 12 paid leaves per year. For exact balance, check with HR or Payroll System records."
    elif "holiday" in message or "holidays" in message:
        reply = "We follow national holidays. The upcoming holiday is Independence Day on 15th August."
    elif "employee list" in message or "all employees" in message:
        reply = "You can view the employee list in the Payroll System main menu under 'Display Employees'."
    elif "policy" in message:
        reply = "Our company policy allows flexible work timings with prior approval from your manager."
    elif "office timings" in message:
        reply = "Office timings are 9 AM to 6 PM with flexible slots as per policy."
    elif "apply for leave" in message:
        reply = "You can apply for leave through the Payroll System portal or by sending a mail to HR."
    elif "contact hr" in message or "hr contact" in message:
        reply = "You can contact HR at hr@company.com or call extension 123."
    elif "manager" in message:
        reply = "Please contact HR to know your reporting manager."
    elif "salary credited" in message:
        reply = "Salaries are credited by the 5th of every month."
    elif "work from home" in message:
        reply = "Work from home is allowed twice a week with prior manager approval."

    elif "bye" in message or "exit" in message:
        reply = "Goodbye! Feel free to ask anytime."
    
    else:
        reply = "Sorry, I didn't understand that. Please ask about salary, leaves, holidays, employee list, or policies."

    return jsonify(reply)


if __name__ == '__main__':
    app.run(debug=True)
    
    # To run this file, print this in terminal:-
    # python App.py