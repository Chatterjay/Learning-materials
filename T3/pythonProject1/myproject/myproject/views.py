# chart_app/views.py
from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Line

def line_chart_view(request):
    x_data = ["一月", "二月", "三月", "四月", "五月", "六月", "七月"]
    y_data = [10, 20, 35, 40, 25, 30, 18]

    chart = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis("系列一", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="折线图示例"))
    )

    return render(request, 'line_chart.html', {'chart': chart.render_embed()})