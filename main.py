import pickle 
from flask import Flask , render_template, request, redirect
from models import db, PredictionModel

model=pickle.load(open('model.pkl','rb'))

# Create an object of the Flask class 

app=Flask(__name__, template_folder='registrationform', static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///houseprediction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['Get','Post'])
def predict():
     # Retrieve form data
    variable1 = int(request.form.get('area'))
    variable2 = int(request.form.get('bedrooms'))
    variable3 = int(request.form.get('bathrooms'))
    variable4 = int(request.form.get('stories'))
    variable5 = int(request.form.get('mainroad'))
    variable6 = int(request.form.get('parking'))
    variable7 = int(request.form.get('prefarea'))
    variable8 = int(request.form.get('guestroom'))
    variable9 = int(request.form.get('basement'))
    variable10 = int(request.form.get('hotwaterheating'))
    variable11= int(request.form.get('airconditioning'))
    variable12= int(request.form.get('furnished'))
    variable13= int(request.form.get('semi-furnished'))
    variable14= int(request.form.get('unfurnished'))

    


    prediction=model.predict([[variable1,variable2,variable3,variable4,variable5,variable6,
    variable7,variable8,variable9,variable10,variable11,variable12,variable13,variable14]])

    output=round(prediction[0],2)
    return render_template('index.html', prediction_text=f'Total Price of house is :{output}/-')

    houseprediction=PredictionModel(
        area=variable1,
        bedrooms=variable2,
        bathrooms=variable3,
        stories=variable4,
        mainroad=variable5,
        parking=variable6,
        prefarea=variable7,
        guestroom=variable8,
        basement=variable9,
        hotwaterheating=variable10,
        airconditioning=variable11,
        furnished=variable12,
        semi_furnished=variable13,
        unfurnished=variable14,
        price=output       
    )

    db.session.add(houseprediction)
    db.session.commit()

if __name__=='__main__':
    app.run(debug=True)  
 
