import pandas as pd

# 1. Load raw dataset (IMPORTANT: sep=';')
data_path = "data/raw/student_data.csv"
df = pd.read_csv(data_path, sep=';')

# 2. Select only required columns
df = df[['studytime', 'absences', 'G1', 'G2', 'G3']]

# 3. Create performance label based on final grade (G3)
def performance_label(score):
    if score < 10:
        return "At-Risk"
    elif score < 15:
        return "Pass"
    else:
        return "Exceeds Expectations"

df['performance'] = df['G3'].apply(performance_label)

# 4. Rename columns for clarity
df.rename(columns={
    'studytime': 'hours_studied',
    'absences': 'attendance_issues',
    'G1': 'internal_1',
    'G2': 'internal_2',
    'G3': 'final_score'
}, inplace=True)

# 5. Save cleaned dataset
output_path = "data/processed/student_cleaned.csv"
df.to_csv(output_path, index=False)

print("✅ Data preprocessing completed successfully")
print(df.head())
