import pandas
import matplotlib.pyplot as plt
def dfSummary(data):
    try:
        return data.describe()  #statistical summary
    except:
        print("Unable to provide statistical summary.",err)
def colBoxPlot(data):
    for col in range(0,len(data.columns)):
        try:
            floatdata=data[col].astype(float) #try to convert each column to float and create box plot
        except ValueError as err:
            print("Unable to create box plot for column",col,'\t',err)     
        else:
            floatdata.plot.box()
