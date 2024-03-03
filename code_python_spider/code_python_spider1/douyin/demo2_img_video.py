# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/22 21:35
# @File    ：demo2_img_video.py
# @Function:

import requests
import re
import os


def req_img():
    url = 'https://pic.netbian.com/uploads/allimg/230406/232451-16807946910184.jpg'
    resp = requests.get(url=url)

    # 文本数据/字符数据 二进制字节流数据/字节数据 resp.content
    with open('mn.jpg', 'wb') as f:  # w wb
        f.write(resp.content)


def req_imgs_many():
    url = 'https://pic.netbian.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'gbk'
    # print(resp.text)

    # 数据解析  re xpath css
    imgs_url_list = re.findall(r'/uploads/allimg/\d+/\d+-[0-9a-zA-Z]+\.jpg', resp.text)
    imgs_url_list2 = ['https://pic.netbian.com' + item for item in imgs_url_list]
    # print(imgs_url_list2)

    if not os.path.exists('.imgs'):
        os.makedirs('./imgs')
    for img_url in imgs_url_list2:
        resp2 = requests.get(url=img_url)
        name = os.path.basename(img_url)
        with open('./imgs/' + name, 'wb') as f:
            f.write(resp2.content)


def req_douyin_video():
    url = 'https://v26-web.douyinvod.com/dac343f6c25f425021ce3bdd38e49ade/65aea6dc/video/tos/cn/tos-cn-ve-15c001-alinc2/o4bLPf7dBfnRJGTDw08GeQD2BwC6IACttngGaA/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=618&bt=618&cs=0&ds=6&ft=t2zLrtjjM95MxrKqoZmCBh9VYl-KKar1GbN4y2_q8Z4ka&mime_type=video_mp4&qs=12&rc=OjppMzplN2hpNjdpM2k6NkBpM208ZWU6ZnFwcDMzNGkzM0AvNjFgNV4yXzIxYjBgXi1jYSNwc2hfcjRnZWVgLS1kLTBzcw%3D%3D&btag=e00008000&dy_q=1705941183&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240123003302E370D9C2F1C38E293848'
    # url = 'https://v26-web.douyinvod.com/cc2f05054449a8a51930fb9d8cab958c/65aea6d8/video/tos/cn/tos-cn-ve-15/oMuIAUo3hfA8iwIgEeLzND7W1Qt9tKyGDALtBv/?a=6383&ch=164&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=645&bt=645&cs=0&ds=3&ft=t2zLrtjjM95MxrKqoZmCBh9VYlmRKar1GbN4y2_q8Z4ka&mime_type=video_mp4&qs=1&rc=Njo3Njo5ZjhoNjczOThlZ0BpampnNWQ6ZjRlcDMzNGkzM0A1LTMyLy8uNjYxMGM1LjFiYSNvYHNycjRvYTBgLS1kLWFzcw%3D%3D&btag=e00008000&dy_q=1705941185&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240123003304B85F8919A041CC321B9D'
    resp = requests.get(url=url)
    with open('mnv2.mp4', 'wb') as f:
        f.write(resp.content)


