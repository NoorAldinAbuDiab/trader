# Telegram Trader Bot

بوت تيليجرام يقوم بنسخ عناوين العملات من قناة محددة وإرسالها إلى بوت تداول آخر.

## المتطلبات
- Python 3.11.5 أو أحدث
- حساب تيليجرام مع بيانات API_ID و API_HASH
- توكن بوت تيليجرام (BOT_TOKEN)
- قناة مصدر (SOURCE_CHANNEL)
- اسم مستخدم بوت التداول (TRADE_BOT_USERNAME)

## طريقة التشغيل محلياً
1. ضع القيم في ملف `.env` (لا ترفعه إلى GitHub):
    ```
    API_ID=YOUR_API_ID
    API_HASH=YOUR_API_HASH
    BOT_TOKEN=YOUR_BOT_TOKEN
    SOURCE_CHANNEL=YOUR_CHANNEL
    TRADE_BOT_USERNAME=YOUR_TRADE_BOT
    ```
2. فعّل البيئة الافتراضية وثبّت المتطلبات:
    ```
    pip install -r requirements.txt
    ```
3. شغّل البوت:
    ```
    python main.py
    ```

## النشر على Render.com
- ارفع الملفات (عدا .env) على مستودع GitHub.
- أنشئ خدمة جديدة على Render.com واربط متغيرات البيئة من إعدادات Render.
- أوامر البناء:
    ```
    pip install -r requirements.txt
    ```
- أمر التشغيل:
    ```
    python main.py
    ```

## ملاحظات
- لا ترفع ملف `.env` إلى GitHub!
- راقب السجلات (Logs) للتأكد من عمل البوت بشكل صحيح.