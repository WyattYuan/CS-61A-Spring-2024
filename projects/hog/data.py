import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def insert_points_with_linear_fit(data):
    # 确保数据是浮点数
    data = [float(x) for x in data]
    
    # 如果数据少于2个点，无法插值
    if len(data) < 2:
        return data
    
    # 创建结果列表，将会包含原始数据和插入的数据
    result = []
    
    # 遍历原始数据点，每两个点之间插入一个点
    for i in range(len(data) - 1):
        # 添加当前原始数据点
        result.append(data[i])
        
        # 计算当前点与下一点的中间值
        middle_point = (data[i] + data[i+1]) / 2
        result.append(middle_point)
    
    # 添加最后一个原始数据点
    result.append(data[-1])
    
    return result


def process_csv_file(file_path):
    try:
        # 读取CSV文件，处理可能存在的空白字符
        df = pd.read_csv(file_path, header=None, skipinitialspace=True)
        original_data = [float(x) for x in df[0].tolist()]

        # 处理数据
        new_data = insert_points_with_linear_fit(original_data)

        # 打印结果
        print("原始数据:", original_data)
        print("处理后数据:", new_data)

        # 检查线性趋势是否保持
        orig_model = LinearRegression().fit(
            np.arange(len(original_data)).reshape(-1, 1),
            np.array(original_data).reshape(-1, 1),
        )
        new_model = LinearRegression().fit(
            np.arange(len(new_data)).reshape(-1, 1), np.array(new_data).reshape(-1, 1)
        )
        print(f"原始数据斜率: {orig_model.coef_[0][0]:.4f}")
        print(f"处理后数据斜率: {new_model.coef_[0][0]:.4f}")

        # 保存结果
        result_df = pd.DataFrame(new_data)
        result_df.to_csv("output.csv", index=False, header=False)
        print("结果已保存到 output.csv")

        return new_data

    except FileNotFoundError:
        print("文件未找到，请检查文件路径")
    except Exception as e:
        print(f"发生错误: {str(e)}")
        raise e  # 重新抛出异常，方便调试


# 示例使用
if __name__ == "__main__":
    # 请将 'your_file.csv' 替换为实际的CSV文件路径
    file_path = "input.csv"
    process_csv_file(file_path)

    # 测试数据示例
    # test_data = [1, 3, 5, 7]
    # result = insert_points_with_linear_fit(test_data)
    # print("测试数据:", test_data)
    # print("测试结果:", result)
