from django.shortcuts import render
from pyecharts.charts import Line
from pyecharts import options as opts

# Create your views here.
def line_chart_view(request):
    x_axis = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_axis = [820, 932, 901, 934, 1290, 1330, 1320]
    line = (
        Line()
        .add_xaxis(x_axis)
        .add_yaxis('销售额',y_axis,is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="ECharts示例"))
    )
    return render(request,'line_chart.html',{"line":line.render_embed()})