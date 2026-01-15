# SmartDataKit---A-Custom-Pandas-Wrapper
A lightweight, chainable Pandas wrapper for fast financial data cleaning, outlier handling, and monthly analytics.

Motivation

Data scientists and analysts spend up to 80% of their time cleaning data. Raw pandas code often becomes verbose and hard to maintain.
SmartDataKit abstracts common financial data-wrangling operations into readable, reusable methods—so you can focus on insights, not boilerplate

Key Features

Method Chaining – Clean, filter, and analyze data in a single line
Automatic Currency Parsing – Converts "$1,200.50" → 1200.50
Outlier Handling – Removes extreme values using statistical thresholds
Stateful Design – Internal DataFrame state is preserved across operations
Beginner-Friendly API – Clean syntax, easy to extend

Installation 
git clone https://github.com/SandeepKumarPatra/SmartDataKit---A-Custom-Pandas-Wrapper.git
cd SmartDataKit---A-Custom-Pandas-Wrapper
pip install pandas numpy


Then run:

python main.py
