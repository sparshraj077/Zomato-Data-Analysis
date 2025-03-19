# Zomato-Data-Analysis
📌 Zomato Data Analysis (Bangalore Restaurants)
📖 Overview
This project aims to analyze restaurant data from Zomato to gain insights into Bangalore's food industry. Using Python libraries like Pandas, NumPy, Matplotlib, and Seaborn, we perform exploratory data analysis (EDA) to understand pricing, ratings, cuisine trends, and geographical distribution of restaurants.

🛠️ Technologies Used
Python
Pandas – Data manipulation and analysis
NumPy – Numerical computations
Matplotlib – Data visualization
Seaborn – Statistical data visualization
📊 Key Analysis & Insights
1️⃣ Distribution of Restaurant Ratings
Identify the average rating of restaurants in Bangalore.
Determine how ratings vary across cuisines and price categories.
2️⃣ Price Range vs. Rating Analysis
Analyze whether higher-priced restaurants have better ratings.
Visualize the trend between affordability and customer satisfaction.
3️⃣ Most Popular Cuisines in Bangalore
Identify the top cuisines served across different locations.
Determine which cuisines have the highest customer ratings.
4️⃣ Geographical Distribution of Restaurants
Identify the most restaurant-dense areas in Bangalore.
Visualize restaurant concentration in different neighborhoods.
5️⃣ Online vs. Offline Orders
Compare the popularity of online ordering across different areas.
Understand customer preferences for dine-in vs. delivery services.
🔥 Dataset Details
The dataset contains information on restaurants in Bangalore, including:
Name, Location, Ratings, Cost for Two, Cuisine Type, Votes, Online Delivery Availability, Table Booking, etc.
📌 How to Run the Project
1️⃣ Install Dependencies
bash
Copy
Edit
pip install pandas numpy matplotlib seaborn
2️⃣ Load the Dataset
python
Copy
Edit
import pandas as pd
df = pd.read_csv("zomato_bangalore.csv")
df.head()
3️⃣ Perform Data Analysis
python
Copy
Edit
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Distribution of Restaurant Ratings
plt.figure(figsize=(8, 5))
sns.histplot(df['Aggregate rating'], bins=30, kde=True, color='blue')
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.show()
📌 Expected Outcomes
✔️ Identify best-rated and affordable restaurants.
✔️ Understand customer preferences for online orders.
✔️ Visualize cuisine popularity and pricing trends.
✔️ Gain insights into restaurant density across Bangalore.

📌 Future Enhancements
🔹 Sentiment analysis on customer reviews
🔹 Machine learning model to predict restaurant success
🔹 Interactive visualizations using Streamlit or Dash

🤝 Contribution
Feel free to fork this repository and contribute by adding new features or improving the analysis.

📩 For any queries, contact Sparsh Rajvanshi.

