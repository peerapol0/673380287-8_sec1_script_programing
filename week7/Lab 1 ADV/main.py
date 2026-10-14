from pathlib import Path

from src.config_parser import ConfigParser
from src.scraper_agent import ScraperAgent
from src.utils import save_data_to_json


PROJECT_ROOT = Path(__file__).parent


def main():
    config_path = PROJECT_ROOT / "configs" / "example_site_config.json"
    output_path = PROJECT_ROOT / "data" / "scraped_products.json"

    config = ConfigParser(str(config_path)).load_config()
    agent = ScraperAgent(config=config, browser="chrome", headless=True)
    results = agent.run()

    save_data_to_json(results, str(output_path))
    print(f"Successfully scraped {len(results)} items and saved to {output_path}")


if __name__ == "__main__":
    main()