def req_douyin_videos_many():
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=150&webid=7285348077275334180&msToken=I_Bmjk-iOrDaE_ICZ_XavKTFkL7TbyFwlW7Xa2bXlN2yTn1pNNmjy8bJvJWUdz31QWz9PmCRYK0fB21rdf7Ca67gW9e0rV1DDNT6NilOjPAcjI6K2_bxFPeuGbWwagM=&X-Bogus=DFSzswVODdUANy5ntiOJMcLZzYjY'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.douyin.com/user/MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS',
        'Cookie': 'ttwid=1%7Carvrjl9oOLsfR9VmFGMFTGDvizND1lCjic8tBa06VUY%7C1696252296%7C304819e23ed9813355ecd682b1d2fd43e4ea6a33f158152b2de5c018f7db12bb; s_v_web_id=verify_lqqurqmd_OdBhcl7i_mLZf_4Pyy_AV8w_ibymmgdTYVSd; passport_csrf_token=c011a53ea595feb12ac0a3f596dc1d60; passport_csrf_token_default=c011a53ea595feb12ac0a3f596dc1d60; bd_ticket_guard_client_web_domain=2; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1440; dy_sheight=960; csrf_session_id=0310651ed47844a23a3120077324cd3d; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221705925383.802%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; odin_tt=b2e59dc4f98ee048745fb1012fbe16f718fc589bcaac1baad9d674f7cefe97a1220279b75adbfe23c6994c48803c74b3f58de575d46d39a376b660a61f80779795b327d5be24e90ae298aab5cf77e89c; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=065ae745f005d58fe8be6; __ac_signature=_02B4Z6wo00f01.g6VagAAIDCKlctag3ViZf4GlEAAJuqR42Gabakk6Lh5b-8RrOCXAuQwp15p9HrO7QK7HuKW87op0REywnI27lgLvvf4bJNyEeSA5JJwZe6jnFNQRFK8QT0hflAFVQTKkbGe1; SEARCH_RESULT_LIST_TYPE=%22single%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; download_guide=%223%2F20240122%2F0%22; pwa2=%220%7C0%7C3%7C0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRFNoZUQ5dFRaYmVTVjlMUmsvS3JwQUVIc0N1U1RWMFlPY2YrMmNiemdEaUZKUmdqSE9iMWpGcHlQdkVDV1lNRVArK3BxSjlyYnF6cTdKUFNiNG0zS009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=I_Bmjk-iOrDaE_ICZ_XavKTFkL7TbyFwlW7Xa2bXlN2yTn1pNNmjy8bJvJWUdz31QWz9PmCRYK0fB21rdf7Ca67gW9e0rV1DDNT6NilOjPAcjI6K2_bxFPeuGbWwagM=; tt_scid=q0Hhvm1xpgQBaQEgzgsUW6v5qAIkqzedWqiMocoVkQtJE7LdtPQqAhD1g0eqIpx73ea2; msToken=AwvMTKy_YstEHGZ_pXlsKBYz1Po4wTxYN7dyJSR-LiKm15pdDTkCejUG9_QI8J1eB2ZO7NoPzmKVVfhBQ8hZltT5DqiU5kgqqoZHzIuMr4iJsX-Vt6Ux5U-tc3-EDvI=; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22'
    }
    """
    params = {
        'ac': 'WIFI',
        'os_api': '28',
        'device_type': 'MI+6',
        'ssmix': 'a',
        'manifest_version_code': '100801',
        'dpi': '440',
        'uuid': 'xxxxxxxxxxxx',
        'version_code': '100800',
        'app_name': 'aweme',
        'version_name': '10.8.0',
        'openudid': 'xxxxxxxxxxxx',
        'device_id': 'xxxxxxxxxxxx',
        'resolution': '1080*2069',
        'os_version': '9',
        'language': 'zh',
        'device_brand': 'Xiaomi',
        'aid': '1128',
        'app_type': 'normal',
        'ac2': 'WIFI',
        'channel': 'tengxun_new',
        'update_version_code': '10809900',
        'app_region': 'cn',
        'config_version': '10.8.0',
    }
    """

    resp = requests.get(url=url, headers=headers)
    # print(resp.text)
    resp_json = resp.json()
    items_list = resp_json['aweme_list']
    print(items_list)
    for item in items_list:
        aweme_id = item['aweme_id']
        desc = item['desc']
        nickname = item['author']['nickname']
        video = {'aweme_id': aweme_id, 'desc': desc, 'nickname': nickname}
        print(video)


if __name__ == '__main__':
    print('start')
    # req_img()  # resp.content
    # req_imgs_many()  #
    # req_douyin_video()
    req_douyin_videos_many()
