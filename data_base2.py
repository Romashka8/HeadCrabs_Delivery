import pickle
import os


# this function create data_base.db
# all_data[0] = couriers, all_data[1] = orders, all_data[2] = order_to_courier, all_data[3] = start_courier_location
def create_data_base():
    if os.path.exists(os.getcwd() + r"\data_base.db") is False:
        with open("data_base.db", "wb") as data:
            all_data = [{}, {}, {}, {}]
            pickle.dump(all_data, data)
        return "Ok, data_base was created!"
    return "Ok, data_base already created!"


# this function create admin_data.db
# basic_admin_data: 0 == admin_login and admin_password; 1 == applications from new couriers
def create_admin_data():
    if os.path.exists(os.getcwd() + r"\admin_data.db") is False:
        with open("admin_data.db", "wb") as data:
            basic_admin_data = [{"admin": "admin"}, []]
            # basic_admin_data = {"admin": "admin"}
            pickle.dump(basic_admin_data, data)
        return "Ok, admin_data was created!"
    return "Ok, admin_data already created!"


# this function give you all information from data_base.db
def get_all_data():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        return all_data


# this function must delete all data_base.db
def delete_db():
    if os.path.exists(os.getcwd() + r"\data_base.db") is True:
        os.remove(os.getcwd() + r"\data_base.db")
        return "Data base was removed successfully!"
    return "Data base was not found!"


# this function must delete "admin_data.db" with one condition:
# admin_login and admin_password that function get must fit with admin_login and admin_password in "admin_data.db".
def delete_admin_data(admin_login=None, admin_password=None):
    if os.path.exists(os.getcwd() + r"\admin_data.db") is False:
        return "admin_data was not found!"
    # with open("admin_data.db", "rb") as data:
    #     all_data = pickle.load(data)
    if check_admin(admin_login, admin_password) is True:
        os.remove(os.getcwd() + r"\admin_data.db")
        return "All admin data was deleted successfully!"
    return "Incorrect authorization data!"


# comparison gotten admin data with truthful admin data
def check_admin(admin_login, admin_password):
    with open("admin_data.db", "rb") as data:
        admin_data = pickle.load(data)
    if admin_login in admin_data[0]:
        if admin_data[0][admin_login] == admin_password:
            return True
        return False
    return False


# this function checks courier id. If his in data_base => True, else => False
def check_courier_id(courier_id):
    with open("data_base.db", "rb") as all_data:
        data = pickle.load(all_data)
        data = data[0]
    if (courier_id in data) is False:
        return False
    return True


# this function function get courier login by gotten courier id
def get_courier_login_by_id(courier_id):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers = all_data[0]
            courier_login = all_couriers[courier_id]
            return courier_login
    return False


# this function add courier in data_base.db
def add_courier(courier_id, courier_login):
    if check_courier_id(courier_id) is False:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            courier_data = all_data[0]
            courier_data[f"{courier_id}"] = courier_login
            all_data[0] = courier_data
            pickle.dump(all_data, data)


# this function add application in admin_data.db
# application - courier ask admin to add his in data_base.db
def add_application_to_admin(name, short_message=""):
    create_admin_data()
    with open("admin_data.db", "rb") as data:
        all_data = pickle.load(data)
    with open("admin_data.db", "wb") as data:
        all_applications = all_data[1]
        application = f"Имя:{name}" + "\n" + f"Короткое сообщение:{short_message}"
        all_applications.append(application)
        all_data[1] = all_applications
        pickle.dump(all_data)


# this function return all couriers id in data_base.db
def get_all_couriers_id():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    couriers_keys = list(all_data[0].keys())
    return couriers_keys


# this function return all start location of all couriers in list
def get_start_courier_location_list(all_couriers_id=[]):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    couriers_with_locations = all_data[3]
    all_start_cor = []
    for i in all_couriers_id:
        if i in couriers_with_locations:
            all_start_cor.append(couriers_with_locations[i])
    return all_start_cor


# this function get all orders in data_base.db
def get_all_orders_location():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        all_orders = all_data[1]
        all_orders = all_orders.keys()
        all_orders_list = []
        for i in all_orders:
            all_orders_list.append([float(i[0:i.find("|")]), float(i[i.find("|") + 1:])])
        return all_orders_list


# this function allows to add order to courier
def add_order_to_courier(courier_id, order_location):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "wb") as data:
            order_to_courier = all_data[2]
            order_to_courier[f"{courier_id}"] = order_location
            all_data[2] = order_to_courier
            pickle.dump(all_data, data)


def get_cur_order_loc(courier_id):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        all_data = all_data[2]
        return all_data[courier_id]


# this function return all busy couriers
def get_all_ord_to_cour():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    ord_to_cour = all_data[2]
    return ord_to_cour


# this function check courier login and courier id in data_base.db
def check_login(courier_id, courier_login):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers = all_data[0]
            if all_couriers[courier_id] == courier_login:
                return True
            return False


