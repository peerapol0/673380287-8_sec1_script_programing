from src.scraper import SimpleWebScraper


def main():
    target_url = "https://automatetheboringstuff.com/3e/"
    scraper = SimpleWebScraper(target_url)
    scraped_data = scraper.scrape_main_titles()

    if scraped_data:
        print("\n--- ข้อมูลที่ Scrape ได้ ---")
        print(f"ชื่อหนังสือ: {scraped_data['book_title']}")
        print("\nชื่อบทต่างๆ:")
        if scraped_data["chapter_titles"]:
            for index, title in enumerate(scraped_data["chapter_titles"], start=1):
                print(f"{index}. {title}")
        else:
            print("ไม่พบชื่อบทใดๆ")
        print("--------------------")
    else:
        print("ไม่สามารถ scrape ข้อมูลได้")


if __name__ == "__main__":
    main()
