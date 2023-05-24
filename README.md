INTRODUCTION: The hotel industry is an essential part of the tourism industry. Understanding the trends and patterns of hotel booking can help businesses make informed decisions and improve their services. This report analyses the Hotel Booking dataset, which contains information about hotel bookings from two different hotels, a City hotel, and a Resort hotel, located in Portugal.

Data Exploration: The dataset contains 32 columns and 119,390 rows. The columns include information such as hotel type, booking dates, room type, meal type, and reservation status.

To explore the data, we used Python's Pandas and Matplotlib libraries. We started by importing the dataset and checking its shape, column names, and data types. We also checked for any missing values in the dataset. We found that the reservation status date column was in object data type, so we converted it into a datetime format for further analysis.

We also explored the categorical columns and their unique values. We found that there are two types of hotels in the dataset, five different market segments, and several customer types.


Data Analysis: We conducted various analyses on the dataset to gain insights into hotel bookings' trends and patterns.
Here are some of the findings:
![Screenshot 2023-05-24 163526](https://github.com/shruti2702/myportfolio/assets/130688987/a2b5711f-4f18-4899-b5ba-fd77922778bd)
![Screenshot 2023-05-24 163600](https://github.com/shruti2702/myportfolio/assets/130688987/007ea4d4-0928-4405-ac2f-a5edb8c53c35)

•	Cancelation Ratio: The dataset has 37% cancelled bookings and 63% not cancelled booking    . 
•	Cancelation by Hotel Type: The cancelation rate is higher in City hotels compared to Resort hotels.
•	Average Daily Rate (ADR): The ADR is higher in City hotels than Resort hotels. The ADR also varies throughout the year, with the highest rates in the summer months.
•	Cancelation by Market Segment: The cancelation rate varies by market segment, with Online Travel Agents having the highest cancelation rate.
•	Top 10 Countries with Cancelled Bookings: The top three countries with the highest number of cancelled bookings are Portugal, France, and the UK.
•	Reservation Status: The reservation status varies over time, with more cancellations in the summer months.


Conclusion: In conclusion, the Hotel Booking dataset provides valuable insights into hotel bookings trends and patterns. The analysis shows that cancelation rates vary by hotel type, market segment, and time of year. The ADR also varies throughout the year, and different market segments have different cancelation rates. Hotel businesses can use this information to improve their services and strategies to reduce cancelations and increase revenue.
Overall, this report highlights the importance of data analysis in the hotel industry and how it can help businesses make informed decisions.
