import pickle
import os

cur_path = os.getcwd() + r"\data_base.db"


def create_path(path):
    if os.path.exists(path) is False:
        with open("data_base.db", "wb") as data:
            all_data = [{}, [], {}, {}]
            pickle.dump(all_data, data)
        return "Ok, data_base was created!"
    else:
        return "Ok, data_base already created!"


def add_courier(courier_id, courier_login):
    if check_courier_id(courier_id) is False:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            courier_data = all_data[0]
            courier_data[f"{courier_id}"] = courier_login
            all_data[0] = courier_data
            pickle.dump(all_data, data)


def get_all_couriers_id():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    couriers_keys = list(all_data[0].keys())
    return couriers_keys


def add_order(order_location):
    if check_order_id(order_location) is False:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            order_data = all_data[1]
            order_data.append(order_location)
            all_data[1] = order_data
            pickle.dump(all_data, data)


def add_order_to_courier(courier_id, order_location):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    with open("data_base.db", "wb") as data:
        order_to_courier = all_data[2]
        order_to_courier[f"{courier_id}"] = order_location
        all_data[2] = order_to_courier
        pickle.dump(all_data, data)


def get_all_ord_to_cour():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    ord_to_cour = all_data[2]
    return ord_to_cour


def add_start_courier_location(courier_id, start_location):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    with open("data_base.db", "wb") as data:
        start_courier_location = all_data[3]
        start_courier_location[f"{courier_id}"] = start_location
        all_data[3] = start_courier_location
        # print(all_data[3])
        pickle.dump(all_data, data)


def check_courier_id(courier_id):
    with open("data_base.db", "rb") as all_data:
        data = pickle.load(all_data)
        data = data[0]
    if (courier_id in data) is False:
        return False
    return True


def check_order_id(order_id):
    with open("data_base.db", "rb") as all_data:
        data = pickle.load(all_data)
        data = data[1]
    if (order_id in data) is False:
        return False
    return True


def create_admin_data():
    with open("admin_data.db", "wb") as data:
        basic_admin_data = {"admin": "admin"}
        pickle.dump(basic_admin_data, data)


def check_admin(admin_login, admin_password):
    with open("admin_data.db", "rb") as data:
        admin_data = pickle.load(data)
    if admin_login in admin_data:
        if admin_data[admin_login] == admin_password:
            return True
        return False
    return False


def get_all_data():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        return all_data


def get_courier_login_by_id(courier_id):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers = all_data[0]
            courier_login = all_couriers[courier_id]
            return courier_login
    return False


def check_id_and_location(courier_id, location):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    if check_courier_id(courier_id) is True:
        cour_and_locs = all_data[3]
        if cour_and_locs[courier_id] == location:
            return True
        return False


def get_start_courier_location(courier_id):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers_location = all_data[3]
            courier_location = all_couriers_location[courier_id]
            return courier_location
    return "This courier does not have start location!"


def get_start_courier_location_list(all_couriers_id=[]):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    couriers_with_locations = all_data[3]
    all_start_cor = []
    for i in all_couriers_id:
        if i in couriers_with_locations:
            all_start_cor.append(couriers_with_locations[i])
    return all_start_cor


def get_all_orders():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        all_orders = all_data[1]
        return all_orders


def add_order_to_courier(courier_id, order_id):
    if check_courier_id(courier_id) is True and check_order_id(order_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            all_order_to_courier = all_data[2]
            all_order_to_courier[courier_id] = order_id
            all_data[2] = all_order_to_courier
            pickle.dump(all_data, data)


def remove_order(order_id=[]):
    if check_order_id(order_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            orders = all_data[1]
            for i in orders:
                if i == order_id:
                    del i
            all_data[1] = orders
            pickle.dump(all_data, data)


def check_login(courier_id, courier_login):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers = all_data[0]
            if all_couriers[courier_id] == courier_login:
                return True
            return False


def main():
    os.remove("data_base.db")
    create_path(cur_path)
    create_admin_data()
    add_courier("4639", "Roman")
    add_courier("6749", "Artyom")
    add_courier("3930", "Raul")
    add_order([53.256412, 34.331337])
    add_order([53.249489, 34.337176])
    add_order([53.258442, 34.332326])
    add_order([53.258442, 34.332326])
    add_order([53.254763, 34.337329])
    add_order([53.255771, 34.334329])
    add_order([53.248780, 34.349472])
    add_order([53.251623, 34.339415])
    add_order([53.252547, 34.339554])
    add_order([53.255602, 34.337151])
    add_start_courier_location("4639", [53.263220, 34.341596])
    add_start_courier_location("6749", [53.258712, 34.327277])
    add_start_courier_location("3930", [53.266150, 34.332263])


# main()
