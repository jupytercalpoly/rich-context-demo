import IPython.display
import pandas

def display_datasets(*datasets, auto_register=False):
    IPython.display.publish_display_data({
        'application/x.jupyter.dataset+json': {
            'datasets': datasets,
            'autoRegister': auto_register
        }
    })


def display_dataset(mime_type, url, data, auto_register=False):
    display_datasets({
        "mimeType": mime_type,
        "url": url,
        "data": data
    }, auto_register=auto_register)

def display_url_dataset(url, auto_register=False):
    display_dataset(f'application/x.jupyter.resolve', url, None, auto_register=auto_register)

def display_file_dataset(path, auto_register=False):
    display_url_dataset(f"file:///{path}", auto_register=auto_register)
    
def display_pandas_dataset(dataframe, auto_register=False):
    path = 'tmp.csv'
    dataframe.to_csv(path, index=False)
    display_file_dataset(path, auto_register=auto_register)
