# Сайт Адвокатського бюро «Селезньов і партнери»

https://seleznov-partners.com.ua — статичний сайт на GitHub Pages.

Усі тексти й дані бюро — у `build.py` (словники `SITE` і `SERVICES`). Після змін:

```
python3 build.py
```

Скрипт перезбирає `index.html`, `404.html`, `robots.txt` і `sitemap.xml`. Шрифти Onest і Geologica (OFL) лежать у `assets/fonts`.

## Cloudflare

Домен обслуговує Cloudflare: сайт іде через його мережу, режим шифрування «Full».
Правило кешу «Static assets long cache»: усе з `/assets/` браузер зберігає рік, Cloudflare — 30 днів.
Тому файл у `assets/` не змінюють на місці: нову версію кладуть під новою назвою (або додають `?v=2` у посиланні),
інакше відвідувачі ще довго бачитимуть стару.
