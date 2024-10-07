import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("./medicine_sales_data.csv")
    df.dropna()
    df.sort_values(by='YearMonth')
    df.reset_index(drop=True,inplace=True)
    YM = df['YearMonth'].tolist()
    TC = df['TraditionalChineseMedicineSales'].tolist()
    WM = df['WesternMedicineSales'].tolist()
    print(YM)
    print(TC)
    print(WM)

