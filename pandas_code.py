#Versão otimizada via Pandas, funcional para alteração de csv automatizada

import pandas as pd

old_file = pd.read_csv('products_export_1.csv', delimiter=',', header='infer', index_col='Handle', engine=None, converters=None, 
    true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, keep_default_na=True, na_filter=True, 
    verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, 
    dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', decimal='.', lineterminator=None, 
    quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, 
    error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False,
    float_precision=None, storage_options=None)

seo_file = pd.read_csv('products_export_teste.csv', delimiter=',', header='infer', index_col='Handle', engine=None, converters=None, 
    true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, keep_default_na=True, na_filter=True, 
    verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, 
    dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', decimal='.',lineterminator=None, quotechar='"', quoting=0, 
    doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, 
    on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False,float_precision=None, storage_options=None)

old_file = pd.DataFrame(old_file)
seo_file = pd.DataFrame(seo_file)

for column in seo_file.columns:
    old_file[column] = seo_file[column]

old_file.to_csv('seo_file_atualizado.csv')

old_file.loc[old_file['SEO Title'] == seo_file['SEO Title'], 'Report'] = 'Otimizado'  
old_file.loc[old_file['SEO Title'] != seo_file['SEO Title'], 'Report'] = 'Não alterado'  

print(old_file.Report.str.count("Otimizado").sum())

report = pd.DataFrame(old_file, columns = ['Report'])

report.to_csv('report.csv')