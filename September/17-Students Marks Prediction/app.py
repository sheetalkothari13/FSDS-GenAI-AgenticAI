import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

'''
Flask → to create the app.
request → to read user input from HTML forms.
render_template → to load HTML files
joblib → to load the pre-trained ML model (saved as .pkl).
'''

app = Flask(__name__)
model = joblib.load(r"C:\Users\Sheetal\SheetalProjects\4. September\Students Marks Prediction\student_mark_predictor.pkl") # Load the pre-trained model. Make sure to provide the correct path to your .pkl file.

df = pd.DataFrame()  # Creates an empty DataFrame. Later, it will store the user inputs + predicted outputs and save them into a CSV file.

@app.route('/')
def home():
    return render_template('index2.html')    #@app.route('/') → defines the home page URL (http://127.0.0.1:5000/). When you open the homepage, it loads the index.html file.

@app.route('/predict',methods=['POST'])  
def predict():
    global df
    
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    #validate input hours
    if input_features[0] <0 or input_features[0] >24:
        return render_template('index2.html', prediction_text='Please enter valid hours between 1 to 24 if you live on the Earth')
        

    output = model.predict([features_value])[0].round(2)
    output = max(0, min(output, 100))

    # input and predicted value store in df then save in csv file
    df= pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    print(df)   
    df.to_csv(r"C:\Users\Sheetal\SheetalProjects\4. September\Students Marks Prediction\smp_data_from_app.csv", index=False)

    return render_template('index2.html', prediction_text='You will get {}% marks, when you study for {} hours per day '.format(output, int(features_value[0])))

'''
Defines a route /predict which is triggered by a POST request (form submission).
Uses global df to update the DataFrame defined outside the function.
request.form.values() → collects all values entered by the user in the HTML form.
Converts them to integers → input_features.
Converts into a numpy array (features_value) so the model can use it.
Checks if the number of study hours is realistic (between 0 and 24).
If invalid, it returns an error message on the HTML page.
[features_value] wraps the input into a 2D array (since sklearn models expect that).
[0][0] gets the first prediction (model output is nested).
round(2) → rounds to 2 decimal places.
Creates a new DataFrame with:
    "Study Hours" = user input
    "Predicted Output" = model’s prediction
Appends it to the global DataFrame df.
Prints the updated DataFrame in the terminal (for debugging).
Saves all results into a CSV file (smp_data_from_app.csv).
Sends the prediction back to the HTML page (index.html).
Displays a message 
'''

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
    
# Runs the Flask server on localhost (127.0.0.1) and port 5000.
#You can open it in browser at → http://127.0.0.1:5000/.
# we have used Linear regression model to predict the marks based on study hours.

# When StudyHours is very high, the formula just keeps increasing without any upper cap.
#That’s why you’re getting 140.85% — unrealistic but mathematically correct for linear regression.


