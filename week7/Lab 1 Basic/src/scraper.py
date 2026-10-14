import requests
from bs4 import BeautifulSoup


class SimpleWebScraper:
    """Scraper พื้นฐานสำหรับหน้า Automate the Boring Stuff."""

    def __init__(self, target_url: str):
        self.target_url = target_url

    def _get_html_content(self):
        print(f"กำลังดาวน์โหลดเนื้อหาจาก: {self.target_url}")
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }

        try:
            response = requests.get(
                self.target_url,
                headers=headers,
                timeout=30,
            )
            response.raise_for_status()
            print("ดาวน์โหลดเนื้อหาสำเร็จ")
            return response.text
        except requests.exceptions.HTTPError as error:
            status_code = error.response.status_code if error.response else "ไม่ทราบ"
            print(f"เกิดข้อผิดพลาด HTTP: {error} - Status Code: {status_code}")
        except requests.exceptions.ConnectionError as error:
            print(f"เกิดข้อผิดพลาดการเชื่อมต่อ: {error}")
        except requests.exceptions.Timeout:
            print("การ request หมดเวลา")
        except requests.exceptions.RequestException as error:
            print(f"เกิดข้อผิดพลาด request ที่ไม่คาดคิด: {error}")

        return None

    def scrape_main_titles(self):
        """ดึงชื่อหนังสือและชื่อบทจากหน้าเว็บเป้าหมาย."""
        html_content = self._get_html_content()
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, "html.parser")

        book_title = "ไม่พบชื่อหนังสือ"
        article_tag = soup.find("article")
        if article_tag:
            heading_tag = article_tag.find(["h1", "h2"])
            if heading_tag:
                book_title = heading_tag.get_text(" ", strip=True)

        chapter_titles = []
        content_body = soup.find("div", class_="content-body")
        if content_body:
            for link in content_body.select("ul li a"):
                title = link.get_text(" ", strip=True)
                if title:
                    chapter_titles.append(title)

        return {
            "book_title": book_title,
            "chapter_titles": chapter_titles,
        }
