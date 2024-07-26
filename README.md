# Goal
The goal of our project is to create and train a predictive model that can predict the prices and implied volatility of European vanilla flex options. So far we have extracted and formatted data of these option contracts into dataframes, estimated the implied volatility of each option contract using Newton's method, and created volatility surfaces for these contracts.
## Getting Started
### Checking Python Version
* Some of the libraries required for this repository to work correctly doesn't work unless you have an updated version of Python, run this line of code to make sure that you have version 2.7 or higher
```
python -V
```
### Download Python Libraries
* Install the following Python libraries by copy and pasting them into your terminal
```
pip install numpy
sudo apt-get install python3-scipy
pip install py_vollib
```
### Create Folder for Repo
* Create a folder where you would like to store the repository
```
mkdir options-theory
```
### Clone Repo into Folder
* Run this command to clone the repository into your desired folder using SSH
```
git clone git@github.com:kimmpy/options-theory.git
```
### Preparing Flex Reports
* Download all necessary flex reports and place them within the flex-reports folder and then organize them by months
* Create a two new directories for 'csv' files and 'txt' files
* For this example, the month of March will be used
```
cd flex-reports
mkdir 2024-03
cd 2024-03
mkdir csv txt
```
* Direct yourself into the 'txt' directory then run this command
* This clears all of the unnecessary headers in the files and then adds the correct headers
```
cd txt
for file in *
do
  grep -e "      2.*" -e "      4.*" "$file" > tmpfile
  mv tmpfile "$file"
  echo "   SYMBOL   P/C   EXPIRATION   STRIKE-PRICE   MARK-PRICE   OPEN-INTEREST" > tmpfile
  cat "$file" >> tmpfile
  mv tmpfile "$file"
done
```
* In order to add the 'DATE' and 'TIME-TO-EXPIRATION' columns, convert the 'EXPIRATION' column into DateTime, and also convert 'STRIKE-PRICE' to float, run the prepare_flex.py script
```
for file in flxopint.*.txt; do python ../../python-scripts/prepare_flex.py "$file"; done
```
* Move all of the new csv files into the 'csv' directory
```
mv *.csv ../csv
```
### Merging Flex and Index
* Download all of the index reports and then move them to the index-data directory
* Before you merge the flex and index files, you first need to merge all of the csv files into one DataFrame
* Direct yourself outside of the 'txt' directory then run the combine_dfs.py script
* The merged csv file will be output with the name of the directory as the file name
```
python ../../python-scripts/combine_dfs.py .
```
* Change directory into the merged-flex-index directory then run the merge_flex_index.py script
* This will filter through the rows in the combined DataFrame that matches the stock market symbol then it will merge it with the stock market's index report
* This will also rename all index columns into uppercase to match flex reports
* For this example, I will be using RUT
```
cd ../../merged-flex-index/
python ../python-scripts/merge_flex_index.py ../flex-reports/2024-03/2024-03.csv ../index-data/RUT.csv RUT
```
## Overview of Folders
* *flex-reports* - Flex reports organized by months. Inside of each folder for each month, there are separate folders containing txt files and their equivalent in csv format. The files outside of these folders are combined DataFrames for each month including one csv file with all three months.
* *index-data* - File for each stock market which contains data about the underlying stock.
* *merged-flex-index* - Merged index data with flex reports based on symbol.
* *iv* - Each folder contains one file with an added column for implied volatilities. Some folders contain png's of the volatility surfaces.
* *python-scripts* - All code used to make/format files.