# this function return start location of one courier
def get_start_courier_location(courier_id):
    if check_courier_id(courier_id) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_couriers_location = all_data[3]
            courier_location = all_couriers_location[courier_id]
            return courier_location
    return "This courier does not have start location!"


# change type of courier data
def order_cor_in_str(order_cor):
    if len(order_cor) == 0:
        return ""
    order_cor[0], order_cor[1] = str(order_cor[0]), str(order_cor[1])
    str_order = order_cor[0] + "|" + order_cor[1]
    return str_order


def get_order_name_by_location(order_cor):
    if type(order_cor) == "list":
        order_cor = order_cor_in_str(order_cor)
    if check_order_id(order_cor) is True:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
            all_orders = all_data[1]
            # add function that convert string in dict key!(if you forget, run main).
            return all_orders[order_cor]
    return "No orders with this location!"


def get_orders_dict_from_data():
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        return all_data[1]


def check_order_status(order_loc):
    if type(order_loc) == "list":
        order_loc = order_cor_in_str(order_loc)
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        all_orders_to_cour = all_data[2]
        for i in all_orders_to_cour:
            if all_orders_to_cour[i] == order_loc:
                return True
        return False


def check_courier_status(courier_id):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
        all_orders_to_cour = all_data[2]
        if courier_id in all_orders_to_cour:
            return True
        return False


# this function check order in data_base.db
def check_order_id(order_id):
    if type(order_id) == list:
        order_id = order_cor_in_str(order_id)
    with open("data_base.db", "rb") as all_data:
        data = pickle.load(all_data)
        data = data[1]
        data = data.keys()
    if (order_id in data) is False:
        return False
    return True


# need new version of this function!!!
# this function remove order from data_base.db
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


# this function add order into data_base.db
def add_order(order_location, order_name):
    order_location = order_cor_in_str(order_location)
    if check_order_id(order_location) is False:
        with open("data_base.db", "rb") as data:
            all_data = pickle.load(data)
        with open("data_base.db", "wb") as data:
            order_data = all_data[1]
            order_data[order_location] = order_name
            all_data[1] = order_data
            pickle.dump(all_data, data)


# this function add courier his start location
def add_start_courier_location(courier_id, start_location):
    with open("data_base.db", "rb") as data:
        all_data = pickle.load(data)
    with open("data_base.db", "wb") as data:
        start_courier_location = all_data[3]
        start_courier_location[f"{courier_id}"] = start_location
        all_data[3] = start_courier_location
        pickle.dump(all_data, data)


def main():
    create_data_base()
    create_admin_data()
    add_courier("4639", "Roman")
    add_courier("6749", "Artyom")
    add_courier("3930", "Raul")
    add_courier("0116", "Duck")
    add_order([53.256412, 34.331337], "test1")
    add_order([53.249489, 34.337176], "test2")
    add_order([53.258442, 34.332326], "test3")
    add_order([53.258442, 34.332326], "test4")
    add_order([53.254763, 34.337329], "test5")
    add_order([53.255771, 34.334329], "test6")
    add_order([53.248780, 34.349472], "test7")
    add_order([53.251623, 34.339415], "test8")
    add_order([53.252547, 34.339554], "test9")
    add_order([53.255602, 34.337151], "test10")
    add_start_courier_location("4639", [53.263220, 34.341596])
    add_start_courier_location("6749", [53.258712, 34.327277])
    add_start_courier_location("3930", [53.266150, 34.332263])
    add_start_courier_location("0116", [53.356412, 34.431337])
    add_order_to_courier("4639", [53.256412, 34.331337])
    # test = Courier("1", "test", "Bryansk")
    # print(type(test) == Courier)


# before creation admins object, you must check admin data from server(gotten data) with check_admin()
# example:
# if check_admin(gotten_admin_login, gotten_admin_password) is True:
#     test = Administrator(gotten_admin_login, gotten_admin_password)
# else:
#   return "Gotten data is incorrect!"
class Administrator:
    def __init__(self, admin_login, admin_password):
        self.admin_login = admin_login
        self.admin_password = admin_password


class Courier:
    def __init__(self, courier_id, courier_login, start_location):
        self.courier_id = courier_id
        self.courier_login = courier_login
        self.location = start_location
        self.permission_to_change = False

    def change_location(self, new_location):
        self.location = new_location

    def check_permission(self):
        if self.permission_to_change is True:
            return True
        return False

    def change_login(self, new_login):
        with open("admin_data.db", "rb") as data:
            all_data = pickle.load(data)
        with open("admin_data.db", "wb") as data:
            all_courier_data = all_data[0]
            all_courier_data[get_courier_login_by_id(self.courier_id)] = new_login
            self.courier_login = new_login
            all_data[0] = all_courier_data
            pickle.dump(all_data)


main()
# a = get_all_ord_to_cour()
# print(a)
# print(get_cur_order_loc("4639"))
