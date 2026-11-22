# Сайт Адвокатського бюро «Селезньов і партнери»

https://seleznov-partners.com.ua — статичний сайт на GitHub Pages.

Усі тексти й дані бюро — у `build.py` (словники `SITE` і `SERVICES`). Після змін:

```
python3 build.py
```

Скрипт перезбирає `index.html`, `404.html`, `robots.txt` і `sitemap.xml`. Шрифти Onest і Geologica (OFL) лежать у `assets/fonts`.
