import numpy as np
import pandas as pd
from django.shortcuts import render
from pyecharts.charts import Line, Bar, HeatMap
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts


def get_sales_data(request):
    df = pd.read_csv(r"/data/WALMART_SALES_DATA.csv")
    df.duplicated().sum()
    df.describe()
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")
    df["Year"] = df['Date'].dt.year
    df["Month"] = df['Date'].dt.month
    df = df[(df['Store'] == 1) | (df['Store'] == 2) | (df['Store'] == 3)]
    df['Store'].unique()
    df['Weekly_Sales'] = (df['Weekly_Sales'] / 10000).round(2)  # 转换成万单位保留两位小数点

    # 按年和商店分组计算总销售额
    total_sales_by_year_and_store = df.groupby(["Year", "Store"])['Weekly_Sales'].sum().unstack().fillna(0)
    # 计算每一年所有商店的总销售额
    total_sales_by_year = total_sales_by_year_and_store.sum(axis=1)
    # 计算每个商店在每一年的销售额占比
    sales_ratio_by_year_and_store = (total_sales_by_year_and_store.div(total_sales_by_year, axis=0) * 100).round(2)
    # 打印结果
    print("每一年每个商店的总销售额:")
    print(total_sales_by_year_and_store)

    print("每一年每个商店的销售额占比:")
    print(sales_ratio_by_year_and_store)

    # 创建折线图
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(total_sales_by_year_and_store.index.astype(str).tolist())
    )

    # 动态生成 .add_yaxis 方法调用
    for store in total_sales_by_year_and_store.columns:
        line.add_yaxis(
            f"商店{store}",
            total_sales_by_year_and_store[store].tolist(),
            # is_smooth=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            stack='stack1'
        )

    line.set_global_opts(
        title_opts=opts.TitleOpts(title="商店年销售额"),
        xaxis_opts=opts.AxisOpts(name="年份", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="销售额 (万元)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_right="2%"),
    )

    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(total_sales_by_year_and_store.columns.tolist())
        .add_yaxis("2010年", total_sales_by_year_and_store.loc[2010].tolist())
        .add_yaxis("2011年", total_sales_by_year_and_store.loc[2011].tolist())
        .add_yaxis("2012年", total_sales_by_year_and_store.loc[2012].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="商店年销售额对比"),
            xaxis_opts=opts.AxisOpts(name="商店"),
            yaxis_opts=opts.AxisOpts(name="销售额 (万元)"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_right="1%"),
        )
    )

    # 按年和月份分组计算总销售额
    total_sales_by_year_and_month = df.groupby(['Year', 'Month'])['Weekly_Sales'].sum().unstack().fillna(0).round(2)
    for column in total_sales_by_year_and_month.columns:
        mean_value = total_sales_by_year_and_month[column].replace(0.00, np.nan).mean()
        total_sales_by_year_and_month[column] = total_sales_by_year_and_month[column].replace(0.00, mean_value)

    heatmap_data = []
    for year in total_sales_by_year_and_month.index:
        for month in total_sales_by_year_and_month.columns:
            value = total_sales_by_year_and_month.loc[year, month]
            heatmap_data.append([str(year), str(month), value])

    heatmap = (
        HeatMap(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(total_sales_by_year_and_month.index.astype(str).tolist())
        .add_yaxis('月份', total_sales_by_year_and_month.columns.tolist(), heatmap_data)
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=total_sales_by_year_and_month.max().max(),
                                              min_=total_sales_by_year_and_month.min().min(), pos_left="right"),
            title_opts=opts.TitleOpts(title='热力图'),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="月份")
        )
    )

    df = pd.read_csv(r"/data/test.csv")

    df['销售额'] = df['销售额'].fillna(df['销售额'].mean())
    df['日期'] = pd.to_datetime(df['日期'])
    df['年'] = df['日期'].dt.year
    df['月'] = df['日期'].dt.month
    #  转换经济单位
    df['销售额'] = (df['销售额'] / 10000).round(2)
    print(df['商品类别'].value_counts())
    df['年'].sort_values(ascending=False).reset_index(drop=False)
    # 按照年月分组统计销售额
    total_sales_by_year_and_store2 = df.groupby(['年', '商品类别'])['销售额'].sum().unstack().fillna(0).round(2)

    # 计算总共销售额
    total_sales_by_year2 = total_sales_by_year_and_store2.sum(axis=1)

    # 计算销售占比
    sales_ratio_by_year_and_store2 = (total_sales_by_year_and_store2.div(total_sales_by_year, axis=0) * 100).round(2)

    # 每年的销售额
    print(total_sales_by_year_and_store2)
    # 计算每年占比
    print(sales_ratio_by_year_and_store2)

    line2 = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(total_sales_by_year_and_store2.index.astype(str).tolist())
    )
    for store in total_sales_by_year_and_store2:
        line2.add_yaxis(
            f"{store}",
            total_sales_by_year_and_store2[store].tolist(),
            areastyle_opts=opts.AreaStyleOpts(.3),
            # is_smooth=True,
            stack='stack1'
        )
    line2.set_global_opts(
        title_opts=opts.TitleOpts(title='药品销售数据'),
        xaxis_opts=opts.AxisOpts(name='年份', boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name='销售额(万元)', ),
        legend_opts=opts.LegendOpts(orient='vertical', pos_top="15%", pos_right="2%")
    )

    df = pd.read_csv(r'/data/cold_patient_data.csv')
    # 分离时间
    df['日期'] = pd.to_datetime(df['日期'])
    df['年'] = df['日期'].dt.year
    df['月'] = df['日期'].dt.month
    # 排序
    df = df.sort_values(['年', '月'], ascending=True).reset_index(drop=True)
    # 填补症状数据
    print(df['患者ID'].unique())

    df['年龄'] = df['年龄'].fillna(df['年龄'].mean())
    df['性别'] = df['性别'].fillna(df['性别'].mode()[0])
    df['症状'] = df['症状'].fillna(df['症状'].mode()[0])
    df = df[df['诊断'] == '是']
    # 无重复人员
    df = df.drop_duplicates(subset=['患者ID'])

    # 根据年月统计感冒的人数
    monthly_counts = df.groupby(['年', '月']).size().unstack().fillna(0)

    heatmap_data2 = []
    for year in monthly_counts.index:
        for month in monthly_counts.columns:
            value = monthly_counts.loc[year, month]
            heatmap_data2.append([str(year), str(month), int(value)])

    heatmap2 = (
        HeatMap(init_opts=InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(monthly_counts.index.tolist())
        .add_yaxis('', monthly_counts.columns.tolist(), heatmap_data2)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="感冒热力图"),
            xaxis_opts=opts.AxisOpts(name="年份", name_location='center', name_gap=30,
                                     name_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            yaxis_opts=opts.AxisOpts(name="月份", name_location='middle', name_gap=30,
                                     name_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            visualmap_opts=opts.VisualMapOpts(min_=int(monthly_counts.min().min()),
                                              max_=int(monthly_counts.max().max()),
                                              pos_top='15%', pos_right='2%'),
        )
    )

    return render(request, 'car_sales.html',
                  {"line": line.render_embed(), 'bar': bar.render_embed(), 'heatmap': heatmap.render_embed(),
                   'line2': line2.render_embed(), 'heatmap2': heatmap2.render_embed()})
