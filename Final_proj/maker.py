import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn import tree 

def preprocessing():
    df = pd.read_csv('car.csv')
    
    #delete unnecessary data columns
    df = df.drop(df.index[0]) #drop the label, say the first row , NOT IN PLACE
    del df['body_type']
    del df['color_slug']
    del df['stk_year']
    del df['date_created']
    del df['date_last_seen']
    df = df.dropna() #drop row with na value, NOT IN PLACE
    
    #print(df)
    car_name = df[['maker']]
    car_name.dtypes.value_counts()
    return df

def draw_PDF(df): #draw the pdf of each column
    df = df.mask(df.astype(object).eq('None')).dropna()
    sample_df = df.sample(n=1000)
    maker_count = sample_df.groupby(['maker']).size()
    
    print(maker_count)
    
    makers = maker_count.keys()
    maker_list = []
    count_list = []
    summ = 0
    for i in range(len(makers)):
        maker_list.append(makers[i])
        count_list.append(maker_count[i])
        summ = summ + maker_count[i]
    
    print(maker_list)
    print(count_list)
    
    plt.figure(figsize=(30,5))
    plt.plot(maker_list,count_list/summ)
    plt.tight_layout()
    plt.show()
        
if __name__ == '__main__':
    draw_PDF(preprocessing())
