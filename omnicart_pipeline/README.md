
# Omnicart Data Pipeline

A simple Python data pipeline for enriching, analyzing, and aggregating product and user data.

## Features

* **Data Enrichment**
  Combines product and user data into a single DataFrame using DuckDB for SQL-style joins. Calculates revenue for each product based on price and rating count.

* **Data Analysis**
  Aggregates enriched data by seller (`username`) to compute:

  * Total revenue per seller
  * Total products sold per seller
  * Average product price per seller

* **Config Management**
  Reads API configuration (base URL and limits) from a `.cfg` file using a `ConfigManager`.

## Installation

```bash
pip install pandas duckdb
```
```

## Testing

Run tests with pytest:

```bash
pytest
```

Tests cover:

* Data enrichment (joins, revenue calculation, handling missing users)
* Data analysis (grouping, aggregation)
* Configuration file reading

## Requirements

* Python 3.8+
* `pandas`
* `duckdb`
* `pytest` (for running tests)


