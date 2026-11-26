# Air Quality Analysis and Visualization

## 📌 Project Overview

Air Quality Analysis and Visualization is a Python-based data analysis project that analyzes air pollution measurements using Pandas, NumPy, Matplotlib, and Seaborn.

The project helps users understand pollutant levels, calculate statistical metrics, filter air quality records, handle missing values, and visualize data through different charts.

## 🎯 Project Objectives

- Load and analyze an air quality dataset.
- Calculate average, maximum, and minimum pollutant values.
- Filter records based on pollutant levels.
- Identify and handle missing values.
- Display dataset summaries.
- Visualize air quality measurements using charts.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## ✨ Features

### 1. Load Dataset
- Load the air quality CSV dataset.
- Display dataset columns and first five records.
- Display the total number of records.

### 2. Calculate Metrics
Calculate the following metrics for selected pollutants:

- Average
- Maximum
- Minimum

Pollutants:
- CO (Carbon Monoxide)
- C6H6 (Benzene)
- NOx (Nitrogen Oxides)
- NO2 (Nitrogen Dioxide)

### 3. Filter Data
Filter air quality records using a minimum value for:
- CO
- NO2
- NOx
- Benzene

### 4. Display Summary
Display:
- First five records
- Statistical summary
- Missing values
- Dataset information
- Total records and columns

### 5. Show Charts

The project displays four visualizations together:

1. **Bar Chart:** Average pollutant levels.
2. **Pie Chart:** CO concentration distribution (Low, Medium, High).
3. **Line Chart:** CO levels over time.
4. **Heatmap:** Correlation between pollutants and environmental measurements.

## 🧹 Missing Value Handling

The dataset uses `-200` to represent missing measurement values.

The project handles missing values by:

1. Replacing `-200` with `NaN`.
2. Displaying missing-value counts before handling.
3. Filling missing numeric measurement values using the median.
4. Displaying missing-value counts after handling.

## 📂 Project Structure

```text
Air-Quality-Analysis/
│
├── main.py
├── air_quality.csv
└── README.md
```

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## ▶️ How to Run

1. Download or clone the project.
2. Keep `air_quality.csv` in the same folder as `main.py`.
3. Open the project folder in VS Code or IDLE.
4. Run the following command:

```bash
python main.py
```

## 📋 Main Menu

```text
========== AIR QUALITY ANALYSIS ==========

1. Load Dataset
2. Calculate Metrics
3. Filter Data
4. Display Summary
5. Show Charts
6. Exit
```

## 🔗 Connect With Me

- **LinkedIn:** [Visit My LinkedIn Profile](https://www.linkedin.com/in/vaidika-ghoghari-2196a534a)
- **Email:** [Contact Me](mailto:ghogharivaidika@gmail.com)
- **Project Explanation Video:** [Watch Project Video](YOUR_VIDEO_URL)

## 👩‍💻 Author

**Vaidika Ghoghari**

Python | Data Analysis | NumPy | Pandas | Data Visualization

---

*This project is developed for learning and practicing Python data analysis and visualization techniques.*
