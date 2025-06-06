from flask import Flask, render_template, request

app = Flask(__name__)

# Load your model and data (do this once, outside the routes)
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',
                           companies=df['Company'].unique(),
                           types=df['TypeName'].unique(),
                           cpus=df['Cpu brand'].unique(),
                           gpus=df['Gpu brand'].unique(),
                           os_list=df['os'].unique(),
                           prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # get form data
    company = request.form.get('company')
    type_ = request.form.get('type')
    ram = int(request.form.get('ram'))
    weight = float(request.form.get('weight'))
    touchscreen = 1 if request.form.get('touchscreen') == 'Yes' else 0
    ips = 1 if request.form.get('ips') == 'Yes' else 0
    screen_size = float(request.form.get('screen_size'))
    resolution = request.form.get('resolution')
    cpu = request.form.get('cpu')
    hdd = int(request.form.get('hdd'))
    ssd = int(request.form.get('ssd'))
    gpu = request.form.get('gpu')
    os_ = request.form.get('os')

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # Create input array for model
    query = np.array([company, type_, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os_]).reshape(1, -1)

    # Predict log price then convert to actual price
    pred_log_price = pipe.predict(query)[0]
    predicted_price = int(np.exp(pred_log_price))

    # Render template with prediction
    return render_template('index.html',
                           companies=df['Company'].unique(),
                           types=df['TypeName'].unique(),
                           cpus=df['Cpu brand'].unique(),
                           gpus=df['Gpu brand'].unique(),
                           os_list=df['os'].unique(),
                           prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
