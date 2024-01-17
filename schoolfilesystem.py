#Libraries you may need:
# import csv, collections, dictionary, (pandas as pd), urlopen, etc..
import csv
import pandas as pd
import PyPDF2
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import matplotlib.pyplot as plt
#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self,url):
        # self.data_file = data_file
        self.data = pd.DataFrame()
        self.url = url
    def process_file(file_path):
        file_extension = os.path.splitext(file_path)[1]
        try:
            if file_extension == ".csv":
                data = pd.read_csv(file_path)
            elif file_extension == ".xlsx":
                data = pd.read_excel(file_path)
            elif file_extension in [".txt", ".log"]:  # Example for plain text formats
                with open(file_path, "r") as f:
                    data = f.read()
            else:
                raise ValueError("Unsupported file format")
            return data

        except FileNotFoundError:
            print(f"Error: File not found at path: {file_path}")
            return None
        except Exception as e:
            print(f"Error processing file: {e}")
            return None
# Example usage:
    file_path = "data.csv"  # Replace with your actual file path
    processed_data = process_file(file_path)

    if processed_data is not None:
    # Proceed with further processing or analysis of the data
        print(processed_data)
    else:
        print("File processing failed.")

    # def transfer_data():
    def transfer_data(input_files, output_file):
    # Define the criteria for data transfer
        criteria = lambda row: row['Score'] >= "70"

    # Initialize an empty list to store the merged data
        merged_data = []

    # Process each input file
        for file_name in input_files:
            with open(file_name, 'r') as input_file:
            # Read data from the CSV file
                reader = csv.DictReader(input_file)
                for row in reader:
                # Apply the predefined criteria
                    if criteria(row):
                    # Add data to the merged_data list
                        merged_data.append(row)

    # Write the merged data to the output file
        with open(output_file, 'w', newline='') as output_file:
            fieldnames = merged_data[0].keys() if merged_data else []  # Assumes at least one row in merged_data
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        # Write header
            writer.writeheader()

        # Write data
            writer.writerows(merged_data)

    if __name__ == "__main__":
    # Example usage
        input_files = ["data_file1.csv", "data_file2.csv", "data_file3.csv"]
        output_file = "output_merged_data.csv"

    # Check if input files exist
        if all(os.path.isfile(file) for file in input_files):
            transfer_data(input_files, output_file)
            print(f"Data transfer successful. Merged data saved to {output_file}.")
        else:
            print("Error: One or more input files do not exist.")
    def fetch_web_data(self):
        try:
            # Fetch the HTML content from the school's webpage
            html_content = urlopen(self.url).read()
            
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract relevant information (modify this based on your needs)
            assessment_info = soup.find('div', class_='assessment-info').text.strip()
            student_scores = soup.find('table', class_='student-scores')
            # ... extract other relevant details

            # Process the data (print or save to a file, database, etc.)
            self.process_data(assessment_info, student_scores)

        except Exception as e:
            print(f"Error: {e}")

    def process_data(self, assessment_info, student_scores):
        # Example: Print extracted data
        print("Assessment Information:")
        print(assessment_info)

        if student_scores:
            print("\nStudent Scores:")
            for row in student_scores.find_all('tr')[1:]:  # Skip the header row
                columns = row.find_all('td')
                student_name = columns[0].text.strip()
                score = columns[1].text.strip()
                print(f"{student_name}: {score}")
        else:
            print("\nNo student scores found.")

if __name__ == "__main__":
    # Example usage
    school_url = "https://www.aupp.edu.kh/"
    web_scraper = SchoolAssessmentSystem(school_url)
    web_scraper.fetch_web_data()

class SchoolSystemContentAnalysis:
    def __init__(self, data_file):
        self.data_file = data_file

    def analyze_content(self):
        try:
            # Load assessment data from a CSV file into a Pandas DataFrame
            df = pd.read_csv(self.data_file)

            # Display the first few rows of the DataFrame for a quick overview
            print("Assessment Data Overview:")
            print(df.head())

            # Generate statistical summaries
            print("\nStatistical Summaries:")
            print(df.describe())

            # Calculate class averages
            class_averages = df.groupby('Subject')['Score'].mean()
            print("\nClass Averages:")
            print(class_averages)

            # Visualize individual student performance
            self.plot_student_performance(df)

        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: Empty data in file '{self.data_file}'.")
        except Exception as e:
            print(f"Error: {e}")

    def plot_student_performance(self, df):
        # Visualize individual student performance using a boxplot
        plt.figure(figsize=(10, 6))
        plt.title('Student Performance Distribution')
        plt.boxplot(df['Score'], vert=False)
        plt.xlabel('Score')
        plt.show()

if __name__ == "__main__":
    # Example usage
    data_file = "assessment_data.csv"
    content_analysis = SchoolSystemContentAnalysis(data_file)
    content_analysis.analyze_content()

class SchoolSystemSummarization:
    def __init__(self, data_file):
        self.data_file = data_file
    def generate_summary(self):
    # def summarize_assessment_activities(self):
        try:
            # Load assessment data from a CSV file into a Pandas DataFrame
            df = pd.read_csv(self.data_file)

            # Display key insights
            print("Key Insights:")
            self.display_key_insights(df)

            # Visualize class performance
            self.plot_class_performance(df)

        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: Empty data in file '{self.data_file}'.")
        except Exception as e:
            print(f"Error: {e}")

    def display_key_insights(self, df):
        # Calculate overall average score
        overall_average = df['Score'].mean()
        print(f"\nOverall Average Score: {overall_average:.2f}")

        # Identify areas of improvement (subjects with lowest average scores)
        lowest_subject = df.groupby('Subject')['Score'].mean().idxmin()
        lowest_average = df.groupby('Subject')['Score'].mean().min()
        print(f"\nArea of Improvement: {lowest_subject} (Average Score: {lowest_average:.2f})")

        # Identify outstanding achievements (subjects with highest average scores)
        highest_subject = df.groupby('Subject')['Score'].mean().idxmax()
        highest_average = df.groupby('Subject')['Score'].mean().max()
        print(f"\nOutstanding Achievement: {highest_subject} (Average Score: {highest_average:.2f})")

    def plot_class_performance(self, df):
        # Visualize class performance using a bar chart
        subject_averages = df.groupby('Subject')['Score'].mean()

        plt.figure(figsize=(10, 6))
        plt.bar(subject_averages.index, subject_averages)
        plt.title('Class Performance by Subject')
        plt.xlabel('Subject')
        plt.ylabel('Average Score')
        plt.show()

if __name__ == "__main__":
    # Example usage
    data_file = "assessment_data.csv"
    summarization = SchoolSystemSummarization(data_file)
    summarization.generate_summary()

# # Analyze content & display result area
