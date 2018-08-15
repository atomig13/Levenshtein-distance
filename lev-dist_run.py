import pandas as pd
#Update the following line to read csv file
#data.df = pd.read_csv("XXXXXXX.csv",encoding = "ISO-8859-1", header=0)
data.df['Distance'] = ""

for cn in range(0,len(retailer)):
    s1 = data.df.iloc[cn,0]
    s2 = data.df.iloc[cn,1]
    try:
        d0 = edit_distance(s1, s2, substitution_cost=1, transpositions=False)
        data.df.iloc[cn,2] = d0
    except:
        pass