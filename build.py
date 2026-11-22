#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сайт Адвокатського бюро «Селезньов і партнери». Запуск: python3 build.py
Усі дані бюро — у SITE нижче; сторінки збираються в index.html і 404.html."""
import json, os, html

SITE = {
    # Домен сайту: вписати, коли буде куплений (без косої риски в кінці)
    "domain": os.environ.get("SITE_DOMAIN", "https://seleznov-partners.com.ua"),
    "name": "Адвокатське бюро «Селезньов і партнери»",
    "short": "Селезньов і партнери",
    "name_en": "Seleznov & Partners Law Firm",
    "person": "Максим Селезньов",
    "cert": "000208",
    "since": "2017",
    "street": "вул. А. Артинова, 46, офіс 110",
    "city": "Вінниця",
    "postal": "21050",
    "region": "Вінницька область",
    "phone": "+380 93 768 84 16",
    "phone_raw": "+380937688416",
    "telegram": "https://t.me/Online_Advokat_UA",
    "whatsapp": "https://wa.me/380937688416",
    "viber": "viber://chat?number=%2B380937688416",
    "erau": "https://erau.unba.org.ua/profile/58196",
    "reviews_tg": "https://t.me/feedbackDivorce",
    "reviews_site": "https://razvod-online.com.ua/feedback",
    "email": os.environ.get("SITE_EMAIL", ""),  # з'явиться на домені бюро
}

SERVICES = [
    {
        "area": "Сімейне право",
        "title": "Розірвання шлюбу онлайн",
        "text": "Пакет документів для суду з покроковою інструкцією або розлучення під ключ, коли справу від подання до рішення веде адвокат.",
        "url": "https://razvod-online.com.ua",
        "host": "razvod-online.com.ua",
        "short": "Розлучення",
        "art": "halves",
    },
    {
        "area": "Сімейне право",
        "title": "Аліменти онлайн",
        "text": "Заява про стягнення аліментів з інструкцією або аліменти під ключ: подаємо документи до суду, контролюємо справу й передаємо виконавчий документ до виконавчої служби.",
        "url": "https://alimenty-online.com.ua",
        "host": "alimenty-online.com.ua",
        "short": "Аліменти",
        "art": "circles",
    },
    {
        "area": "Для українців за кордоном",
        "title": "Документи з України",
        "text": "Повторні свідоцтва ДРАЦС, витяги, витяг про несудимість, РНОКПП. Адвокат отримує документ в Україні, ставить апостиль, робить переклад і надсилає у вашу країну.",
        "url": "https://dokumenty-z-ukrainy.com.ua",
        "host": "dokumenty-z-ukrainy.com.ua",
        "short": "Документи з України",
        "art": "sheet",
    },
    {
        "area": "Шаблони документів",
        "title": "Deposit Documents",
        "text": "Онлайн-база шаблонів юридичних документів, які готують практикуючі адвокати та юристи. Обираєте документ, оплачуєте й отримуєте його на пошту.",
        "url": "https://deposit-documents.com",
        "host": "deposit-documents.com",
        "short": "Шаблони документів",
        "art": "stack",
    },
]

TITLE = "Адвокатське бюро «Селезньов і партнери» — сімейні справи онлайн"
DESCRIPTION = ("Адвокатське бюро «Селезньов і партнери»: розлучення, аліменти та документи з України для тих, "
               "хто за кордоном. Адвокатська практика з 2017 року, офіс у Вінниці, працюємо онлайн по всій Україні.")

E = html.escape
OUT = os.path.dirname(os.path.abspath(__file__))

def mark(gid, size=42):
    """Знак бюро (варіант А2): ваги з вигнутим коромислом, одна лінія й точка, фірмовий градієнт."""
    return (f'<svg class="mark" viewBox="0 0 64 64" width="{size}" height="{size}" fill="none" stroke="url(#{gid})" stroke-width="3.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><defs><linearGradient id="{gid}" x1="0" y1="0" x2="64" y2="0" '
            f'gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2D48B7"/><stop offset="1" stop-color="#00A2F5"/></linearGradient></defs>'
            f'<circle cx="32" cy="10.5" r="3.5" fill="url(#{gid})" stroke="none"/><path d="M12 22 Q32 17 52 22 M32 19.5 V55 M24 55 H40"/>'
            f'<path d="M7 38 L12 22 L17 38 M5 38 Q12 44 19 38 Z"/><path d="M47 38 L52 22 L57 38 M45 38 Q52 44 59 38 Z"/></svg>')


def wordmark():
    return '<span><span class="wm"><b>Селезньов</b><span> і партнери</span></span><small>адвокатське бюро</small></span>'


ARROW = '<svg aria-hidden="true" viewBox="0 0 16 16" class="ico"><path d="M2 8H14M9 3L14 8L9 13"/></svg>'
OUTLINK = '<svg aria-hidden="true" viewBox="0 0 16 16" class="ico"><path d="M4 12L12 4M6 4H12V10"/></svg>'

ART = {
    "halves": '<span class="a-half a-half--l"></span><span class="a-half a-half--r"></span>',
    "circles": '<span class="a-dot a-dot--big"></span><span class="a-dot a-dot--glass"></span>',
    "sheet": '<span class="a-sheet"><i></i><i></i><i class="s"></i></span><span class="a-dot a-dot--seal"></span>',
    "stack": '<span class="a-card a-card--1"></span><span class="a-card a-card--2"></span><span class="a-card a-card--3"></span>',
}

CSS = """
@font-face{font-family:Onest;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/onest-cyrillic-wght-normal.woff2) format("woff2-variations");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:Onest;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/onest-latin-wght-normal.woff2) format("woff2-variations");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:Geologica;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/geologica-cyrillic-wght-normal.woff2) format("woff2-variations");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:Geologica;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/geologica-latin-wght-normal.woff2) format("woff2-variations");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:Raleway;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/raleway-cyrillic-wght-normal.woff2) format("woff2-variations");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:Raleway;font-style:normal;font-display:swap;font-weight:100 900;src:url(/assets/fonts/raleway-latin-wght-normal.woff2) format("woff2-variations");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{--sand:#E9DFD2;--paper:#F4EEE6;--ink:#1F1E1C;--muted:#4A433B;--soft:#5C544B;--accent:#2D48B7;--sky:#00A2F5;--grad:linear-gradient(90deg,#2D48B7,#00A2F5);--logo:Raleway,Onest,Arial,sans-serif;--sage:#8A9A7B;--slate:#7F93A8;--clay:#D8CBBB;--glass:rgba(255,255,255,.55);--glass-line:rgba(255,255,255,.85);
--display:Geologica,Onest,system-ui,-apple-system,"Segoe UI",Arial,sans-serif;--body:Onest,system-ui,-apple-system,"Segoe UI",Arial,sans-serif;--gut:max(20px,env(safe-area-inset-left,0px));color-scheme:light}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--sand);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.55;-webkit-text-size-adjust:100%}
a{color:inherit;text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:4px}
a:focus-visible{outline:2px solid currentColor;outline-offset:3px;border-radius:8px}
.btn:hover,.pill:hover{text-decoration:none;filter:brightness(1.08)}
.ico{width:15px;height:15px;flex:none;fill:none;stroke:currentColor;stroke-width:1.5}
.wrap{max-width:1200px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
@media(min-width:900px){.wrap{padding-left:56px;padding-right:56px}}
h1,h2,h3{font-family:var(--display);margin:0;text-wrap:balance}
p{margin:0}
.kicker{display:inline-flex;align-items:center;gap:10px;font-size:14px;font-weight:500}
.kicker::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent)}
.btn{display:inline-flex;align-items:center;gap:12px;min-height:52px;padding:0 26px;background:var(--ink);color:#fff;border-radius:999px;font-weight:500;font-size:16px}
.btn--light{background:#fff;color:var(--ink)}
/* header */
.top{padding-top:20px}
.bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 28px;padding:8px 10px 8px 20px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--glass-line);border-radius:32px}
.brand{display:flex;align-items:center;gap:14px;min-height:48px}
.brand:hover{text-decoration:none}
.mark{flex:none;width:42px;height:42px}
.wm{display:block;font-family:var(--logo);font-size:21px;line-height:1.05;letter-spacing:-.2px;white-space:nowrap}
.wm b{font-weight:700;color:var(--accent)}
.wm span{font-weight:300;color:var(--sky)}
.brand small{display:block;font-family:var(--logo);font-size:13px;font-weight:500;color:#1F7FD8;margin-top:2px}
.nav{display:flex;flex-wrap:wrap;gap:2px 26px;font-size:15px}
.nav a,.bar .tel{display:inline-flex;align-items:center;min-height:44px}
.bar .tel{font-size:15px;font-weight:500;font-variant-numeric:tabular-nums}
.bar-act{display:flex;flex-wrap:wrap;align-items:center;gap:6px 20px}
.bar .btn{min-height:46px;padding:0 22px;font-size:15px}
@media(max-width:760px){.nav{display:none}.bar .tel{display:none}}
/* hero */
.hero{display:flex;flex-wrap:wrap;align-items:center;gap:48px 64px;padding-top:56px;padding-bottom:80px}
.hero-text{flex:3 1 440px;min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:26px}
.badge{display:inline-flex;align-items:center;gap:10px;min-height:36px;padding:0 16px;background:var(--glass);border:1px solid var(--glass-line);border-radius:999px;font-size:14px;font-weight:500}
.badge::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent)}
.hero h1{font-weight:300;font-size:clamp(36px,5vw,70px);line-height:1.06;letter-spacing:-.025em}
.hero h1 span{color:var(--accent)}
.lead{max-width:34em;font-size:19px;color:var(--muted)}
.hero-art{flex:2 1 320px;min-width:0;max-width:500px;position:relative;padding:56px 0 28px}
.orb{position:absolute;border-radius:50%;aspect-ratio:1/1}
.orb--glass{left:12%;top:0;width:76%;border:1.5px solid var(--glass-line);background:linear-gradient(145deg,rgba(255,255,255,.5),rgba(255,255,255,.06) 58%)}
.orb--accent{right:0;top:30%;width:58%;background:var(--grad)}
.orb--sage{right:7%;top:5%;width:12%;background:var(--sage)}
.orb--slate{left:0;bottom:0;width:31%;background:radial-gradient(circle at 35% 30%,#AAB9C9,#72859A 72%)}
.pick{position:relative;width:min(100%,350px);padding:26px;display:flex;flex-direction:column;gap:16px;background:var(--glass);-webkit-backdrop-filter:blur(26px);backdrop-filter:blur(26px);border:1px solid var(--glass-line);border-radius:36px}
.pick small{display:block;font-size:14px;color:var(--muted)}
.pick strong{display:block;font-family:var(--display);font-weight:400;font-size:26px;line-height:1.15}
.pick nav{display:flex;flex-direction:column;gap:10px;font-size:15.5px;font-weight:500}
.pill{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:50px;padding:0 20px;background:rgba(255,255,255,.78);border-radius:999px}
.since{position:relative;width:min(88%,310px);margin:-18px 0 0 auto;padding:24px 28px;display:flex;flex-direction:column;gap:6px;background:var(--ink);color:var(--paper);border-radius:32px}
.since b{font-family:var(--display);font-weight:400;font-size:30px;line-height:1.1}
.since span{font-size:15px;line-height:1.4;color:#C9C0B5}
/* figures */
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(270px,100%),1fr));gap:22px;padding-bottom:96px}
.fig{min-height:190px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;gap:22px;border-radius:36px;position:relative;overflow:hidden}
.fig b{position:relative;font-family:var(--display);font-weight:300;font-size:clamp(46px,4.6vw,64px);line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.fig span{position:relative;font-size:16px;line-height:1.45}
.fig--glass{background:var(--glass);border:1px solid var(--glass-line)}
.fig--glass span{color:var(--muted)}
.fig--accent{background:var(--grad);color:#fff}
.fig--accent::before{content:"";position:absolute;right:-60px;top:-70px;width:230px;height:230px;border-radius:50%;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.35)}
.fig--ink{background:var(--ink);color:var(--paper)}
.fig--ink span{color:#C9C0B5}
/* services */
.services{position:relative;overflow:hidden;background:var(--paper)}
.services::before,.services::after{content:"";position:absolute;border-radius:50%;z-index:0}
.services::before{left:-140px;top:220px;width:520px;height:520px;background:#E3D6C6}
.services::after{right:-110px;bottom:90px;width:400px;height:400px;background:rgba(138,154,123,.4)}
.services .wrap{position:relative;z-index:1;padding-top:96px;padding-bottom:96px;display:flex;flex-direction:column;gap:52px}
.head{display:flex;flex-direction:column;gap:16px;max-width:760px}
.head h2{font-weight:300;font-size:clamp(30px,3.7vw,50px);line-height:1.1;letter-spacing:-.02em}
.head p{font-size:18px;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(440px,100%),1fr));gap:22px}
.card{padding:34px;display:flex;flex-direction:column;align-items:flex-start;gap:26px;background:var(--glass);-webkit-backdrop-filter:blur(26px);backdrop-filter:blur(26px);border:1px solid rgba(255,255,255,.9);border-radius:40px}
.card small{display:block;font-size:14px;color:var(--soft);margin-bottom:10px}
.card h3{font-weight:400;font-size:28px;line-height:1.15;letter-spacing:-.015em;margin-bottom:12px}
.card p{color:var(--muted)}
.card .btn{margin-top:auto;min-height:48px;padding:0 22px;font-size:15px;gap:10px}
.art{display:flex;align-items:flex-end;height:120px}
.a-half{width:60px;height:120px;background:var(--slate)}
.a-half--l{border-radius:120px 0 0 120px}
.a-half--r{border-radius:0 120px 120px 0;background:var(--accent);margin-left:16px}
.a-dot{border-radius:50%}
.a-dot--big{width:120px;height:120px;background:var(--sage)}
.a-dot--glass{width:64px;height:64px;margin-left:-24px;background:rgba(255,255,255,.5);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.95)}
.a-sheet{width:92px;height:120px;padding:22px 18px;display:flex;flex-direction:column;gap:10px;border-radius:18px;background:#fff}
.a-sheet i{height:6px;border-radius:3px;background:var(--clay)}
.a-sheet i.s{width:60%}
.a-dot--seal{width:64px;height:64px;margin:0 0 -6px -28px;background:var(--accent)}
.art:has(.a-card){align-items:flex-start}
.a-card{width:84px;height:106px;border-radius:18px;background:var(--clay)}
.a-card--2{margin:8px 0 0 -50px;background:var(--slate)}
.a-card--3{margin:16px 0 0 -50px;background:rgba(255,255,255,.5);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.95)}
/* about */
.about{padding-top:96px}
.panel{position:relative;overflow:hidden;padding:clamp(28px,5vw,68px);display:flex;flex-wrap:wrap;align-items:flex-start;gap:44px 68px;background:var(--ink);color:var(--paper);border-radius:44px}
.panel::before{content:"";position:absolute;right:-90px;top:-130px;width:440px;height:440px;border-radius:50%;background:var(--accent);filter:blur(70px);opacity:.6}
.panel::after{content:"";position:absolute;left:-70px;bottom:-110px;width:280px;height:280px;border-radius:50%;border:1px solid rgba(255,255,255,.16)}
.panel>*{position:relative}
.about-text{flex:3 1 400px;min-width:0;display:flex;flex-direction:column;gap:26px}
.about-text .kicker{color:#E3DACF}
.about-text .kicker::before{background:var(--paper)}
.about-text>p:not(.kicker){font-family:var(--display);font-weight:300;font-size:clamp(23px,2.5vw,33px);line-height:1.3;letter-spacing:-.01em;text-wrap:pretty}
.person{display:flex;align-items:center;gap:18px}
.mono{flex:none;width:88px;height:88px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--accent);font-family:var(--display);font-size:28px;font-weight:400;color:#fff}
.person b{display:block;font-family:var(--display);font-size:21px;font-weight:400}
.person span{font-size:15px;color:#C9C0B5}
.facts{flex:2 1 320px;min-width:0;margin:0;padding:8px 26px;display:flex;flex-direction:column;font-size:16px;background:rgba(255,255,255,.09);-webkit-backdrop-filter:blur(26px);backdrop-filter:blur(26px);border:1px solid rgba(255,255,255,.2);border-radius:30px}
.facts div{display:flex;justify-content:space-between;gap:22px;padding:15px 0}
.facts div+div{border-top:1px solid rgba(255,255,255,.16)}
.facts dt{color:#D5CCC1}
.facts dd{margin:0;text-align:right}
.facts a{text-decoration:underline;text-underline-offset:4px}
/* reviews */
.reviews{padding-top:56px;padding-bottom:96px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px 40px}
.reviews h2{font-weight:300;font-size:clamp(26px,3vw,40px);line-height:1.15;letter-spacing:-.02em}
.reviews p{margin-top:10px;color:var(--muted);max-width:36em}
.reviews nav{display:flex;flex-wrap:wrap;gap:12px}
.reviews .pill{background:var(--glass);border:1px solid var(--glass-line);font-size:15px;font-weight:500;gap:10px}
/* contacts */
.cta{position:relative;overflow:hidden;padding:clamp(28px,5vw,68px);display:flex;flex-direction:column;gap:44px;background:var(--grad);color:#fff;border-radius:44px}
.cta::before{content:"";position:absolute;right:-120px;top:-160px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.3)}
.cta>*{position:relative}
.cta h2{font-weight:300;font-size:clamp(32px,4.2vw,56px);line-height:1.08;letter-spacing:-.02em;max-width:820px}
.ways{display:flex;flex-wrap:wrap;align-items:center;gap:12px 28px}
.ways a:not(.btn){display:inline-flex;align-items:center;min-height:44px;font-weight:500;text-decoration:underline;text-underline-offset:5px;font-variant-numeric:tabular-nums}
.office{font-style:normal;align-self:flex-start;padding:22px 26px;display:flex;flex-direction:column;gap:4px;background:rgba(255,255,255,.14);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.32);border-radius:30px}
.office b{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.15}
/* footer */
.foot{padding-top:60px;padding-bottom:calc(64px + env(safe-area-inset-bottom,0px));display:flex;flex-wrap:wrap;justify-content:space-between;gap:30px 60px;font-size:15px}
.foot .brand{min-height:0}
.foot small{display:block;font-size:13px;letter-spacing:.06em;color:var(--soft)}
.foot nav{display:flex;flex-direction:column}
.foot nav a{display:inline-flex;align-items:center;min-height:34px}
.foot .legal{display:flex;flex-direction:column;gap:8px;color:var(--soft)}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""


def jsonld():
    d = SITE["domain"]
    data = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": f"{d}/#bureau",
        "name": SITE["name"],
        "alternateName": [SITE["short"], SITE["name_en"]],
        "url": f"{d}/",
        "image": f"{d}/assets/og.png",
        "logo": f"{d}/assets/favicon.svg",
        "description": DESCRIPTION,
        "telephone": SITE["phone_raw"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["city"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["postal"],
            "addressCountry": "UA",
        },
        "areaServed": "UA",
        "knowsLanguage": ["uk"],
        "founder": {
            "@type": "Person",
            "name": SITE["person"],
            "jobTitle": "Адвокат, медіатор",
            "sameAs": [SITE["erau"]],
        },
        "foundingDate": SITE["since"],
        "sameAs": [SITE["telegram"]],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Сервіси бюро",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["title"], "url": s["url"]}}
                for s in SERVICES
            ],
        },
    }
    if SITE["email"]:
        data["email"] = SITE["email"]
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def head(title, description, path, noindex=False):
    d = SITE["domain"]
    url = f"{d}{path}"
    return f"""<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#E9DFD2">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/onest-cyrillic-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/geologica-cyrillic-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/raleway-cyrillic-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website">
<meta property="og:site_name" content="{E(SITE['short'])}">
<meta property="og:locale" content="uk_UA">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{d}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{E(SITE['name'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(description)}">
<meta name="twitter:image" content="{d}/assets/og.png">
<style>{CSS.strip()}</style>
</head>
<body>
"""


