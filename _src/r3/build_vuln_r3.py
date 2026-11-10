# 脆弱性チェック ver2.1：トップの画像エリアに緊急対策PHP（ptarmigan2026）と同じ画像を置く（11/10 16:09 永田様）
import sys
src,dst=sys.argv[1:3]
t=open(src,encoding='utf-8').read()
def rep(t,a,b,n=1):
    c=t.count(a)
    if c!=n: sys.exit('置換件数が違う %d!=%d %s'%(c,n,a[:60]))
    return t.replace(a,b)
t=rep(t,'swc2026_vulncheck_ver2.0 / 2026-11-10','swc2026_vulncheck_ver2.1 / 2026-11-10')
t=rep(t,'''  <!-- 画像エリア：差し替える画像を images/ に置き、下の枠の中に img を入れてください
       <img src="images/top.jpg" alt="ＰＨＰ脆弱性チェックのイメージ"> -->
  <div class="media-slot vc-wide" id="mediaSlot"><span class="ms-note">画像エリア</span></div>''',
'''  <!-- 画像エリア：緊急対策PHP（ptarmigan2026）と同じ images/top.png。差し替えるときは images/top.png を置き換えてください -->
  <div class="media-slot vc-wide" id="mediaSlot"><img src="images/top.png" alt="ＰＨＰのイメージ"><span class="ms-note">画像エリア</span></div>''')
open(dst,'w',encoding='utf-8').write(t); print('ok')
