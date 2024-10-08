import pandas as pd
import numpy as np

# 生成症状和诊断结果
symptoms = ['发烧', '咳嗽', '流鼻涕', '头痛', '喉咙痛']
diagnosis_results = ['感冒', '流感', '肺炎', '普通感冒', '其他']

# 生成随机数据
np.random.seed(42)  # 确保结果可复现
num_samples = 1000

data = {
    '症状1': np.random.choice(symptoms, size=num_samples),
    '症状2': np.random.choice(symptoms, size=num_samples),
    '症状3': np.random.choice(symptoms, size=num_samples),
    '年龄': np.random.randint(0, 100, size=num_samples),
    '性别': np.random.choice(['男', '女'], size=num_samples),
    '诊断结果': np.random.choice(diagnosis_results, size=num_samples)
}

# 创建DataFrame
df_patients = pd.DataFrame(data)

# 保存为CSV文件
df_patients.to_csv(r"./patient_data.csv", index=False)

print("Patient data generated and saved to patient_data.csv")