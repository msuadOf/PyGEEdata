import pandas as pd

def get_Sheet(excel_name,sheet_name="sheet1"):
    # 假设你的Excel文件路径和名称是'your_file.xlsx'
    df = pd.read_excel(excel_name,sheet_name=sheet_name, engine='openpyxl')  # 使用openpyxl引擎读取xlsx文件（默认引擎可能会根据pandas版本有所不同）

    # 处理缺失或无效的列名（如NaN）
    df.columns = df.columns.fillna('未知')  # 将NaN替换为'未知'或其他合适的占位符

    # 确保数据中无额外的非标题行
    if not df.iloc[0].isnull().all():
        # 如果第一行不是全为NaN，则可能有非标题行混入，需要处理
        # 假设第二行开始才是有效数据，移除第一行
        df = df.iloc[1:]

    data_dict_list = df.to_dict('records')
    return data_dict_list

if __name__=="__main__":
    excel_name="【考研择校】东南大学2017-2023复试分数线.xlsx"
    sheet_name='2022'
    data_dict_list=get_Sheet(excel_name,sheet_name)
    print(data_dict_list[0])
    for dict_item in data_dict_list:
        # 现在应该得到正确的字典结构
        # print(dict_item)
        1