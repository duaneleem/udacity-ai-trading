# Artificial Intelligence for Trading built by WorldQuant & Udacity
Notes on the topics of AI engineering for Trading I have went through.


## Tar Project Folder
Run the following in a cell to tar:
``` !tar chvfz notebook.tar.gz * ```

In a bash terminal:
``` tar -zxvf notebook.tar.gz ```


## Create Virtual Environment
```sh
python3 -m venv env
source env/bin/activate
deactivate
```

Docs: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/


## Download an unreachable CSV
```python
from IPython.display import FileLink, FileLinks
df.to_csv('./temp-data.csv', index=False)
df.to_excel('./temp-data.xlsx', index=False)

FileLinks('./')
```


