from flask import Flask, request, render_template
from config import LocalDevelopmentConfig
from search_propertiess import search_properties
import tensorflow as tf
import random
import numpy as np
import pandas as pd

app = Flask(__name__)
from model import *
app = None
UPLOAD_FOLDER="static/uploads"
def create_app():
    app=Flask(__name__)
    print("starting local development")
    app.config.from_object(LocalDevelopmentConfig)
    app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
    db.init_app(app)
    app.app_context().push()
    return app

app=create_app()


@app.route('/seeeearch', methods=['GET','POST'])
def search():

    # Get the form data from the request
    location = request.form['location']
    property_type = request.form['property_type']
    new_or_old = request.form['new_or_old']
    bath = request.form['bath']
    bhk = request.form['bhk']
    furnished = request.form['furnished']
    min_budget = request.form['min_budget']
    max_budget = request.form['max_budget']
    
    #give me a random number between 1 and 100
    number=random.randint(1,6)


    # Perform the property search
    # print( location +" " + property_type+" " + new_or_old+" " + bath+" " + bhk+" " + furnished+" " + min_budget+" " + max_budget)
    lhouses = db.session.query(houses).filter(houses.locality == location, houses.bathroom == bath, houses.bhk == bhk, houses.price.between(min_budget, max_budget)).all()
    print(lhouses)
    if lhouses:
        return render_template('listings.html', houses=lhouses,number=number)
    else:
        return "HI"
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('sell.html')
    if request.method == 'POST':
        year=request.form['year']
        l=list()
        l.append(int(year))
        year=l
        year=np.array(year)
        year=year.astype(int)
        print(year)
        area=np.array(list(request.form['areacode']))
        area=area.astype(int) 
        bhk=np.array(list(request.form['bhk']))
        bhk=bhk.astype(int)  
        bathroom=np.array((request.form['bathroom']))
        bathroom=bathroom.astype(int)
        rooms= np.array([15])
        rooms=rooms.astype(int)
        areatotal = np.array([4000])
        areatotal=areatotal.astype(int)    
        print(areatotal)
        new_data = pd.DataFrame({
            'AreaCode': area,
            'Bedroom': bhk,
            'Bath': bathroom,
            'TotalRooms': rooms,
            'YrSold': year,
            'TotalArea': areatotal,
        })
        model=tf.keras.models.load_model('classifier.hdf5')
        predicted_prices = model.predict(new_data)
        predicted_prices = predicted_prices.tolist()
        print(type(predicted_prices))
        predicted_prices=str(predicted_prices[0][0])
        print(predicted_prices)
        return render_template('sell.html',predicted_prices=predicted_prices)


@app.route('/answer', methods=['GET','POST'])
def answer():
    model=tf.keras.models.load_model('classifier.hdf5')
    new_data = pd.DataFrame({
    'AreaCode': [1],
    'Bedroom': [4],
    'Bath': [4],
    'TotalRooms': [15],
    'YrSold': [2008],
    'TotalArea': [4000],
})
    model=tf.keras.models.load_model('../buy3/classifier.hdf5')
    predicted_prices = model.predict(new_data)
    predicted_prices = predicted_prices.tolist()
    print(type(predicted_prices))
    return str(predicted_prices[0][0])

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
