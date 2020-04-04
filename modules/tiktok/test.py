import mechanicalsoup
import random

from useragents import *

url = 'https://www.tiktok.com/@willsmith?lang=en'

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True
)
browser.session.headers.update({'User-Agent':random.choice(user_agents)})

browser.open(url)


videos = browser.get_current_page().find_all('video', src=True)
print(videos)


browser.close()

'''
<div style="border-radius: 4px; background-image: url(&quot;

https://p16-va-default.akamaized.net/obj/tos-maliva-p-0068/c27cb7565213cd77453264c513e7e175

&quot;);" class="jsx-1464109409 image-card"><div class="jsx-3355072868 video-card default"><video src="
https://v19.muscdn.com/60b135909cc94ea893ca21708a0eba0b/5e8961d6/video/tos/useast2a/tos-useast2a-ve-0068c002/c2235e013a864ce0a19da975e41c0913/?a=1233&amp;br=2168&amp;bt=1084&amp;cr=0&amp;cs=0&amp;dr=0&amp;ds=3&amp;er=&amp;l=202004042242470101890710703450607E&amp;lr=tiktok_m&amp;qs=0&amp;rc=anNpOXc1bjlpczMzOzczM0ApNDtnZTxpPDw1N2Q5Z2hmM2czZjVgZDNlcW5fLS0zMTZzc2I2MmJeNV5eL15hLS82NTU6Yw%3D%3D&amp;vl=&amp;vr=" webkit-playsinline="true" playsinline="" loop="" autoplay="" preload="metadata" class="jsx-3382097194 video-player">
</video><div class="jsx-3355072868 video-card-mask"><div class="jsx-1543915374 card-footer normal no-avatar"><div class="jsx-1543915374"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyLjMxNzEgNy41NzUzOEMxMi42MzE3IDcuNzcxMDIgMTIuNjMxNyA4LjIyODk4IDEyLjMxNzEgOC40MjQ2Mkw0LjAxNDAxIDEzLjU4NzFDMy42ODA5NSAxMy43OTQyIDMuMjUgMTMuNTU0NyAzLjI1IDEzLjE2MjVWMi44Mzc0N0MzLjI1IDIuNDQ1MjggMy42ODA5NSAyLjIwNTc3IDQuMDE0MDEgMi40MTI4NUwxMi4zMTcxIDcuNTc1MzhaIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8L3N2Zz4K" class="jsx-1543915374 like-icon">
<span class="jsx-1543915374">9.4M</span></div></div></div></div></div>


https://v19.muscdn.com/60b135909cc94ea893ca21708a0eba0b/5e8961d6/video/tos/useast2a/tos-useast2a-ve-0068c002/c2235e013a864ce0a19da975e41c0913/
'''