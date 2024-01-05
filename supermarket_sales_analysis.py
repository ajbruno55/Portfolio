from pathlib import Path
import csv

import plotly.express as px

# Reading in data sourced from Kaggle.com (free open source data site)
path = Path('supermarket_sales.csv')
contents = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(contents)
header_row = next(reader)

# Gathering categories of each transaction
category = []
for row in reader:
    product_line = row[5]
    category.append(product_line)

# Making sure each category only appears once for the x axis of chart
set_category = sorted(set(category))

# Counting total number of transactions and assigning them to each category
transactions = []
for number in set_category:
    numbers = category.count(number)
    transactions.append(numbers)

# Creating bar chart with plotly to show results
labels = {'x' : 'Category', 'y' : 'Transactions'}
title = "Supermarket Transactions by Category"
fig = px.bar(y=transactions, x=set_category, title=title, labels=labels)
fig.show()
