# Python brazilian currency deflator

A simple python package to deflate historical yearly or monthly values using IPCA (Consumers Broad Price Index).

Throught IPEA Data's API the function gather historical IPCA yearly (PRECOS_IPCAG series) and monthly (PRECOS12_IPCAG12 series) indexes to deflate currency values.

### Installation:

- `pandas` and `requests` packages are required in your environment (`python -m pip install pandas requests`).
- Install the package (`pip install deflatepybr`)

### Usage:
The function takes 5 arguments:
- `data_frame`: A `Pandas.DataFrame` with the data;
- `value_column`(str): A column containing the values to deflate;
- `date_column`(str): Column name from `data_frame` with the date range;
- `deflate_year`(int): Year that you wanna deflate the series to;
- `deflate_month`(int), optional: Month to deflate if you need monthly index values.

If only `deflate_year` is passed, the functions assumes that Yearly values are desired.

Examples can be found in the `example.ipynb` jupyter notebook file available on the project's Github page.
