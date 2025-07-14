#we are going to design a simple front end using Streamlit

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

tips = sns.load_dataset("tips")

st.title('Sheetal Data Visualizations App')
st.write("This is a simple app to visualize the tips dataset using seaborn.")


#functionto create and display plot

def display_plot(title,plot_func):
    st.subheader(title)
    fig,ax = plt.subplots(figsize=(8,6))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)


#to plot the graph
def scatter_plot(ax):
    sns.scatterplot(data = tips, x='total_bill',y='tip',hue = 'time',size='size',palette="deep",ax=ax)
    ax.set_title("Scatterplot")

def line_plot(ax):
    sns.lineplot(data=tips,x = 'size', y = 'total_bill',hue = 'sex',ci = None,palette='dark',ax=ax)
    ax.set_title("line plot")

def bar_plot(ax):
    sns.barplot(data = tips,x = 'day',y = 'total_bill',hue = 'sex',palette='muted',ax=ax)
    ax.set_title("bar plot")

def box_plot(ax):
    sns.boxplot(data = tips,x = 'day',y = 'tip',hue = 'smoker',palette='pastel',ax=ax)
    ax.set_title("boxplot")

def violin_plot(ax):
    sns.violinplot(data = tips,x = 'day',y = 'total_bill',hue = 'time',split=True,palette='colorblind',ax=ax)
    ax.set_title("Violin plot")

def count_plot(ax):
    sns.countplot(data = tips,x = 'day',hue = 'smoker',palette='bright',ax=ax)
    ax.set_title('Count plot')

def reg_plot(ax):
    sns.regplot(data = tips,x = 'total_bill',y = 'tip',scatter_kws={'s':50,'color':'green'},line_kws={'color':'red'},ax=ax)
    ax.set_title('Regression plot')

def hist_plot(ax):
    sns.histplot(data = tips,x = 'total_bill',bins = 20,kde = True,color = 'maroon',ax=ax)
    ax.set_title("Histogram plot")

# def pair_plot(ax):
#     sns.pairplot(tips,hue='sex',vars=["total_bill","tip","size"], palette='husl', ax=ax)
#     ax.set_suptitle("pair plot: Numerical variables by gender",y = 1.02)

def strip_plot(ax):
    sns.stripplot(data=tips,x='day',y = 'tip',hue = 'sex',jitter=True, palette='Set1',ax=ax)
    ax.set_title('stripplot')

def kde_plot(ax):
    sns.kdeplot(data = tips,x = 'total_bill',hue = 'sex',fill = True, palette='tab10', ax=ax)
    ax.set_title('KDE plot')
    
# st.subheader("Select a plot")

display_plot("Scatter Plot",scatter_plot)
display_plot("Line Plot",line_plot)
display_plot("Bar Plot",bar_plot)
display_plot("Box Plot",box_plot)
display_plot("Violin Plot",violin_plot)
display_plot("Count Plot",count_plot)
display_plot("Regression Plot",reg_plot)
display_plot("Histogram Plot",hist_plot)
# display_plot("Pair Plot",pair_plot) 
display_plot("Strip Plot",strip_plot)
display_plot("KDE Plot",kde_plot)

















    