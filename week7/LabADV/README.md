# Agentic Web Scraper

โปรเจกต์ตัวอย่างสำหรับเรียนรู้การ scrape เนื้อหาแบบ dynamic ด้วย Selenium และการกำหนดพฤติกรรมผ่านไฟล์ JSON configuration

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

เลือก Python interpreter ของ `.venv` ใน VS Code แล้วรัน:

```powershell
python main.py
```

ผลลัพธ์จะถูกบันทึกที่ `data/scraped_products.json` โดยตัวอย่างนี้ใช้เว็บไซต์สำหรับการทดสอบ `books.toscrape.com` เท่านั้น

## โครงสร้าง

- `src/scraper_agent.py`: วนหน้าและดึงข้อมูลตาม config
- `src/config_parser.py`: โหลดและตรวจสอบ config
- `src/data_models.py`: dataclass สำหรับข้อมูลสินค้า
- `src/driver_manager.py`: ตั้งค่า Chrome หรือ Firefox WebDriver
- `src/utils.py`: รอ element, คลิก และบันทึก JSON
- `configs/example_site_config.json`: ตัวอย่างกฎการ scrape
- `docs/ETHICS.md`: แนวทางการใช้งานอย่างรับผิดชอบ
