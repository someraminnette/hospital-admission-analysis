
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset (synthetic example)
data = {
    "Patient_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [25, 34, 67, 45, 23, 56, 78, 34, 21, 50],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male"],
    "Reason_for_Admission": [
        "Infection", "Cardiac", "Infection", "Orthopedic", "Infection", "Cardiac", "Orthopedic", "Infection", "Cardiac", "Orthopedic"
    ],
    "Length_of_Stay": [3, 5, 7, 10, 2, 4, 8, 3, 5, 6],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Analyze Most Common Reasons for Admission
admission_counts = df["Reason_for_Admission"].value_counts()
print("\nMost Common Reasons for Admission:")
print(admission_counts)

# Step 3: Calculate Average Length of Stay by Condition
avg_stay = df.groupby("Reason_for_Admission")["Length_of_Stay"].mean()
print("\nAverage Length of Stay by Condition:")
print(avg_stay)

# Step 4: Visualize Patient Demographics
# Gender distribution
gender_counts = df["Gender"].value_counts()
plt.figure(figsize=(6, 4))
gender_counts.plot(kind="bar", color=["#1f77b4", "#ff7f0e"])
plt.title("Gender Distribution")
plt.ylabel("Number of Patients")
plt.xlabel("Gender")
plt.show()

# Age distribution
plt.figure(figsize=(6, 4))
plt.hist(df["Age"], bins=5, color="#2ca02c", alpha=0.7)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()