def header():
    return f"""<header class="wrap top">
<div class="bar">
<a class="brand" href="/" aria-label="{E(SITE['name'])}, на головну">{mark('bm-h')}{wordmark()}</a>
<nav class="nav" aria-label="Розділи сторінки"><a href="/#services">Сервіси</a><a href="/#about">Про бюро</a><a href="/#contacts">Контакти</a></nav>
<div class="bar-act"><a class="tel" href="tel:{SITE['phone_raw']}">{SITE['phone']}</a><a class="btn" href="{SITE['telegram']}">Написати адвокату</a></div>
</div>
</header>
"""


def footer():
    links = "".join(f'<a href="{s["url"]}">{E(s["title"])}</a>' for s in SERVICES)
    return f"""<footer class="wrap foot">
<a class="brand" href="/" aria-label="{E(SITE['name'])}, на головну">{mark('bm-f', 38)}{wordmark()}</a>
<nav aria-label="Сервіси бюро">{links}</nav>
<div class="legal"><span>Свідоцтво адвоката № {SITE['cert']}</span><span>{E(SITE['street'])}, м. {E(SITE['city'])}, {SITE['postal']}</span><span>© {SITE['since']}–2026 АБ «{E(SITE['short'])}»</span></div>
</footer>
</body>
</html>
"""


