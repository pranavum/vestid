from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, user_logged_in
from . import db, generator
import matplotlib.pyplot as plt

url = Blueprint('url', __name__)

@url.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return render_template("home.html", user=current_user)
    return render_template("index.html", user=current_user)

@url.route('/new_model', methods=['GET', 'POST'])
def new_model():
    if request.method == 'POST':
        name = request.form.get("name")
        stock = request.form.get("stock")
        inputs = request.form.getlist("input")
        days = request.form.get("days")
        start = request.form.get("start")
        end = request.form.get("end")

        model = generator.generate_model(stock, inputs, days, start, end)
        dates_train, X_train, y_train, dates_val, X_val, y_val, dates_test, X_test, y_test = generator.generate_dataset(stock, inputs, days, start, end)

        train_predictions = model.predict(X_train).flatten()
        val_predictions = model.predict(X_val).flatten()
        test_predictions = model.predict(X_test).flatten()



        plt.plot(dates_train, train_predictions)
        plt.plot(dates_train, y_train)
        plt.plot(dates_val, val_predictions)
        plt.plot(dates_val, y_val)
        plt.plot(dates_test, test_predictions)
        plt.plot(dates_test, y_test)
        plt.legend(['Training Predictions', 
                    'Training Observations',
                    'Validation Predictions', 
                    'Validation Observations',
                    'Testing Predictions', 
                    'Testing Observations'])
        plt.show()
    return render_template("new_model.html", user=current_user)