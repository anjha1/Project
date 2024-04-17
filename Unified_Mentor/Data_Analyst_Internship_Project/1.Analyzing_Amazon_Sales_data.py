"""Data Analyst - Internship Project
Description:
In this internship project, the primary objective is to gain hands-on experience in data analysis within the context of e-commerce sales data from Amazon. The project aims to provide valuable insights into sales trends, key metrics, and factors influencing revenue generation. Through the utilization of various tools and techniques, including Python for data manipulation and analysis, as well as visualization tools like Matplotlib and Power BI, the project aims to enhance skills in data analysis and presentation.

Key Objectives:
Data Extraction: Obtain the Amazon sales dataset and load it into a suitable data structure for analysis.

Data Transformation: Clean and preprocess the data, including converting date columns to datetime format and extracting relevant temporal features such as month, year, and year-month.

Data Analysis:

Explore sales trends on a month-wise, year-wise, and yearly-month-wise basis to understand the patterns and fluctuations in revenue over time.
Identify key metrics such as total revenue, total cost, and total profit to evaluate the financial performance of sales operations.
Conduct correlation analysis and regression techniques to uncover meaningful relationships between attributes and factors influencing sales performance.
Visualization:

Utilize Python libraries like Matplotlib to create visualizations such as bar charts and line plots to illustrate sales trends effectively.
Explore Power BI to create interactive dashboards and reports resembling professional business intelligence visualizations.
Insights and Recommendations:

Derive actionable insights from the analysis to guide decision-making processes aimed at optimizing sales management strategies.
Provide recommendations for improving sales performance, enhancing distribution methods, and reducing operational costs to increase profits.
Expected Learning Outcomes:
Gain proficiency in data manipulation and analysis using Python and pandas.
Develop skills in data visualization and presentation using Matplotlib and Power BI.
Understand the importance of sales management and its impact on business performance in the e-commerce domain.
Learn to derive actionable insights from data analysis to drive business decisions and strategies.
Project Duration:
The internship project is expected to span over a specified duration, during which interns will work on various tasks related to data analysis, visualization, and presentation. Regular feedback and guidance will be provided to ensure continuous learning and development throughout the internship period.

Project Deliverables:
Completed Python code for data extraction, transformation, analysis, and visualization.
Documentation detailing the analysis approach, methodologies, findings, and recommendations.
Presentation slides summarizing key insights and recommendations for stakeholders.
Evaluation Criteria:
Interns will be evaluated based on their ability to:

Successfully execute data analysis tasks using Python and visualization tools.
Demonstrate critical thinking and problem-solving skills in deriving insights from the data.
Effectively communicate findings and recommendations through documentation and presentations.
Conclusion:
The Data Analyst internship project offers a valuable opportunity to gain practical experience in data analysis within the e-commerce domain. Through hands-on tasks and real-world datasets, interns will develop essential skills in data manipulation, analysis, and visualization, while also contributing to meaningful insights that can drive business growth and success."""








import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("/content/Amazon Sales data.csv")

# Convert 'Order Date' to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Extract month, year, and year-month from 'Order Date'
data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Year_Month'] = data['Order Date'].dt.to_period('M')

# Calculate total profit
data['Total Profit'] = data['Total Revenue'] - data['Total Cost']

# Aggregate sales data by month, year, and year-month
monthly_sales = data.groupby('Order Month')['Total Revenue'].sum()
yearly_sales = data.groupby('Order Year')['Total Revenue'].sum()
yearly_monthly_sales = data.groupby('Order Year_Month')['Total Revenue'].sum()

# Print unique counts of months, years, and yearly-months
month_unique_count = data['Order Month'].nunique()
year_unique_count = data['Order Year'].nunique()
year_month_unique_count = data['Order Year_Month'].nunique()

print(f'Month unique count: {month_unique_count}')
print(f'Year unique count: {year_unique_count}')
print(f'Year_Month unique count: {year_month_unique_count}')

# Create a dataframe to store sales trends
sales_trend = pd.DataFrame({
    'Month': data['Order Month'].unique()[:min(month_unique_count, year_unique_count, year_month_unique_count)],
    'Year': data['Order Year'].unique()[:min(month_unique_count, year_unique_count, year_month_unique_count)],
    'Year_Month': data['Order Year_Month'].unique()[:min(month_unique_count, year_unique_count, year_month_unique_count)]
})

# Calculate total sales for each category
sales_trend['Total Sales'] = data.groupby('Order Month')['Total Revenue'].sum()
sales_trend['Total Sales_Year'] = data.groupby('Order Year')['Total Revenue'].sum()
sales_trend['Total Sales_Year_Month'] = data.groupby('Order Year_Month')['Total Revenue'].sum()

# Display sales trends dataframe
print(sales_trend)

# Plotting with Matplotlib
plt.figure(figsize=(12, 6))

# Monthly Sales Trend
plt.subplot(2, 2, 1)
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

# Yearly Sales Trend
plt.subplot(2, 2, 2)
yearly_sales.plot(kind='bar', color='lightgreen')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Sales')

# Yearly-Monthly Sales Trend
plt.subplot(2, 2, 3)
yearly_monthly_sales.plot(kind='line', marker='o', color='orange')
plt.title('Yearly-Monthly Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Sales')

plt.tight_layout()
plt.show()
