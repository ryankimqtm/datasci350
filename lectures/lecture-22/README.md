# Lecture 22 - Scaling data analysis in practice

Last class we learnt the concepts. This one is the practice session: which tool do you actually reach for when the file gets big? We set up a Dask cluster and watch the dashboard while it works, then meet the two engines that made "buy a cluster" bad advice for most datasets. At the end we race pandas, Polars, DuckDB and Dask on 200 million rows and read the result honestly.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-22/22-scaling-in-practice.html)

## What we cover

- Dask clusters: workers, the scheduler, and the `Client` you create once at the top of a script
- The dashboard at `localhost:8789`, read while a real computation runs
- The 2026 reality check: why most datasets that feel large fit on one machine
- Polars: expressions, `select` and `filter`, `with_columns`, `group_by`, and how each maps to pandas
- Lazy mode with `scan_parquet` and `collect`, plus streaming for data larger than RAM
- DuckDB: SQL straight over a Parquet file, and querying a DataFrame by name
- The benchmark on 200 million rows, with the same query written four ways
- A decision framework for the four tools, then two slides on GPUs

Every output on the slides comes from a real run on my laptop (Apple M5, 10 cores, 24 GB RAM). The benchmark was measured once and saved to `data/benchmark_results.csv`.

## The data

The slides read the small WDI panel from `lectures/lecture-19/data/wdi_panel.parquet`. The benchmark reads `data/wdi_big.parquet`, which is about 1.4 GB and is not committed. Rebuild it with:

```bash
cd lectures/lecture-22/data
python make_big_parquet.py
```

The script uses a fixed seed, so everyone gets the same file. Pass `--replicas 400` for a smaller version on a slower laptop.

## Rendering

The deck runs Polars, DuckDB and Dask while it renders, so use a Python that has all three plus `pyarrow` and `yaml`:

```bash
cd lectures/lecture-22
QUARTO_PYTHON=~/miniconda3/envs/datasci/bin/python quarto render 22-scaling-in-practice.qmd
```

## Before the next class

Finish both exercises: the Polars rewrite and the DuckDB query. Time the four engines on the small panel with the code in Appendix 05. Check that `dask`, `polars` and `duckdb` all import in your environment.

Tool claims and screenshots verified 26 August 2026.
