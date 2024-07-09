import pandas as pd
import glob

txt_files = glob.glob('*.txt')

for txt_file in txt_files:
    df = pd.read_fwf(txt_file)
    df.to_csv(txt_file)