import pandas as pd

def merge(flex_file, index_name, filter, output_file):
    flex_df = pd.read_csv(flex_file)
    index_df = pd.read_csv(index_name)
    #index_df.drop('Unnamed: 0', inplace=True, axis=1)

    filtered_df = flex_df[flex_df['SYMBOL'].str.contains(filter, na=False)]
    #filtered_df = filtered_df.to_frame()
    filtered_df.to_csv('filtered_df.csv')
    filtered_df = pd.read_csv('filtered_df.csv')
    
    #merged_df = pd.merge(index_df, filtered_df, on='DATE', how='inner')
    merged_df = filtered_df.merge(index_df, how='inner', on='DATE')
    #print(filtered_df)
    #print(merged_df)

    """
    iterates through each row in the index report file and adds the dates into a list
    IMPORTANT: itterows() returns a tuple in the form of [index, row] so access row information by specifying column
    """
    #dates = []
    #for index, row in index_df.iterrows():
    #    dates.append(row['Date'])
    
    #df_output = index_df[index_df['Date'].isin(flex_df['DATE'])]
    #print(df_output)
    #merged_df = flex_df.merge(index_df, how = 'inner', on = ['DATE'])
    #print(flex_df)
    #print(index_df)
    #print(merged_df)
    merged_df.to_csv(output_file)

def merge(flex_file, filter, output_file):
    flex_df = pd.read_csv(flex_file)
    #index_df.drop('Unnamed: 0', inplace=True, axis=1)

    filtered_df = flex_df[flex_df['SYMBOL'].str.contains(filter, na=False)]
    #filtered_df = filtered_df.to_frame()
    filtered_df.to_csv('filtered_df.csv')
    filtered_df = pd.read_csv('filtered_df.csv')
    
    #merged_df = pd.merge(index_df, filtered_df, on='DATE', how='inner')
    #merged_df = filtered_df.merge(index_df, how='inner', on='DATE')
    #print(filtered_df)
    #print(merged_df)

    """
    iterates through each row in the index report file and adds the dates into a list
    IMPORTANT: itterows() returns a tuple in the form of [index, row] so access row information by specifying column
    """
    #dates = []
    #for index, row in index_df.iterrows():
    #    dates.append(row['Date'])
    
    #df_output = index_df[index_df['Date'].isin(flex_df['DATE'])]
    #print(df_output)
    #merged_df = flex_df.merge(index_df, how = 'inner', on = ['DATE'])
    #print(flex_df)
    #print(index_df)
    #print(merged_df)
    #merged_df.to_csv(output_file)


flex_file = input('Enter flex report file path: ')
#index_file = input('Enter underlying stock file path: ')
filter = input('Enter filter: ')
output_file = input('Enter name of output file: ')

merge(flex_file, filter, output_file)