def index():
    picks = "".join(f'<a class="pill" href="{s["url"]}">{E(s["short"])}{OUTLINK}</a>' for s in SERVICES)
    cards = "".join(f"""<article class="card">
<div class="art" aria-hidden="true">{ART[s['art']]}</div>
<div><small>{E(s['area'])}</small><h3>{E(s['title'])}</h3><p>{E(s['text'])}</p></div>
<a class="btn" href="{s['url']}">{E(s['host'])}{OUTLINK}</a>
</article>""" for s in SERVICES)
    email = f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>' if SITE["email"] else ""
    return head(TITLE, DESCRIPTION, "/") + header() + f"""<main>
<section class="wrap hero">
<div class="hero-text">
<p class="badge">Адвокатська практика з {SITE['since']} року</p>
<h1>Сімейні справи й документи з України. <span>Онлайн, з будь-якої країни.</span></h1>
<p class="lead">Адвокатське бюро «{E(SITE['short'])}» веде розлучення й аліменти та отримує документи в Україні дистанційно. Працюємо через чотири онлайн-сервіси: оберіть свій або напишіть нам, і ми підкажемо, з чого почати.</p>
<a class="btn" href="{SITE['telegram']}">Написати адвокату{ARROW}</a>
</div>
<div class="hero-art">
<span class="orb orb--glass" aria-hidden="true"></span><span class="orb orb--accent" aria-hidden="true"></span><span class="orb orb--sage" aria-hidden="true"></span><span class="orb orb--slate" aria-hidden="true"></span>
<div class="pick"><div><small>Сервіси бюро</small><strong>Що вам потрібно?</strong></div><nav aria-label="Швидкий перехід до сервісів">{picks}</nav></div>
<div class="since"><b>З {SITE['since']} року</b><span>адвокатська практика, свідоцтво № {SITE['cert']}</span></div>
</div>
</section>

<section class="wrap figs" aria-label="Бюро в цифрах">
<div class="fig fig--glass"><b>10 000+</b><span>клієнтів замовили документи для розлучення або справу під ключ</span></div>
<div class="fig fig--accent"><b>35+</b><span>країн, куди ми вже надсилали документи клієнтам</span></div>
<div class="fig fig--ink"><b>4 сервіси</b><span>розлучення, аліменти, документи з України та шаблони документів</span></div>
</section>

<section class="services" id="services">
<div class="wrap">
<div class="head"><p class="kicker">Сервіси бюро</p><h2>Чотири сервіси, за кожним із яких стоїть адвокат</h2><p>Кожен сервіс має власний сайт, де можна одразу замовити послугу. Не знаєте, який вам потрібен? Напишіть нам.</p></div>
<div class="cards">{cards}</div>
</div>
</section>

<section class="wrap about" id="about">
<div class="panel">
<div class="about-text">
<p class="kicker">Про бюро</p>
<p>За кожним нашим сайтом стоїть адвокат зі свідоцтвом, а не анонімний сервіс. Договір, адвокатська таємниця й відповідальність перед клієнтом однакові, з якого б сайту ви до нас прийшли.</p>
<div class="person"><span class="mono" aria-hidden="true">МС</span><div><b>{E(SITE['person'])}</b><span>адвокат і медіатор, засновник бюро</span></div></div>
</div>
<dl class="facts">
<div><dt>Свідоцтво адвоката</dt><dd>№ {SITE['cert']}</dd></div>
<div><dt>Практика</dt><dd>з {SITE['since']} року</dd></div>
<div><dt>Напрями</dt><dd>сімейне право, транскордонні справи, документи</dd></div>
<div><dt>Офіс</dt><dd>Вінниця</dd></div>
<div><dt>Реєстр адвокатів</dt><dd><a href="{SITE['erau']}">профіль у ЄРАУ</a></dd></div>
</dl>
</div>
</section>

<section class="wrap reviews" aria-labelledby="reviews-title">
<div><h2 id="reviews-title">Відгуки клієнтів</h2><p>Клієнти залишають відгуки в нашій Telegram-групі. Частину з них зібрано на сайті сервісу розлучень.</p></div>
<nav aria-label="Відгуки"><a class="pill" href="{SITE['reviews_tg']}">Відгуки в Telegram{OUTLINK}</a><a class="pill" href="{SITE['reviews_site']}">Відгуки на сайті{OUTLINK}</a></nav>
</section>

<section class="wrap" id="contacts">
<div class="cta">
<h2>Напишіть адвокату. Підкажемо, з чого почати у вашій справі.</h2>
<div class="ways"><a class="btn btn--light" href="{SITE['telegram']}">Написати в Telegram{ARROW}</a><a href="tel:{SITE['phone_raw']}">{SITE['phone']}</a><a href="{SITE['whatsapp']}">WhatsApp</a><a href="{SITE['viber']}">Viber</a>{email}</div>
<address class="office"><b>{E(SITE['city'])}</b><span>{E(SITE['street'])}</span><span>{SITE['postal']}, {E(SITE['region'])}</span></address>
</div>
</section>
</main>
<script type="application/ld+json">{jsonld()}</script>
""" + footer()


def not_found():
    return head("Сторінку не знайдено — " + SITE["name"], "Такої сторінки немає. Перейдіть на головну сайту бюро.", "/404.html", noindex=True) + header() + f"""<main class="wrap" style="padding-top:80px;padding-bottom:80px;display:flex;flex-direction:column;align-items:flex-start;gap:22px">
<h1 style="font-weight:300;font-size:clamp(34px,4vw,56px);line-height:1.1">Такої сторінки немає</h1>
<p class="lead">Можливо, посилання застаріло. На головній є всі сервіси бюро й контакти адвоката.</p>
<a class="btn" href="/">На головну{ARROW}</a>
</main>
""" + footer()


def main():
    files = {
        "index.html": index(),
        "404.html": not_found(),
        "robots.txt": f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n",
        "sitemap.xml": f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE["domain"]}/</loc></url></urlset>\n',
    }
    for name, text in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(text)
    print("built:", ", ".join(files), "for", SITE["domain"])


if __name__ == "__main__":
    main()
