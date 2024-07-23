#Goal
The goal of our project is to create and train a predictive model that can predict the prices and implied volatility of European vanilla flex options. So far we have extracted and formatted data of these option contracts into dataframes, estimated the implied volatility of each option contract using Newton's method, and created volatility surfaces for these contracts.
##Getting Started
###Checking Python Version
*Some of the libraries required for this repository to work correctly doesn't work unless you have an updated version of Python, run this line of code to make sure that you have version 2.7 or higher
```
python -V
```
###Download Python Libraries
*Install the following Python libraries by copy and pasting them into your terminal
```
pip install numpy
sudo apt-get install python3-scipy
pip install py_vollib
```
###Create Folder for Repo
*Create a folder where you would like to store the repository
```
mkdir {folder name}
```
###Clone Repo into Folder
*Run this command to clone the repository into your desired folder using SSH
```
git clone git@github.com:kimmpy/options-theory.git
```
##Overview of Folders
**flex-reports* - Flex reports organized by months. Inside of each folder for each month, there are separate folders containing txt files and their equivalent in csv format. The files outside of these folders are combined DataFrames for each month including one csv file with all three months.
**index-data* - File for each stock market which contains data about the underlying stock.
**merged-flex-index* - Merged index data with flex reports based on symbol.
**iv* - Each folder contains one file with an added column for implied volatilities. Some folders contain png's of the volatility surfaces.
**python-scripts* - All code used to make/format files.
