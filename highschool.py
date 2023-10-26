# from pyecharts.render import make_snapshot
# from snapshot_selenium import snapshot
import os

from pyecharts import options as opts
from pyecharts.charts import Map

sz = [('苏州市',1)]
cd = [('成都市',1)]
bh = [('北海市',1)]
heb = [('哈尔滨市',1)]
nn = [('南宁市',1)]
wh = [('武汉市',1)]
bj = [('北京市',1)]
jn = [('济南市',1)]
sh = [('上海市',1)]
gl = [('桂林市',1)]
dl = [('大连市',1)]
cc = [('长春市',1)]

map2 = (
    Map()
    .add('甘忠义',sz,'china-cities')
    .add('王清莹',cd,'china-cities')
    .add('韦剑磊',bh,'china-cities')
    .add('温喜杰',heb,'china-cities')
    .add('邱苑彬',nn,'china-cities')
    .add('黄扬才',wh,'china-cities')
    .add('黄宇轩',wh,'china-cities')
    .add('陆诗绘',bj,'china-cities')
    .add('刘寒烛',cd,'china-cities')
    .add('莫睿琳',nn,'china-cities')
    .add('李志乐',jn,'china-cities')
    .add('黄锐翔',sh,'china-cities')
    .add('苏晓柔',nn,'china-cities')
    .add('李雨霏',nn,'china-cities')
    .add('蒙得悦',gl,'china-cities')
    .add('李琳',nn,'china-cities')
    .add('廖扬',gl,'china-cities')
    .add('陆芷莹',nn,'china-cities')
    .add('李光鑫',dl,'china-cities')
    .add('高肇艺',cc,'china-cities')
    .add('邓诚',nn,'china-cities')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render('202010.html')
)

os.system('202010.html')
# os.system('output.png')
