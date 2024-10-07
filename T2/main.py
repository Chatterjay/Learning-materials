from pandas import read_csv
from pyecharts.charts import Bar


def sort_and_reset_index(df):
    """按销售时间排序并重置索引"""
    df.sort_values(by='销售时间', inplace=True, ascending=True)
    df.reset_index(drop=True, inplace=True)
    return df

def main():
    df = read_csv('药品消费数据.csv')
    df.dropna(inplace=True)
    sort_and_reset_index(df)
    # df.to_csv("./output.csv",encoding="utf-8-sig",index=False,)
    # print(df.head())
    bar_chart = Bar()



if __name__ == '__main__':
    main()