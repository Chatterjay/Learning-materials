import pandas as pd
from numpy import datetime64


read_data = './TestDate2.csv'

def rename_columns(df, old_name, new_name):
    """重命名指定列"""
    df.rename(columns={old_name: new_name}, inplace=True)
    return df

def sort_and_reset_index(df,name:str,sort=True):
    df.sort_values(by=name, inplace=True, ascending=sort)  # 默认升排序
    df.reset_index(drop=True, inplace=True)  # 重置索引

def main():
    missing_values = ["n/a", "na", "--", "-1", "-2"]
    df = pd.read_csv(read_data, na_values=missing_values)
    rename_columns(df,"购药时间","销售时间")
    df.dropna(inplace=True)
    # df[['销售数量','应收金额']] = df[['销售数量','应收金额']].astype(object) #更改对应类型
    try:
        df["销售时间"] = pd.to_datetime(df["销售时间"], format='mixed')
    except:
        df['销售时间'] = pd.to_datetime(df['销售时间'], errors='coerce')
        df.dropna(subset=['销售时间'], inplace=True)
    sort_and_reset_index(df, '销售时间')
    df.to_csv("./f.csv", encoding='utf-8-sig',index=False)
    print(df)



if __name__ == '__main__':
    main()
