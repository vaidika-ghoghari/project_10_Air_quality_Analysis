# Air Quality Analysis and Visualization

A Python-based data analysis project that explores air pollution measurements using Pandas, NumPy, Matplotlib, and Seaborn. This project performs exploratory data analysis (EDA), calculates pollutant statistics, handles missing values, and visualizes air quality patterns through different charts.

## Project Overview

Air quality is an important environmental factor that affects human health and the environment. This project analyzes air quality measurements to understand pollutant concentrations and identify patterns in the dataset.

The project provides a simple menu-driven interface to load data, calculate statistical metrics, filter records, display dataset summaries, and generate visualizations.

## Objectives

- Analyze air quality data using Python.
- Calculate average, minimum, and maximum pollutant values.
- Filter records based on pollutant concentrations.
- Identify and handle missing values.
- Display dataset information and statistical summaries.
- Create visualizations to understand pollutant distributions and relationships.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

## Dataset

The project uses the Air Quality dataset containing air pollution measurements collected from an air quality monitoring station.

**Dataset Source:** [UCI Machine Learning Repository – Air Quality Dataset](https://archive.ics.uci.edu/dataset/360/air+quality)

The dataset contains measurements of several pollutants, including:

- CO – Carbon Monoxide
- C6H6 – Benzene
- NOx – Nitrogen Oxides
- NO2 – Nitrogen Dioxide

The dataset uses `-200` to represent missing measurement values.

## Features

### 1. Load Dataset

- Load the CSV dataset.
- Display the first five records.
- Display column names and total records.

### 2. Calculate Metrics

Calculate the following statistical metrics for selected pollutants:

- Average
- Maximum
- Minimum

### 3. Filter Data

Filter air quality records using minimum pollutant values for:

- CO
- NO2
- NOx
- Benzene

### 4. Display Dataset Summary

Display important information about the dataset:

- First five records
- Statistical summary
- Missing-value counts
- Dataset information
- Total records and columns

### 5. Data Cleaning

The dataset contains missing values represented by `-200`.

The project handles missing values by:

1. Replacing `-200` with `NaN`.
2. Displaying missing-value counts before handling.
3. Filling missing numeric measurement values using the median.
4. Displaying missing-value counts after handling.

### 6. Data Visualization

The project generates four visualizations:

| Chart | Purpose |
|---|---|
| Bar Chart | Compare average pollutant levels |
| Pie Chart | Show CO concentration categories |
| Line Chart | Visualize CO levels over time |
| Heatmap | Examine correlations between pollutants and environmental measurements |

## Project Structure

```text
project_10_air_quality_analysis/
│
├── main.py
├── air_quality.csv
└── README.md
```

## Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/vaidika-ghoghari/project_10_Air_quality_Analysis.git
```

2. Open the project folder:

```bash
cd project_10_Air_quality_Analysis
```

3. Make sure `air_quality.csv` is in the same folder as `main.py`.

4. Run the program:

```bash
python main.py
```

## Main Menu

The application provides the following options:

```text
========== AIR QUALITY ANALYSIS ==========

1. Load Dataset
2. Calculate Metrics
3. Filter Data
4. Display Summary
5. Show Charts
6. Exit
```

Select an option from the menu to perform the required analysis.

## Conclusion

This project demonstrates how Python libraries can be used to perform exploratory data analysis on air quality measurements.

Through data cleaning, statistical calculations, filtering, and visualization, the project helps understand pollutant concentrations and patterns in the dataset.

The visualizations provide a clear representation of pollutant levels, changes over time, and relationships between environmental measurements.

## Author

**Vaidika Ghoghari**

Python | Data Analysis | Pandas | NumPy | Data Visualization

## Connect With Me

- GitHub: [Vaidika Ghoghari](https://github.com/vaidika-ghoghari)
- LinkedIn: [Visit My LinkedIn Profile](https://www.linkedin.com/)
- Email: [ghogharivaidika@gmail.com](mailto:ghogharivaidika@gmail.com)

---

This project was developed for learning and practicing Python data analysis and visualization techniques.
