from api import sheet

get_Sheets(excel_name):


if __name__=="__main__":
    excel_name="【考研择校】东南大学2017-2023复试分数线.xlsx"
    sheet_name='2022'
    data_dict_list=sheet.get_Sheet(excel_name,sheet_name)
    # print(data_dict_list)
    for dict_item in data_dict_list:
        # 现在应该得到正确的字典结构
        print(dict_item)
        1