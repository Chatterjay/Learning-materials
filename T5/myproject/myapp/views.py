import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from pandas import read_csv
from pyecharts.charts import Line, HeatMap
from pyecharts import options as opts
from pyecharts.globals import ThemeType


# Create your views here.
def line_chart_view(request):
    x_axis = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_axis = [820, 932, 901, 934, 1290, 1330, 1320]
    line = (
        Line()
        .add_xaxis(x_axis)
        .add_yaxis('销售额', y_axis, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="ECharts示例"))
    )
    return render(request, 'line_chart.html', {"line": line.render_embed()})


def line_chart_view2(req):
    # 读取CSV文件
    df = pd.read_csv(r"D:\PyDemo\T5\data\mds.csv")
    df.dropna(inplace=True)

    # 按日期排序
    df['日期'] = pd.to_datetime(df['日期'])
    df.sort_values(by='日期', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['年份'] = df['日期'].dt.year

    # 分别获取中成药和西药的销售额
    df_chinese = df[df['药品类型'] == '中成药']
    df_western = df[df['药品类型'] == '西药']
    # 每年总和
    chinese_sales = df_chinese.groupby('年份')['销售额'].sum().reset_index()
    western_sales = df_western.groupby('年份')['销售额'].sum().reset_index()

    x = chinese_sales['年份'].tolist()
    data_chinese:list = chinese_sales['销售额'].tolist()
    data_western:list = western_sales['销售额'].tolist()


    # 创建堆叠面积图
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x)
        .add_yaxis('中成药', data_chinese, areastyle_opts=opts.AreaStyleOpts(opacity=0.5), stack="stack1")
        .add_yaxis('西药', data_western, areastyle_opts=opts.AreaStyleOpts(opacity=0.5), stack="stack1")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="药品销售趋势"),
            tooltip_opts=opts.TooltipOpts(trigger='axis'),
            yaxis_opts=opts.AxisOpts(type_='value')
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(),
        )
    )

    return render(req, 'line_chart2.html', {'lines': line.render_embed()})


# 热力图
def heat_map(req):
    df = pd.read_csv(r"D:\PyDemo\T5\data\cold_cases.csv")
    df.dropna(inplace=True)

    # 年份月份排序
    df.sort_values(by=['年份', '月份'], inplace=True)
    # 获取唯一值
    years = df['年份'].unique().tolist()
    months = df['月份'].unique().tolist()

    # 准备热力图数据
    heatmap_data = []
    for year in years:
        for month in months:
            cases = df[(df['年份'] == year) & (df['月份'] == month)]['感冒病例数']
            heatmap_data.append([years.index(year), months.index(month), int(cases)])

    heatmap = (
        HeatMap(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(years)
        .add_yaxis("月份", months, heatmap_data, label_opts=opts.LabelOpts(is_show=True, position="inside"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="感冒高发期热力图"),
            visualmap_opts=opts.VisualMapOpts(max_=max(df['感冒病例数']), min_=min(df['感冒病例数']))
        )
    )
    return render(req, 'heat_map.html', {'heatmap': heatmap.render_embed()})
