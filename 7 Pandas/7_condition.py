import pandas as pd 
df = pd.read_csv('5_datarokok.csv')

# print(df)
# print(df.shape)

# ======================

# menampilkan data yg kolom 2015-nya max
# print(df[df['2015'] == df['2015'].max()])

# menampilkan data yg kolom 2015-nya >= rata2nya
# print(df[df['2015'] >= df['2015'].mean()])

# menampilkan provinsi yg kolom 2015-nya > rata2
# print(df['Provinsi'][df['2015'] >= df['2015'].mean()])

# menampilkan data provinsi & 2015, yg 2015-nya >= rata2
# print(df[['Provinsi', '2015']][df['2015'] >= df['2015'].mean()])

# menampilkan data player yg skill overall >= 90 & clubnya Real Madrid
# df[['Name', 'Position', 'Club', 'Overall']][df['Overall'] >= 90][df['Club'] == 'Real Madrid']