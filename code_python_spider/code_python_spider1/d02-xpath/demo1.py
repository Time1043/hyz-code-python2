from lxml import etree

html = '''
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
'''

tree = etree.HTML(html)  # 实例化html对象

tree.xpath('a')
