
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class AirQualityAnalysis:

    def __init__(self):
        self.__data = None

        self.pollutants = [
            "CO(GT)",
            "C6H6(GT)",
            "NOx(GT)",
            "NO2(GT)"
        ]

        self.measurement_columns = [
            "CO(GT)",
            "PT08.S1(CO)",
            "NMHC(GT)",
            "C6H6(GT)",
            "PT08.S2(NMHC)",
            "NOx(GT)",
            "PT08.S3(NOx)",
            "NO2(GT)",
            "PT08.S4(NO2)",
            "PT08.S5(O3)",
            "T",
            "RH",
            "AH"
        ]

    # 1. Load Dataset
    def load_dataset(self):

        try:
            self.__data = pd.read_csv(
                "air_quality.csv",
                sep=None,
                engine="python",
                decimal=","
            )

            # Clean Column Names
            self.__data.columns = (
                self.__data.columns.str.strip().str.replace(
                    "\ufeff", "", regex=False
                )
            )

            # Convert Measurement Columns to Numeric
            for column in self.measurement_columns:
                self.__data[column] = pd.to_numeric(
                    self.__data[column],
                    errors="coerce"
                )

            # Replace -200 with NaN
            self.__data[self.measurement_columns] = (
                self.__data[self.measurement_columns].replace(
                    -200, np.nan
                )
            )

            # Display Missing Values Before Handling
            print("\nMissing Values Before Handling:")
            print(self.__data.isnull().sum())

            # Fill Missing Values Using Median
            for column in self.measurement_columns:
                median_value = self.__data[column].median()

                if pd.notna(median_value):
                    self.__data[column] = (
                        self.__data[column].fillna(median_value)
                    )

            # Display Missing Values After Handling
            print("\nMissing Values After Handling:")
            print(self.__data.isnull().sum())

            # Create DateTime Column
            self.__data["DateTime"] = pd.to_datetime(
                self.__data["Date"].astype(str) + " " +
                self.__data["Time"].astype(str).str.replace(
                    ".", ":", regex=False
                ),
                format="%d/%m/%Y %H:%M:%S",
                errors="coerce"
            )

            print("\nDataset Loaded Successfully!")

            print("\nDataset Columns:")
            print(self.__data.columns.tolist())

            print("\nFirst 5 Records:")
            print(self.__data.head())

            print("\nTotal Records:", len(self.__data))

        except FileNotFoundError:
            print("Dataset file not found!")

        except KeyError as e:
            print("Required Column Not Found:", e)
            self.__data = None

        except Exception as e:
            print("Error:", e)
            self.__data = None

    # 2. Calculate Metrics
    def calculate_metrics(self):

        if self.__data is None:
            print("Please load the dataset first!")
            return

        print("\n========== AIR QUALITY METRICS ==========")

        for column in self.pollutants:

            print("\n", column)
            print("Average:", self.__data[column].mean())
            print("Maximum:", self.__data[column].max())
            print("Minimum:", self.__data[column].min())

    # 3. Filter Data
    def filter_data(self):

        if self.__data is None:
            print("Please load the dataset first!")
            return

        print("\n1. Filter by CO")
        print("2. Filter by NO2")
        print("3. Filter by NOx")
        print("4. Filter by Benzene")

        choice = input("Enter your choice: ")

        columns = {
            "1": "CO(GT)",
            "2": "NO2(GT)",
            "3": "NOx(GT)",
            "4": "C6H6(GT)"
        }

        if choice not in columns:
            print("Invalid Choice!")
            return

        column = columns[choice]

        try:
            value = float(input("Enter minimum value: "))

            result = self.__data[
                self.__data[column] >= value
            ]

            print("\nFiltered Data:")
            print(result.head(20))

            print("\nTotal Records:", len(result))

        except ValueError:
            print("Please enter a valid number!")

    # 4. Display Summary
    def display_summary(self):

        if self.__data is None:
            print("Please load the dataset first!")
            return

        print("\n========== DATASET SUMMARY ==========")

        print("\nFirst 5 Records:")
        print(self.__data.head())

        print("\nStatistical Summary:")
        print(self.__data.describe())

        print("\nMissing Values:")
        print(self.__data.isnull().sum())

        print("\nDataset Information:")
        self.__data.info()

        print("\nTotal Records:", len(self.__data))

        print("Total Columns:", len(self.__data.columns))

    # 5. Show Charts
    def show_charts(self):

        if self.__data is None:
            print("Please load the dataset first!")
            return

        pollutants = self.pollutants

        # Bar Chart
        average = self.__data[pollutants].mean()

        # Pie Chart
        co_data = self.__data["CO(GT)"].dropna()

        categories = pd.cut(
            co_data,
            bins=[0, 2, 5, float("inf")],
            labels=["Low", "Medium", "High"]
        )

        # Line Chart
        data = self.__data.dropna(
            subset=["DateTime", "CO(GT)"]
        ).sort_values("DateTime")

        # Heatmap
        correlation = self.__data[
            pollutants + ["T", "RH", "AH"]
        ].corr()

        # Display All Charts
        plt.figure(figsize=(14, 10))

        # 1. Bar Chart
        plt.subplot(2, 2, 1)
        average.plot(kind="bar")
        plt.title("Average Pollutant Levels")
        plt.xlabel("Pollutants")
        plt.ylabel("Average Value")
        plt.xticks(rotation=45)
        plt.tight_layout()


        # 2. Pie Chart
        plt.subplot(2, 2, 2)
        categories.value_counts().plot(
            kind="pie",
            autopct="%1.1f%%"
        )
        plt.title("CO Level Distribution")
        plt.ylabel("")
        plt.tight_layout()


        # 3. Line Chart
        plt.subplot(2, 2, 3)
        plt.plot(data["DateTime"], data["CO(GT)"])
        plt.title("CO Levels Over Time")
        plt.xlabel("Date")
        plt.ylabel("CO Level")
        plt.xticks(rotation=45)
        plt.tight_layout

        # 4. Heatmap
        plt.subplot(2, 2, 4)
        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm"
        )
        plt.title("Air Quality Correlation")

        plt.tight_layout()
        plt.show()
        

# Main Program

obj = AirQualityAnalysis()

while True:

    print("\n========== AIR QUALITY ANALYSIS ==========")

    print("1. Load Dataset")
    print("2. Calculate Metrics")
    print("3. Filter Data")
    print("4. Display Summary")
    print("5. Show Charts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.load_dataset()

    elif choice == "2":
        obj.calculate_metrics()

    elif choice == "3":
        obj.filter_data()

    elif choice == "4":
        obj.display_summary()

    elif choice == "5":
        obj.show_charts()

    elif choice == "6":
        print("\nThank You for Using Air Quality Analysis!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
