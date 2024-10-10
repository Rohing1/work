from DrissionPage import Chromium
import time
# 启动或接管浏览器，并创建标签页对象
tab = Chromium().latest_tab
# 跳转到登录页面
tab.get('https://work.weixin.qq.com/')
time.sleep(1.5)
#点击扫描二维码登录
ele = tab.ele('tag:a@@class=index_top_operation_loginBtn@@role=button@@data-js-click-report-log^79506294,official_we@@text()=企业登录').click()
#停止60s进行扫码登录
time.sleep(90)
