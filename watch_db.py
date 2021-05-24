import pickle
import data_base2 as db

# with open("data_base.db", "rb") as data:
#     all_data = pickle.load(data)
#     print(all_data)

print(db.get_start_courier_location_list(db.get_all_couriers_id()))
