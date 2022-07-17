import time
import json

import requests

from config_module_first import HEADER_AUTH, DATA_PRODUCTS, ADRESS
from date import today, yesterday_good_format
from consts import KEY_DATA, KEY_NAME, KEY_METRICS, KEY_DIMENSION, KET_RESULT
from google_sheet import sheet_products


def module_first():

    response = requests.post(ADRESS, headers=HEADER_AUTH, json=DATA_PRODUCTS)

    data_products = response.json()
    format_data_products = json.dumps(data_products)
    data_products_json = json.loads(format_data_products)

    datas = data_products_json[f'{KET_RESULT}'][f'{KEY_DATA}']

    products = []
    list_hits_view = []
    list_hits_view_pdp = []
    list_ordered_units = []
    list_revenue = []
    list_adv_sum_all = []

    for data_one in datas:
        all_products_dict = dict(data_one)

        name_element = dict(all_products_dict[f'{KEY_DIMENSION}'][0])
        metric_element = list(all_products_dict[f'{KEY_METRICS}'])

        hits_view = metric_element[0]
        hits_view_pdp = metric_element[1]
        ordered_units = metric_element[2]
        revenue = metric_element[3]
        adv_sum_all = metric_element[4]

        products.append(name_element[f'{KEY_NAME}'])
        list_hits_view.append(hits_view)
        list_hits_view_pdp.append(hits_view_pdp)
        list_ordered_units.append(ordered_units)
        list_revenue.append(revenue)
        list_adv_sum_all.append(adv_sum_all)

    for name_product, metric_1, metric_2, metric_3, metric_4, metric_5 in zip(products, list_hits_view,
                                                                              list_hits_view_pdp,
                                                                              list_ordered_units, list_revenue,
                                                                              list_adv_sum_all):
        values_col_names = sheet_products.col_values(2)
        nums_col_names = len(values_col_names)
        row_write = nums_col_names + 1

        sheet_products.update(f'A{row_write}:{row_write}',
                              [[
                                  today,
                                  f"{yesterday_good_format} - {today}",
                                  name_product,
                                  metric_1,
                                  metric_2,
                                  metric_3,
                                  metric_4,
                                  metric_5,
                              ]
                              ])
        time.sleep(2)
