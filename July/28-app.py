import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr 
import ollama 

def eda_analysis(file_path):
    df = pd.read_csv(file_path)  #This line defines a function named eda_analysis. This is the main function that will be called by the Gradio interface.reads the CSV file into a Pandas DataFrame.
    
    for col in df.select_dtypes(include=['number']).columns:  #Selects all columns in the DataFrame that have a numerical data type.
        df[col].fillna(df[col].median(),inplace=True)  #For each numerical column, it calculates the median of that column and then uses fillna() to replace any NaN (Not a Number, representing missing values) with that median. inplace=True modifies the DataFrame directly.
       
    for col in df.select_dtypes(include=['object']).columns: 
        df[col].fillna(df[col].mode()[0], inplace=True)  #For each categorical column, it calculates the mode (most frequent value) of that column. df[col].mode() can return multiple modes if there's a tie, so [0] selects the first one. Then, fillna() replaces any NaN values with this mode. inplace=True modifies the DataFrame directly.
        
    summary = df.describe(include='all').to_string()  #This method computes descriptive statistics for all columns in the DataFrame, including both numerical and categorical data (e.g., count, unique, top, freq for categorical columns).,,Converts the resulting summary DataFrame into a plain string format, which is suitable for display in the Gradio interface and for sending to the AI model.
    
    missing_values = df.isnull().sum().to_string()  #df.isnull(): Returns a DataFrame of boolean values, indicating True where a value is missing (NaN) and False otherwise.,.sum(): Sums the True values (which are treated as 1) for each column, effectively counting the number of missing values per column.,.to_string(): Converts this Series of missing value counts into a string.
    
    insights = generate_ai_insights(summary)
    
    plot_paths = generate_visualizations(df)
    
    return f"\n Data Loaded Successfully! \n\n Summary:\n{summary} \n\n Missing Values:\n{missing_values}\n\n AI Insights:\n{insights}",plot_paths

def generate_ai_insights(df_summary):
    prompt = f"Analyze the dataset summary and provide  insights:\n\n{df_summary}"  #this line constructs the prompt string for the AI model. It instructs the model to "Analyze the dataset summary and provide insights" and then includes the df_summary string.
    response = ollama.chat(model="mistral", messages=[{'role':'user','content':prompt}])  #This line sends the prompt to the AI model using the ollama.chat function. It specifies the model to use (in this case, "mistral") and provides the messages in a format that includes the user's input.
    return response['message']['content']  #This line extracts the content of the AI's response from the response dictionary and returns it.

def generate_visualizations(df):
    plot_paths = []
    
    for col in df.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col],bins=30,kde=True,color='pink')
        plt.title(f"Distribution of {col}")
        path = f"{col}_distribution.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()  
        # This block generates histograms for each numeric column in the DataFrame. It uses seaborn's histplot to create a histogram with a kernel density estimate (KDE) overlay, saves the plot as a PNG file, and appends the file path to the plot_paths list.
        
    numeric_df = df.select_dtypes(include=['number'])  #This line creates a new DataFrame containing only the numeric columns from the original DataFrame.
    if not numeric_df.empty:  #Checks if the numeric DataFrame is not empty before proceeding to generate a correlation heatmap.
        plt.figure(figsize=(8,5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        path = "correlation_heatmap.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()  #This block generates a correlation heatmap for the numeric columns in the DataFrame, saves it as a PNG file, and appends the file path to the plot_paths list.
        
    return plot_paths  

demo = gr.Interface(
    fn=eda_analysis,  #Specifies that the eda_analysis function should be executed when the user interacts with the Gradio interface (e.g., uploads a file and clicks a button).
    inputs = gr.File(type="filepath"),  #Defines the input component for the Gradio interface. In this case, it allows users to upload a file, and the type is set to "Filepath" so that the function receives the file path as a string.
    outputs=[gr.Textbox(label="EDA Report"),gr.Gallery(label="Data Visualizations")],  #Defines the output components for the Gradio interface. The first output is a textbox labeled "EDA Report" where the analysis results will be displayed, and the second output is a gallery labeled "Data Visualizations" where generated plots will be shown.
    title="LLM-Powered Exploratory Data Analysis (EDA)",#Sets the title of the Gradio interface.
    description = "Upload ur file Broo!! and get automated EDA insights with AI-powered analysis and visualizations."
)

demo.launch()