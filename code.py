import statistics
import plotly.express as px
import csv
import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")

height=data["Height(Inches)"].tolist()
Weight = data ["Weight(Pounds)"].tolist()

meanHeight = statistics.mean(height)
meanWeight = statistics.mean(Weight)

medianHeight = statistics.median(height)
medianWeight = statistics.median(Weight)

modeHeight = statistics.mode(height)
modeWeight = statistics.mode(Weight)

print("Mean, Median and mode of Height are: " , meanHeight, medianHeight, modeHeight)
print("Mean, Median and mode of Weight are: " , meanWeight, medianWeight, modeWeight)


std_Height = statistics.stdev(height)
std_Weight = statistics.stdev(Weight)
print(".........................")
First_std_Height_start, First_std_Height_end = meanHeight - std_Height, meanHeight + std_Height
Second_std_Height_start, Second_std_Height_end = meanHeight - (2*std_Height), meanHeight + (2*std_Height)
Third_std_Height_start, Third_std_Height_end = meanHeight - (3*std_Height), meanHeight + (3*std_Height)


height_LOD_within_First_stdev = [result for result in height if result > First_std_Height_start and result < First_std_Height_end]
height_LOD_within_Second_stdev = [result for result in height if result > Second_std_Height_start and result < Second_std_Height_end]
height_LOD_within_Third_stdev = [result for result in height if result > Third_std_Height_start and result < Third_std_Height_end]

print("{}% of data for data lies within First Standard Deviation of Height", format(len(height_LOD_within_First_stdev)* 100.0 / len(height)))
print("{}% of data for data lies within Second Standard Deviation of Height", format(len(height_LOD_within_Second_stdev)* 100.0 / len(height)))
print("{}% of data for data lies within Third Standard Deviation of Height", format(len(height_LOD_within_Third_stdev)* 100.0 / len(height)))
print(".........................")

First_std_Weight_start, First_std_Weight_end = meanWeight - std_Weight, meanWeight + std_Weight
Second_std_Weight_start, Second_std_Weight_end = meanWeight - (2*std_Weight), meanWeight + (2*std_Weight)
Third_std_Weight_start, Third_std_Weight_end = meanWeight - (3*std_Weight), meanWeight + (3*std_Weight)

Weight_LOD_within_First_stdev = [result for result in Weight if result > First_std_Weight_start and result < First_std_Weight_end]
Weight_LOD_within_Second_stdev = [result for result in Weight if result > Second_std_Weight_start and result < Second_std_Weight_end]
Weight_LOD_within_Third_stdev = [result for result in Weight if result > Third_std_Weight_start and result < Third_std_Weight_end]

print("{}% of data for data lies within First Standard Deviation of Weight", format(len(Weight_LOD_within_First_stdev)* 100.0 / len(Weight)))
print("{}% of data for data lies within Second Standard Deviation of Weight", format(len(Weight_LOD_within_Second_stdev)* 100.0 / len(Weight)))
print("{}% of data for data lies within Third Standard Deviation of Weight", format(len(Weight_LOD_within_Third_stdev)* 100.0 / len(Weight)))