import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Create Sample Dataset
# -------------------------------
data = {
    'Student_ID': range(1, 21),
    'Name': ['Student'+str(i) for i in range(1, 21)],
    'Gender': ['Male','Female']*10,
    'Age': [15,16,17,15,16,17,16,15,17,16,15,16,17,15,16,17,15,16,17,16],
    'Class': ['10th']*10 + ['12th']*10,
    'Math_Score': [65,78,90,55,49,82,71,88,69,73,59,66,85,72,64,91,53,87,79,68],
    'Science_Score': [72,64,81,58,92,77,85,69,74,88,63,70,84,91,68,79,60,75,80,67],
    'English_Score': [70,85,67,90,74,82,65,88,79,83,76,80,69,84,91,73,77,81,75,86],
    'Attendance': [92,88,95,78,85,90,96,89,91,87,93,88,94,89,90,97,86,92,88,95]
}

df = pd.DataFrame(data)
df.to_csv("student_performance.csv", index=False)
print("Sample dataset created: student_performance.csv")

# -------------------------------
# Step 2: Load Dataset
# -------------------------------
data = pd.read_csv("student_performance.csv")
print("\nFirst 5 rows of dataset:")
print(data.head())

# -------------------------------
# Step 3: Data Cleaning
# -------------------------------
data['Attendance'] = data['Attendance'].fillna(data['Attendance'].mean())

# -------------------------------
# Step 4: Add Average Score & Pass/Fail Status
# -------------------------------
data['Average_Score'] = data[['Math_Score', 'Science_Score', 'English_Score']].mean(axis=1)
data['Status'] = data['Average_Score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# -------------------------------
# Step 5: Visualizations
# -------------------------------

# Subject-wise Average Score
subject_avg = data[['Math_Score', 'Science_Score', 'English_Score']].mean()
plt.figure(figsize=(6,4))
subject_avg.plot(kind='bar', color=['#4CAF50','#2196F3','#FF9800'])
plt.title('Subject-wise Average Scores')
plt.ylabel('Average Score')
plt.show()

# Gender Distribution
plt.figure(figsize=(5,5))
data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

# Attendance vs Average Score
plt.figure(figsize=(6,4))
sns.scatterplot(x='Attendance', y='Average_Score', hue='Gender', data=data)
plt.title('Attendance vs Average Score')
plt.show()

# Top 10 Students
top_students = data.sort_values(by='Average_Score', ascending=False).head(10)
print("\nTop 10 Students by Average Score:")
print(top_students[['Name', 'Average_Score']])

# Save cleaned data
data.to_csv("student_performance_cleaned.csv", index=False)
print("\nCleaned data saved as student_performance_cleaned.csv")
