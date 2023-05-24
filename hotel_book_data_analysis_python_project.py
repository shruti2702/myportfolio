
**importing libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""**loading the dataset**"""

df=pd.read_csv('/content/hotel_bookings 2.csv')

"""**exploratory data analysis and data cleaning**"""

df.head()  # shows the top 5 row of dataset
df.tail()  # shows the last 5 rows of dataset 
df.shape # shows number of rows and columns
df.columns # shows column name
df.info() # shows datatype

# coverting data suchas reservation status date was object but then convert it to datetime
#df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
df.info()
df.describe(include='object')    #describe with include This will generate a summary statistics DataFrame that includes information for all columns, including categorical columns.

#finding a object column and running loop on it and find the categorical column and unique values
for col in df.describe(include='object').columns:
  print(col)
  print(df[col].unique())  #first we are filtering the dataframme with the current column and then passing the unique function

#find the mising value
df.isnull().sum()

df.describe() #summary statistics

df=df[df['adr']<5000]

#is_canceled column data analysis wether the reservation is cancaeled or not its ratio
cancelled_perc=df['is_canceled'].value_counts(normalize=True) 
print(cancelled_perc)
plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.4)
plt.show()

#cancelation in comparison between resort hotels and city hotels
plt.figure(figsize=(8,4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Reds')
legend_labels,_ =ax1.get_legend_handles_labels()
ax1.legend(loc='upper right')
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()

#finding in percentage form the cancelation of resort reservation
resort_hotel= df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)

#finding in percentage form the cancelation of resort reservation
resort_hotel= df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)

#finding mean on city and resort on bases of adr column
resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# Plot for resort hotel
axes[0].set_title('Average Daily Rate for Resort Hotel', fontsize=20)
axes[0].plot(resort_hotel.index, resort_hotel['adr'], label='Resort Hotel')
axes[0].legend(fontsize=16)

# Plot for city hotel
axes[1].set_title('Average Daily Rate for City Hotel', fontsize=20)
axes[1].plot(city_hotel.index, city_hotel['adr'], label='City Hotel')
axes[1].legend(fontsize=16)

plt.show()

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=df,palette='bright')
legend_labels,_ =ax1.get_legend_handles_labels()
ax1.legend(loc='upper right')
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()

plt.figure(figsize=(10,8))
plt.title('ADR per month',fontsize=30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize=20)
plt.show()

cancelled_data=df[df['is_canceled']==1]
top_10_country=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(7,8))
plt.title('Top 10 Countries with reservation canceled')
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()

df['market_segment'].value_counts()

df['market_segment'].value_counts()

cancelled_data['market_segment'].value_counts(normalize=True)

cancelled_df = df[df['is_canceled'] == 1]
cancelled_df_adr = cancelled_df.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label='cancelled')
plt.legend(fontsize=20)
plt.show()

