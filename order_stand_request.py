import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order)


def get_order_by_track(track):
    return requests.get(url=configuration.URL_SERVICE + configuration.ORDER_INFO + str(track))
