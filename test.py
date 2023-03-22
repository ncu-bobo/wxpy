import pandas as pd

# 读取Excel文件
df = pd.read_excel('resource/Am')

# 查找特定值所在的行和列
row_index, col_index = divmod((df == 'value').to_numpy().argmax(), len(df.columns))

# 打印结果
print(f"Value found at row {row_index} and column {chr(col_index + ord('A'))}")