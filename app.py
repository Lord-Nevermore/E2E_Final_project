from flask import Flask, request
import joblib
import numpy

MODEL_PATH = 'ml_models/model_1/model.pkl'
SCALER_X_PATH = 'ml_models/model_1/scaler_x.pkl'
SCALER_Y_PATH = 'ml_models/model_1/scaler_y.pkl'

MODEL_PATH_2 = 'ml_models/model_2/model_2.pkl'
SCALER_X_PATH_2 = 'ml_models/model_2/scaler_x_2.pkl'
SCALER_Y_PATH_2 = 'ml_models/model_2/scaler_y_2.pkl'


app = Flask(__name__)

@app.route("/predict_price", methods = ['GET'])
def predict():
    args = request.args
    model = args.get('model', default=-1, type=int)
    
    open_plan = args.get('open_plan', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    renovation = args.get('renovation', default=-1, type=int)
    time_gap = args.get('time_gap', default=-1, type=int)


    if model == -1 or open_plan == -1 or rooms == -1 or area ==-1 or renovation == -1 or time_gap == -1:
            return "FATAL ERROR code:405 => lack of parameters"
        
    elif model == 1:
        #response = "rooms:{}, area:{}, renovation:{}".format(rooms, area, renovation)
        model = joblib.load(MODEL_PATH)
        sc_x = joblib.load(SCALER_X_PATH)
        sc_y = joblib.load(SCALER_Y_PATH)

        x = numpy.array([rooms,area,renovation]).reshape(1,-1)
        x = sc_x.transform(x)
        result = model.predict(x)
        result = sc_y.inverse_transform(result.reshape(1,-1))

        return str(result[0][0])

    elif model == 2:
        #response = "open_plan:{}, rooms:{}, area:{}, renovation:{}, time_gap{}".format(open_plan,rooms, area, renovation, time_gap)
        model2 = joblib.load(MODEL_PATH_2)
        sc_x2 = joblib.load(SCALER_X_PATH_2)
        sc_y2 = joblib.load(SCALER_Y_PATH_2)

        x2 = numpy.array([open_plan,rooms,area,renovation,time_gap]).reshape(1,-1)
        x2 = sc_x2.transform(x2)
        result2 = model2.predict(x2)
        result2 = sc_y2.inverse_transform(result2.reshape(1,-1))

        return str(result2[0][0])

    elif model != 1 or model != 2:
        return "You HAVE to choose/define the model(1-decision tree/2-randomforest)"  


if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')
