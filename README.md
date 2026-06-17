# NGO Donation Data Dashboard

## Overview

The NGO Donation Data Dashboard is a data analysis project built using Python and Streamlit. It helps analyze donation data and visualize trends through interactive charts.

## Features

* View donation dataset
* Calculate total donations
* Category-wise donation analysis
* Monthly donation trends
* Donation share visualization using pie charts

## Technologies Used

* Python
* Pandas
* Matplotlib
* Streamlit

## Project Structure

```
NGO-Donation-Data-Dashboard/
│
├── data/
│   └── donations.csv
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

## Dataset Columns

* Donor_Name
* Amount
* Category
* Date
* City

## Output

The dashboard displays:

* Donation dataset table
* Total donation amount
* Category-wise donation bar chart
* Monthly donation trend line chart
* Donation share pie chart

## Conclusion

This project demonstrates how data analysis and visualization can help NGOs understand donation patterns and support better fundraising decisions.
