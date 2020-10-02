from pyecharts.charts import BMap
from pyecharts import options as opts

from parse_xml import get_coordinate_list
baidu_log_offset = 0.010598
baidu_lat_offset = 0.00203
# 不习惯链式调用的开发者依旧可以单独调用方法
bmap = BMap(init_opts=opts.InitOpts(width='2000px', height='1000px'))
bmap.add_schema(baidu_ak='GvrsNgKWZokjb1yG7gOphfmHFsrBn8AL', center=[113.975994,22.59844],
zoom=16)
coordinate_list = get_coordinate_list('build/my-data.xml')
bunch_points = [[i[2], 1] for i in coordinate_list]
for i, v in enumerate(coordinate_list):
    bmap.add_coordinate(v[2], baidu_log_offset + v[0], baidu_lat_offset + v[1])
bmap.add('shenzhen', bunch_points, label_opts=opts.LabelOpts(is_show=False))

bmap.set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
bmap.render()

