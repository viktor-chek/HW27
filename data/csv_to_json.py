import csv
import json

ads_file = 'ads'
categories_file = 'categories'


def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as f:
        for i in csv.DictReader(f):
            to_add = {
                'model': model, 'pk': int(i['Id'] if 'Id' in i else i['id'])
            }
            if 'id' in i:
                del i['id']
            else:
                del i['Id']
            to_add['fields'] = i

            if 'is_published' in i:
                if i['is_published'] == 'TRUE':
                    i['is_published'] = True
                else:
                    i['is_published'] = False
            if 'price' in i:
                i['price'] = int(i['price'])
            to_add['fields'] = i
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))


convert_file(f'{ads_file}.csv', f'{ads_file}.json', 'ads.ad')
convert_file(f'{categories_file}.csv', f'{categories_file}.json', 'ads.category')
