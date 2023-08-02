from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Page
import os

bh = [('北海市', 1)]
bj = [('北京市', 1)]
cd = [('成都市', 1)]
dy = [('德阳市', 1)]
gz = [('广州市', 1)]
gl = [('桂林市', 1)]
heb = [('哈尔滨市', 1)]
nj = [('南京市', 1)]
nn = [('南宁市', 1)]
qd = [('青岛市', 1)]
sh = [('上海市', 1)]
sz = [('深圳市', 1)]
suz = [('苏州市', 1)]
tj = [('天津市', 1)]
wh = [('武汉市', 1)]
xa = [('西安市', 1)]
aus = [('Australia', 1)]
dl = [('大连市', 1)]
xm = [('厦门市', 1)]

cn = (
    Map()
    .add("陈浩巍", bh, "china-cities")
    .add("李昊伦", bj, "china-cities")
    .add("陈炫廷", bj, "china-cities")
    .add("刘语溦", bj, "china-cities")
    .add("毛胤儒", bj, "china-cities")
    .add("李安乔", bj, "china-cities")
    .add("刘寒烛", cd, "china-cities")
    .add("廖璟生", dy, "china-cities")
    .add("井之涵", gz, "china-cities")
    .add("梁玉烨", gl, "china-cities")
    .add("裴靖雅", gl, "china-cities")
    .add("覃馨怡", heb, "china-cities")
    .add("陈科宏", nj, "china-cities")
    .add("罗喆", nn, "china-cities")
    .add("吉姝凝", nn, "china-cities")
    .add("杨宇翔", qd, "china-cities")
    .add("陈玥伽", sh, "china-cities")
    .add("林楚珊", sz, "china-cities")
    .add("刘翊嘉", suz, "china-cities")
    .add("梁欣怡", tj, "china-cities")
    .add("蔡沿恺", wh, "china-cities")
    .add("温浩然", wh, "china-cities")
    .add("张瑞滢", wh, "china-cities")
    .add("谭颖杉", xa, "china-cities")
    .add("李文羽", nn, "china-cities")
    .add("苏品乐", sh, "china-cities")
    .add("梁子耀", dl, "china-cities")
    .add("李诗羽", xm, "china-cities")
    .add("赵雨歆", sh, "china-cities")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

wo = (
    Map()
    .add("黄峙锟", aus, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

final_map = (
    Page(page_title = '13班蹭饭图')
    .add(cn)
    .add(wo)
    .render('index.html')
)

os.system('index.html')
