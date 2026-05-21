import csv
from datetime import datetime

class RegionalDataPipeline:
    def __init__(self, data_source_name):
        self.source = data_source_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[SYSTEM INITIALIZED] Tracking active for source: {self.source}")

    def fetch_market_metrics(self):
        """Simulates automated retrieval of localized market and logistics data."""
        print(f"[{self.timestamp}] Connecting to data distribution endpoints...")
        simulated_raw_payload = [
            {"item_id": "101", "region": "Multan_South", "index_value": "2450.50", "status": "Stable"},
            {"item_id": "102", "region": "Khanewal_Central", "index_value": "2610.00", "status": "High_Demand"},
            {"item_id": "103", "region": "Punjab_East", "index_value": "2390.25", "status": "Correction"}
        ]
        return simulated_raw_payload

    def process_and_compile(self, raw_data):
        """Transforms raw logistics structures into clean business files."""
        output_filename = "business_metrics_report.csv"
        fields = ["item_id", "region", "index_value", "status"]
        
        try:
            with open(output_filename, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                writer.writeheader()
                for row in raw_data:
                    writer.writerow(row)
            print(f"[SUCCESS] Operational report compiled successfully: {output_filename}")
            return True
        except IOError as e:
            print(f"[ERROR] Subsystem write failure: {e}")
            return False
