import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "employee_attrition.csv"

try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"File {file_path} not found. Please check the path and try again.")
    st.stop()

st.title("📊 Employee Attrition Analysis Dashboard")

st.subheader("Dataset Preview")
st.dataframe(data)

# Convert categorical columns for better visualization
data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})

# 1. Overall Attrition Rate
st.subheader("📌 Overall Employee Attrition Rate")
attrition_rate = data['Attrition'].mean() * 100
st.write(f"**Attrition Rate:** {attrition_rate:.2f}%")

# 2. Attrition by Department
st.subheader("📌 Attrition by Department")
dept_attrition = data.groupby("Department")["Attrition"].mean() * 100
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=dept_attrition.index, y=dept_attrition.values, palette="coolwarm", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.title("Attrition Rate by Department")
st.pyplot(fig)

# 3. Attrition by Business Travel
st.subheader("📌 Attrition by Business Travel")
travel_attrition = data.groupby("BusinessTravel")["Attrition"].mean() * 100
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x=travel_attrition.index, y=travel_attrition.values, palette="magma", ax=ax)
plt.xlabel("Business Travel")
plt.ylabel("Attrition Rate (%)")
plt.title("Attrition Rate by Business Travel")
st.pyplot(fig)

# 4. Monthly Income Distribution
st.subheader("📌 Monthly Income Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data["MonthlyIncome"], kde=True, color="blue", bins=30, ax=ax)
plt.xlabel("Monthly Income")
plt.ylabel("Frequency")
plt.title("Monthly Income Distribution")
st.pyplot(fig)

# 5. Attrition by Job Role
st.subheader("📌 Attrition by Job Role")
job_attrition = data.groupby("JobRole")["Attrition"].mean() * 100
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=job_attrition.index, y=job_attrition.values, palette="viridis", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")
plt.title("Attrition Rate by Job Role")
st.pyplot(fig)

# 6. Work-Life Balance vs. Attrition
st.subheader("📌 Work-Life Balance vs. Attrition")
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x="WorkLifeBalance", y="Attrition", data=data, hue="WorkLifeBalance", legend=False, palette="coolwarm", ax=ax)
plt.xlabel("Work-Life Balance")
plt.ylabel("Attrition (1 = Yes, 0 = No)")
plt.title("Impact of Work-Life Balance on Attrition")
st.pyplot(fig)

# 7. Years at Company vs. Attrition
st.subheader("📌 Years at Company vs. Attrition")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data[data["Attrition"] == 1]["YearsAtCompany"], kde=True, color="red", bins=20, label="Attrition", ax=ax)
sns.histplot(data[data["Attrition"] == 0]["YearsAtCompany"], kde=True, color="blue", bins=20, label="No Attrition", ax=ax)
plt.xlabel("Years at Company")
plt.ylabel("Frequency")
plt.title("Years at Company Distribution for Attrition vs. Non-Attrition")
plt.legend()
st.pyplot(fig)

# 8. Satisfaction Scores Analysis
st.subheader("📌 Satisfaction Scores Analysis")
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(x="JobSatisfaction", y="Attrition", data=data, hue="JobSatisfaction", legend=False, palette="coolwarm", ax=ax[0])
ax[0].set_title("Job Satisfaction vs. Attrition")

sns.boxplot(x="EnvironmentSatisfaction", y="Attrition", data=data, hue="EnvironmentSatisfaction", legend=False, palette="coolwarm", ax=ax[1])
ax[1].set_title("Environment Satisfaction vs. Attrition")

sns.boxplot(x="WorkLifeBalance", y="Attrition", data=data, hue="WorkLifeBalance", legend=False, palette="coolwarm", ax=ax[2])
ax[2].set_title("Work-Life Balance vs. Attrition")

st.pyplot(fig)

# 9. Age Distribution
st.subheader("📌 Age Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data["Age"], kde=True, bins=30, color="green", ax=ax)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Employees")
st.pyplot(fig)

# Conclusion
st.markdown("## 🔍 Key Takeaways")
st.write("""
- **The Human Resources department has the highest attrition rate, followed by R&D and Sales.**
- **Employees who travel frequently for business have the highest attrition rate, while those who travel rarely or do not travel have significantly lower attrition.**
- **The monthly income distribution is right-skewed, indicating that most employees earn lower salaries, but there is a smaller group with high earnings. This could impact attrition, with lower-income employees possibly leaving more frequently.**
""")
