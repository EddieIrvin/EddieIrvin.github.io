from pyecharts import options as opts

from pyecharts.charts import Map

from pyecharts.charts import Page

import os

n1 = [('北海市',1)]
n2 = [('北京市',1)]
n3 = [('成都市',1)]
n4 = [('德阳市',1)]
n5 = [('广州市',1)]
n6 = [('桂林市',1)]
n7 = [('哈尔滨市',1)]
n8 = [('南京市',1)]
n9 = [('南宁市',1)]
n10 = [('青岛市',1)]
n11 = [('上海市',1)]
n12 = [('深圳市',1)]
n13 = [('苏州市',1)]
n14 = [('天津市',1)]
n15 = [('武汉市',1)]
n16 = [('西安市',1)]
n17 = [('Australia',1)]
n18 = [('大连市',1)]
n19 = [('厦门市',1)]

cn = (
    Map()
    .add("陈浩巍",n1,"china-cities")
    .add("李昊伦",n2,"china-cities")
    .add("陈炫廷",n2,"china-cities")
    .add("刘语溦",n2,"china-cities")
    .add("毛胤儒",n2,"china-cities")
    .add("李安乔",n2,"china-cities")
    .add("刘寒烛",n3,"china-cities")
    .add("廖璟生",n4,"china-cities")
    .add("井之涵",n5,"china-cities")
    .add("梁玉烨",n6,"china-cities")
    .add("裴靖雅",n6,"china-cities")
    .add("覃馨怡",n7,"china-cities")
    .add("陈科宏",n8,"china-cities")
    .add("罗喆",n9,"china-cities")
    .add("吉姝凝",n9,"china-cities")
    .add("杨宇翔",n10,"china-cities")
    .add("陈玥伽",n11,"china-cities")
    .add("林楚珊",n12,"china-cities")
    .add("刘翊嘉",n13,"china-cities")
    .add("梁欣怡",n14,"china-cities")
    .add("蔡沿恺",n15,"china-cities")
    .add("温浩然",n15,"china-cities")
    .add("张瑞滢",n15,"china-cities")
    .add("谭颖杉",n16,"china-cities")
    .add("李文羽",n9,"china-cities")
    .add("苏品乐",n11,"china-cities")
    .add("梁子耀",n18,"china-cities")
    .add("李诗羽",n19,"china-cities")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

wo = (
    Map()
    .add("黄峙锟", n17, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

final_map = (
    Page(page_title = '13班蹭饭图')
    .add(cn)
    .add(wo)
    .render('index.html')
)

os.system('index.html')
