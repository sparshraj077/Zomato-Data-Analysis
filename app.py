from flask import Flask, request, render_template # type: ignore
import joblib # type: ignore
import numpy as np

app = Flask(__name__)


model = joblib.load('restaurant_model.pkl')

online_order_options = ['Yes', 'No']
book_table_options = ['Yes', 'No']
city_options = [
    'Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur', 'Brigade Road', 
    'Brookefield', 'BTM', 'Church Street', 'Electronic City', 'Frazer Town', 'HSR', 
    'Indiranagar', 'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli', 
    'Koramangala 4th Block', 'Koramangala 5th Block', 'Koramangala 6th Block', 
    'Koramangala 7th Block', 'Lavelle Road', 'Malleshwaram', 'Marathahalli', 'MG Road', 
    'New BEL Road', 'Old Airport Road', 'Rajajinagar', 'Residency Road', 'Sarjapur Road', 
    'Whitefield'
]
type_options = ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out', 'Drinks & nightlife', 'Pubs and bars']
cuisines_options = ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out', 'Drinks & nightlife', 'Pubs and bars']

@app.route('/')
def home():
    return render_template('index.html', online_order_options=online_order_options, 
                           book_table_options=book_table_options, city_options=city_options, 
                           type_options=type_options, cuisines_options=cuisines_options)

@app.route('/predict', methods=['POST'])
def predict():
    
    online_order = request.form.get('online_order')
    book_table = request.form.get('book_table')
    listed_in_city = request.form.get('listed_in_city')
    listed_in_type = request.form.get('listed_in_type')
    approx_cost = float(request.form.get('approx_cost'))
    cuisines = request.form.get('cuisines')

    
    online_order = 1 if online_order == 'Yes' else 0
    book_table = 1 if book_table == 'Yes' else 0
    listed_in_city = city_options.index(listed_in_city)
    listed_in_type = type_options.index(listed_in_type)
    cuisines = cuisines_options.index(cuisines)

    
    input_data = np.array([[online_order, book_table, listed_in_city, listed_in_type, approx_cost, cuisines]])
    
    
    prediction = model.predict(input_data)[0]

    
    formatted_prediction = round(prediction, 2)  
   

    return render_template('index.html', prediction_text=f'Predicted Rating: {formatted_prediction}', 
                           online_order_options=online_order_options, book_table_options=book_table_options, 
                           city_options=city_options, type_options=type_options, cuisines_options=cuisines_options)

if __name__ == '__main__':
    app.run(debug=True)
