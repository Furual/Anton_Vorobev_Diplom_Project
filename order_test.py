import order_stand_request


def test_get_order_ingo_by_track():
    new_order = order_stand_request.post_new_order()
    track = new_order.json()["track"]
    order_info = order_stand_request.get_order_by_track(track)
    assert order_info.status_code == 200
