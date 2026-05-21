from core.pipeline import RegionalDataPipeline

def main():
    print("==================================================")
    print("[START] Launching Regional Data Orchestration Pipeline")
    print("==================================================")
    
    # Core system instantiation
    pipeline = RegionalDataPipeline(data_source_name="Central_Agri_Logistics_Stream")
    
    # Process orchestration cycle
    raw_payload = pipeline.fetch_market_metrics()
    pipeline.process_and_compile(raw_payload)
    
    print("==================================================")
    print("[SUCCESS] Pipeline Execution Completed.")
    print("==================================================")

if __name__ == "__main__":
    main()
