from pyecharts.charts import BMap
from pyecharts import options as opts

from parse_xml import get_coordinate_list

# 不习惯链式调用的开发者依旧可以单独调用方法
bmap = BMap()
bmap.add_schema(baidu_ak='GvrsNgKWZokjb1yG7gOphfmHFsrBn8AL', center=[113.975994,22.59844],
zoom=16)
coordinate_list = get_coordinate_list('build/my-data.xml')
bunch_points = [[str(i), 1] for i in range(len(coordinate_list))]
for i, v in enumerate(coordinate_list):
    bmap.add_coordinate(str(i), v[0], v[1])
bmap.add('shenzhen', bunch_points, label_opts=opts.LabelOpts(is_show=False))

bmap.set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
bmap.render()

