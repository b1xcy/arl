# coding=utf-8
"""
OneForAll配置
"""

import pathlib

# 路径设置
relative_directory = pathlib.Path(__file__).parent.parent  # OneForAll代码相对路径
data_storage_dir = relative_directory.joinpath('data')  # 数据存放目录

# OneForAll入口参数设置
enable_check_version = False  # 开启最新版本检查
enable_brute_module = False  # 使用爆破模块(默认True)
enable_dns_resolve = False  # 使用DNS解析子域(默认True)
enable_http_request = False  # 使用HTTP请求子域(默认True)
enable_finder_module = False  # 开启finder模块,开启会从响应体和JS中再次发现子域(默认True)
enable_altdns_module = False  # 开启altdns模块,开启会利用置换技术重组子域再次发现新子域(默认True)
enable_cdn_check = True  # 开启cdn检查模块(默认True)
enable_banner_identify = False  # 开启WEB指纹识别模块(默认True)
enable_takeover_check = False  # 开启子域接管风险检查(默认False)
# HTTP请求子域的端口范围 参数可选值有 'small', 'medium', 'large'
http_request_port = 'medium'  # 请求端口范围(默认 'small'，表示请求子域的80,443端口)
# 参数可选值True，False分别表示导出存活，全部子域结果
result_export_alive = True  # 只导出存活的子域结果(默认False)
result_save_format = 'csv'  # 子域结果保存文件格式(默认csv)
# 参数path默认None使用OneForAll结果目录自动生成路径
result_save_path = None  # 子域结果保存文件路径(默认None)

# 收集模块设置
save_module_result = False  # 保存各模块发现结果为json文件(默认False)
enable_all_module = True  # 启用所有收集模块(默认True)
enable_partial_module = []  # 启用部分收集模块 必须禁用enable_all_module才能生效
# 只使用ask和baidu搜索引擎收集子域的示例
# enable_partial_module = [('modules.search', 'ask')
#                          ('modules.search', 'baidu')]

# 爆破模块设置
brute_concurrent_num = 3000  # 爆破时并发查询数量(默认2000，最大推荐10000)
# 爆破所使用的字典路径(默认None则使用data/subdomains.txt，自定义字典请使用绝对路径)
brute_wordlist_path = None
enable_recursive_brute = False  # 是否使用递归爆破(默认False)
brute_recursive_depth = 2  # 递归爆破深度(默认2层)
# 爆破下一层子域所使用的字典路径(默认None则使用data/subnames_next.txt，自定义字典请使用绝对路径)
recursive_nextlist_path = None
enable_check_dict = False  # 是否开启字典配置检查提示(默认False)
delete_generated_dict = True  # 是否删除爆破时临时生成的字典(默认True)
#  是否删除爆破时massdns输出的解析结果 (默认True)
#  massdns输出的结果中包含更详细解析结果
#  注意: 当爆破的字典较大或使用递归爆破或目标域名存在泛解析时生成的文件可能会很大
delete_massdns_result = True
only_save_valid = True  # 是否在处理爆破结果时只存入解析成功的子域
check_time = 10  # 检查字典配置停留时间(默认10秒)
enable_fuzz = False  # 是否使用fuzz模式枚举域名
fuzz_place = None  # 指定爆破的位置 指定的位置用`*`表示 示例：www.*.example.com
fuzz_rule = None  # fuzz域名的正则 示例：'[a-z][0-9]' 表示第一位是字母 第二位是数字
brute_ip_blacklist = {'0.0.0.0', '0.0.0.1'}  # IP黑名单 子域解析到IP黑名单则标记为非法子域
# CNAME黑名单 子域解析到CNAME黑名单则标记为非法子域
brute_cname_blacklist = {'nonexist.sdo.com', 'shop.taobao.com'}
ip_appear_maximum = 100  # 多个子域解析到同一IP次数超过100次则标记为非法(泛解析)子域
cname_appear_maximum = 50  # 多个子域解析到同一cname次数超过50次则标记为非法(泛解析)子域

# 代理设置
enable_request_proxy = False  # 是否使用代理(全局开关)
proxy_all_module = False  # 代理所有模块
proxy_partial_module = ['GoogleQuery', 'AskSearch', 'DuckDuckGoSearch',
                        'GoogleAPISearch', 'GoogleSearch', 'YahooSearch',
                        'YandexSearch', 'CrossDomainXml',
                        'ContentSecurityPolicy']  # 代理自定义的模块
request_proxy_pool = [{'http': 'http://127.0.0.1:1080',
                       'https': 'https://127.0.0.1:1080'}]  # 代理池
# request_proxy_pool = [{'http': 'socks5h://127.0.0.1:10808',
#                        'https': 'socks5h://127.0.0.1:10808'}]  # 代理池

# 搜索模块设置
enable_recursive_search = False  # 递归搜索子域
search_recursive_times = 2  # 递归搜索层数
