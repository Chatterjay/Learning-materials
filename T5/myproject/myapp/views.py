import pandas as pd
from django.shortcuts import render
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def stacked_area_chart_view(request):
    df = pd.read_csv("D:\PyDemo\T5\myproject\data\mds.csv")
    df.dropna()
    df.sort_values(by='日期')
    df.reset_index(drop=True, inplace=True)
    x_axis = df['日期'].tolist()
    data1 = df['药品类型'].tolist()
    data2 = df['销售额'].tolist()

    # 创建图表
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_axis)
        .add_yaxis("系列1", data1, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        .add_yaxis("系列2", data2, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="堆叠面积图示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(),
        )
    )

    # 渲染模板并传递图表数据
    return render(request, 'index.html', {'line_chart': line.render_embed()})
    # return HttpResponse("Hello World!")