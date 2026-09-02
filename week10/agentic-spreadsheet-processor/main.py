# main.py
import sys
import os
from datetime import datetime

from src.utils import setup_logging
from src.config_parser import ConfigParser
from src.spreadsheet_agent import SpreadsheetAgent

logger = setup_logging(__name__)

def main():
    config_file_path = os.path.join(os.path.dirname(__file__), 'configs', 'example_spreadsheet_config.json')
    try:
        project_dir = os.path.dirname(__file__)
        os.makedirs(os.path.join(project_dir, 'data'), exist_ok=True)
        logger.info(f"Loading configuration from: {config_file_path}")
        config_parser = ConfigParser(config_file_path)
        config = config_parser.load_config()
        
        input_file_path = os.path.join(project_dir, config.get("input_file", ""))
        if not os.path.exists(input_file_path):
            logger.critical(f"❌ Input file not found: '{input_file_path}'")
            return
        
        logger.info("Initializing Spreadsheet Agent...")
        config["input_file"] = input_file_path
        config["output_file"] = os.path.join(project_dir, config.get("output_file", "data/output_report.xlsx"))
        reports_dir = os.path.join(project_dir, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        config["audit_log"] = os.path.join(
            reports_dir,
            f"audit_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        )
        agent = SpreadsheetAgent(config)
        logger.info("Running Spreadsheet Agent...")
        agent.run()
    except Exception as e:
        logger.critical(f"Critical error: {e}", exc_info=True)

if __name__ == "__main__":
    main()