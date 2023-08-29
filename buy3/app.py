from flask import Flask, request, render_template
from search_propertiess import search_properties
app = Flask(__name__)


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
    
    # Perform the property search
    print( location +" " + property_type+" " + new_or_old+" " + bath+" " + bhk+" " + furnished+" " + min_budget+" " + max_budget)
    results = search_properties("C:/Users/Madhav Pradhan/Downloads/buy3/MagicBricksedited.csv", location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget)
    
    if results:
        return results 
        return render_template('listings.html', results=results)
    else:
        return "results are not there"
        return render_template('no_results.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
