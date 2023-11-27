html = '''
<div class="BOX">
    <!-- 内容模块 开始 -->
    <div class="App max-box" index="0" style="max-width: 868px;min-width: 599px; height:360px;margin: 0 auto;">
        <!-- 第一本书 开始 -->
        <book title="西游记" class="box-1 aa bb cc" index="01">
            <b class="book-1" href="https://www.###1.com" target="_parent">
                <a>《西游记》</a>
                </br>
                <a href="http://www.baidu.com">百度一下</a>
            </b>
            <img class="book1-img" id="ps-1" title="图片1" alt="img1.jpg"
                src="http://img3m6.ddimg.cn/54/26/28548486-1_b_19.jpg">
            <c class="xiaowu laowu">作者：<span>吴承恩</span></c>
            <d>今日<span>1000</span>人观看</d>
        </book>
        <!-- 第一本书 结束 -->
        <!-- 第二本书 开始 -->
        <book title="三国演义" class="box-2 aa bb cc" index="02">
            <b class="book-2" href="https://www.###2.com" target="_parent">
                <a>《三国演义》</a>
                </br>
                <a href="http://www.baidu.com">百度一下</a>
            </b>
            <img class="book2-img" id="ps-2" title="图片2" alt="img2.jpg"
                src="http://img3m9.ddimg.cn/2/7/28514279-1_b_17.jpg">
            <c class="xiaoluo laowu">作者：<span>罗贯中</span></c>
            <d>今日<span>2000</span>人观看</d>
        </book>
        <!-- 第二本书 结束 -->
        <!-- 第三本书 开始 -->
        <book title="水浒传" class="box-3 aa bb cc" index="03">
            <b class="book-3" href="https://www.###3.com" target="_parent">
                <a>《水浒传》</a>
                </br>
                <a href="http://www.baidu.com">百度一下</a>
            </b>
            <img class="book3-img" id="ps-3" title="图片3" alt="img3.jpg"
                src="http://img3m5.ddimg.cn/24/28/29162355-1_b_2.jpg">
            <c class="xiaoshi laowu">作者：<span>施耐庵</span></c>
            <d>今日<span>3000</span>人观看</d>
        </book>
        <!-- 第三本书 结束 -->
        <!-- 第四本书 开始 -->
        <book title="红楼梦" class="box-4 aa bb cc" index="04">
            <b class="book-4" href="https://www.###4.com" target="_parent">
                <a>《红楼梦》</a>
                </br>
                <a href="http://www.baidu.com">百度一下</a>
            </b>
            <img class="book4-img" id="ps-4" title="图片4" alt="img4.jpg"
                src="http://img3m4.ddimg.cn/91/30/29249344-1_b_9.jpg">
            <c class="xiaocao laowu">作者：<span>曹雪芹</span></c>
            <d>今日<span>4000</span>人观看</d>
        </book>
        <!-- 第一本书 结束 -->
    </div>
    <!-- 内容模块 结束 -->
</div>
'''

from lxml import etree

tree = etree.HTML(html)

'''age:'''
# index：01
index = tree.xpath('//book/@index')
print(index)
# name: 西游记
name = tree.xpath('//book//b/a[1]/text()')
print(name)
# code: 吴承恩
code = tree.xpath('//c[@*]/span/text()')
print(code)
# url: https://www.###.com
url = tree.xpath('//div[@class="App max-box"][1]/book/b/@href')
print(url)
# img_code: 图片1
img_code = tree.xpath('//book/img/@title')
print(img_code)
# img_url: http://img3m6.ddimg.cn/54/26/28548486-1_b_19.jpg
img_url = tree.xpath('//book/img/@src')
print(img_url)
# age: 今日观看人数
age = tree.xpath('//d/span/text()')
print(age)

# 整理数据
data = []
dict = {}
for i in range(len(index)):
    dict['index'] = index[i]
    dict['name'] = name[i]
    dict['code'] = code[i]
    dict['url'] = url[i]
    dict['img_code'] = img_code[i]
    dict['img_url'] = img_url[i]
    dict['age'] = age[i]
    data.append(dict)

print(data)
