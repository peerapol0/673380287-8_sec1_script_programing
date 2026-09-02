# Agentic Data Processor — Advanced CSV & JSON Workflows

A configuration-driven `DataAgent` that executes a multi-step data pipeline: aggregating
CSV sales data, converting it to JSON, and updating a nested JSON inventory file — all
defined declaratively in `configs/data_pipeline_config.json`.

## Key Concepts

- **Agentic workflow orchestration** — `DataAgent` reads the task list in the config and runs
  each task in order.
- **Internal data store** — `self.data_store` passes intermediate results between tasks via
  `input_data_key` / `output_data_key`.
- **Advanced CSV processing** — load, aggregate (sum/count/average) by group, filter, save.
- **Advanced JSON processing** — load, dot-notation `set` / `add_to_list` / `remove_from_list`
  updates on nested structures, dot-notation query, save.
- **Cross-format conversion** — CSV rows → JSON objects (with type coercion) and JSON → CSV
  (with simple nested-key flattening).
- **Audit logging** — every task's start/success/failure is recorded and written to
  `reports/audit_report_<timestamp>.json`.

## Project Structure

```
agentic-data-processor/
├── src/
│   ├── __init__.py
│   ├── data_agent.py        # Orchestrator: dispatches tasks, manages data_store
│   ├── csv_tasks.py         # load/save/aggregate/filter for CSV
│   ├── json_tasks.py        # load/save/update/query for JSON
│   ├── conversion_tasks.py  # CSV <-> JSON conversion
│   ├── config_parser.py     # Loads & validates the pipeline config
│   └── utils.py             # Logging, directory helpers, audit logging
├── configs/
│   └── data_pipeline_config.json
├── data/
│   ├── input_sales.csv               # sample input
│   ├── input_inventory.json          # sample input
│   ├── processed_sales_by_customer.csv  # output
│   ├── sales_data.json                  # output
│   └── updated_inventory.json           # output
├── main.py
├── .gitignore
└── README.md
```

## How to Run

Requires only the Python standard library (no external dependencies).

```bash
cd agentic-data-processor
python main.py
```

This will:
1. Load `data/input_sales.csv`.
2. Aggregate total `Amount` by `Customer` → save to `data/processed_sales_by_customer.csv`.
3. Convert the raw sales rows to JSON → save to `data/sales_data.json`.
4. Load `data/input_inventory.json`.
5. Apply updates (restock, edit nested `details`, append a new product) and save the
   result to `data/updated_inventory.json`.
6. Query one nested field (`0.details.brand`) as a demonstration.
7. Write a full audit trail to `reports/audit_report_<timestamp>.json`.

## Viewing Results in VS Code

Open the `agentic-data-processor` folder in VS Code, then open:
- `data/processed_sales_by_customer.csv` — VS Code shows it as plain text or, with the
  "Edit CSV" / "Rainbow CSV" extension, as a formatted table.
- `data/sales_data.json`
- `data/updated_inventory.json`

Both JSON files render with syntax highlighting and folding out of the box.

## Debugging Notes

- `FileNotFoundError`: confirm `data/input_sales.csv` and `data/input_inventory.json` exist.
- `KeyError`-style issues: check that CSV headers (`Customer`, `Amount`) and JSON keys
  (`id`, `stock`, `details`) match what the config expects.
- Nothing changing: verify `output_data_key` of one task matches the `input_data_key`
  of the next task you expect to chain.
- Check `reports/audit_report_*.json` for a full per-task log of status and details.
