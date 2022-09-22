# Código original importando biblioteca docopt solicitando através das labels do arquivo

""" scriptTitles
Usage:
    scriptTitles  <original_file_name.dat> <original_file_name2.dat> <report_file.dat> 
"""
#!/usr/bin/env python3

import csv
from docopt import docopt

args = docopt(__doc__)

with open(args['<original_file_name.dat>'], 'r', encoding='utf8') as file_input, open(args['<original_file_name2.dat>'], 'r', encoding='utf8') as file_input2, open(args['<report_file.dat>'], 'w', encoding='utf8') as report_file :    
    writer = csv.writer(report_file, delimiter=',') 
    reader = csv.DictReader(file_input, delimiter=',')
    reader2 = csv.DictReader(file_input2, delimiter=',')

    writer.writerow
    ([  
        'Handle',
        'Title',
        'Body (HTML)',
        'Vendor', 
        'Standardized Product Type', 
        'Custom Product Type',
        'Tags',
        'Published',
        'Option1 Name',
        'Option1 Value',
        'Option2 Name',
        'Option2 Value',
        'Option3 Name',
        'Option3 Value',
        'Variant SKU',
        'Variant Grams',
        'Variant Inventory Tracker',
        'Variant Inventory Qty',
        'Variant Inventory Policy',
        'Variant Fulfillment Service',
        'Variant Price',
        'Variant Compare At Price',
        'Variant Requires Shipping',
        'Variant Taxable',
        'Variant Barcode',
        'Image Src',
        'Image Position',
        'Image Alt Text',
        'Gift Card',
        'SEO Title',
        'SEO Description',
        'Google Shopping / Google Product Category',
        'Google Shopping / Gender',
        'Google Shopping / Age Group',
        'Google Shopping / MPN',
        'Google Shopping / AdWords Grouping',
        'Google Shopping / AdWords Labels',
        'Google Shopping / Condition',
        'Google Shopping / Custom Product',
        'Google Shopping / Custom Label 0',
        'Google Shopping / Custom Label 1',
        'Google Shopping / Custom Label 2',
        'Google Shopping / Custom Label 3',
        'Google Shopping / Custom Label 4',
        'Variant Image',
        'Variant Weight Unit',
        'Variant Tax Code',
        'Cost per item',
        'Price / Internacional',
        'Compare At Price / Internacional',
        'Status'                                      
    ])

    for row in reader:
        handle = row['Handle']
        title = row['Title']
        body = row['Body (HTML)']
        vendor = row['Vendor']
        sptype = row['Standardized Product Type']
        tags = row['Tags']
        published = row['Published']
        opt1name = row['Option1 Name']
        opt1value = row['Option1 Value']
        opt2name = row['Option2 Name']
        opt2value = row['Option2 Value']
        opt3name = row['Option3 Name']
        opt3value = row['Option3 Value']
        variantsku = row['Variant SKU']
        variantgrams = row['Variant Grams']
        variantit = row['Variant Inventory Tracker']
        variantiq = row['Variant Inventory Qty']
        variantip = row['Variant Inventory Policy'] 
        variantfs = row['Variant Fulfillment Service']
        variantprice = row['Variant Price']
        variantcap = row['Variant Compare At Price']
        variantrs = row['Variant Requires Shipping',]
        varianttax = row['Variant Taxable']
        variantbc = row['Variant Barcode']
        imagesrc = row['Image Src']
        imagepos = row['Image Position']
        imagealttxt = row['Image Alt Text']
        giftcard = row['Gift Card']
        seotitle = row['SEO Title']
        seodescription = row['SEO Description']
        googlespc = row['Google Shopping / Google Product Category']
        googlesg = row['Google Shopping / Gender']  
        googlesag = row['Google Shopping / Age Group']  
        googlesmpn = row['Google Shopping / MPN']  
        googlesadwg = row['Google Shopping / AdWords Grouping']  
        googlesadwl = row['Google Shopping / AdWords Labels']  
        googlesc = row['Google Shopping / Condition']  
        googlescp = row['Google Shopping / Custom Product']  
        googlescl0 = row['Google Shopping / Custom Label 0']  
        googlescl1 = row['Google Shopping / Custom Label 1']  
        googlescl2 = row['Google Shopping / Custom Label 2']  
        googlescl3 = row['Google Shopping / Custom Label 3']  
        googlescl4 = row['Google Shopping / Custom Label 4']
        variantimg = row['Variant Image']
        variantwu = row['Variant Weight Unit']
        varianttc = row['Variant Tax Code']
        costperitem = row['Cost per item']
        priceinternational = row['Price / Internacional']
        capinternational = row['Compare At Price / Internacional'] 
        status = row['Status']             


    for row in reader:            
        writer.writerow
        ([
            handle,
            title, 
            body, 
            vendor, 
            sptype,
            tags,
            published,
            opt1name,
            opt1value,
            opt2name,
            opt2value,
            opt3name,
            opt3value,
            variantsku,
            variantgrams,
            variantit,
            variantiq,
            variantip,
            variantfs,
            variantprice,
            variantcap,
            variantrs,
            varianttax,
            variantbc,
            imagesrc,
            imagepos,
            imagealttxt,
            giftcard,
            seotitle,
            seodescription,
            googlespc,
            googlesg,
            googlesag,
            googlesmpn,
            googlesadwg,
            googlesadwl,
            googlesc,
            googlescp,
            googlescl0,
            googlescl1,
            googlescl2,
            googlescl3,
            googlescl4,
            variantimg,
            variantwu,
            varianttc,
            costperitem,
            priceinternational,
            capinternational,
            status
        ])