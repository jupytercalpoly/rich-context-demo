import IPython.display
import pandas

def display_datasets(*datasets):
    IPython.display.publish_display_data({
        'application/x.jupyter.dataset+json': datasets
    })


def display_dataset(mime_type, url, data):
    display_datasets({
        "mimeType": mime_type,
        "url": url,
        "data": data
    })

def display_url_dataset(url):
    display_dataset(f'application/x.jupyter.resolve', url, None)

def display_file_dataset(path):
    display_dataset(f'application/x.jupyter.resolver', f"file:///{path}", None)

    
def display_pandas_dataset(dataframe):
    path = 'tmp.csv'
    dataframe.to_csv(path, index=False)
    display_file_dataset(path)