"""商品LP 脆弱性チェック（緊急対策PHPベース・Ver.1の型）を組み立てる
使い方: python3 -I build.py <srcフォルダ> <出力HTML>
"""
import sys, os

src, out = sys.argv[1], sys.argv[2]
BUILD_TAG = 'swc2026_vulncheck_ver1.0 / 2026-11-09'

def rd(n):
    return open(os.path.join(src, n), encoding='utf-8').read()

t = rd('template.html')
css = rd('base_v1.css') + rd('add.css') + rd('add_vuln.css')
mailto = rd('mailto.txt').strip()

price_box = ('<div class="vc-box">'
             '<p class="b-unit">1サイト　料金</p>'
             '<p class="b-price"><span class="b-num">50,000</span><span class="b-yen">円</span><span class="b-tax">（税込）</span></p>'
             '<p class="b-note">脆弱性アドバイス付・追加費用なし。<br>カード払い可能。</p>'
             '<p class="b-term">納期　<b>72時間</b>以内</p>'
             '</div>')
cta = ('<div class="btns one vc-cta">'
       f'<a class="btn btn-order" href="{mailto}">お申し込み・お問い合わせ</a>'
       '</div>')

def rep(s, old, new, n=1):
    c = s.count(old)
    if c != n:
        raise SystemExit(f'置換数が違う: {old[:40]!r} {c}件（期待 {n}）')
    return s.replace(old, new)

t = rep(t, '{{BUILD_TAG}}', BUILD_TAG)
t = rep(t, '{{CSS}}', css)
t = rep(t, '{{PRICE_BOX}}', price_box, 2)
t = rep(t, '{{CTA}}', cta, 3)
t = rep(t, '{{TOP_IMG}}', '')
assert '{{' not in t, '置き換え残り'
open(out, 'w', encoding='utf-8').write(t)
print('built', out, len(t))
