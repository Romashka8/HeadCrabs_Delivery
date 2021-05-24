import folium
import os
import data_base as db

map = folium.Map(location=[53.25637, 34.330066], zoom_start=14)


def create_folder_with_maps():
    if os.path.exists(os.getcwd() + "/maps") is False:
        os.mkdir(os.getcwd() + "/maps")


def set_cor_for_courier(courier_id, map_name, courier_cor, orders_cor=[]):
    courier_login = db.get_courier_login_by_id(courier_id)
    if len(orders_cor) > 1:
        for i in range(len(orders_cor)):
            folium.Marker(location=[orders_cor[i][0], orders_cor[i][1]],
                          popup=str(orders_cor[i][0]) + "|" + str(orders_cor[i][1]),
                          icon=folium.Icon(icon="briefcase", color='orange')).add_to(map)
        folium.CircleMarker(location=[courier_cor[0], courier_cor[1]], radius=4, popup=courier_login, fill=True,
                            fill_Color="green", fill_opacity=1, color="green").add_to(map)
        map.save("templates" + "\\" + map_name + ".html")
    elif len(orders_cor) == 1:
        folium.Marker(location=[orders_cor[0][0], orders_cor[0][1]],
                      popup=str(orders_cor[0][0]) + "|" + str(orders_cor[0][1]),
                      icon=folium.Icon(icon="briefcase", color='orange')).add_to(map)
        folium.CircleMarker(location=[courier_cor[0], courier_cor[1]], radius=4, popup=courier_login, fill=True,
                            fill_Color="green", fill_opacity=1, color="green").add_to(map)
        map.save("templates" + "\\" + map_name + ".html")


def set_cor_for_admin(all_courier_id=[], courier_cor=[], orders_cor=[]):
    if len(courier_cor) > 1:
        for i in range(len(courier_cor)):
            run = True
            count = 0
            cour_id = None
            while run:
                if db.check_id_and_location(all_courier_id[count], courier_cor[i]) is False:
                    count += 1
                else:
                    cour_id = all_courier_id[count]
                    run = False
            folium.CircleMarker(location=[courier_cor[i][0], courier_cor[i][1]], radius=4,
                                popup=cour_id, fill=True,
                                fill_Color="green", fill_opacity=1, color="green").add_to(map)
    else:
        folium.CircleMarker(location=[courier_cor[0][0], courier_cor[0][1]], radius=4, popup="courier", fill=True,
                            fill_Color="green", fill_opacity=1, color="green").add_to(map)
    if len(orders_cor) > 1:
        for i in range(len(orders_cor)):
            folium.Marker(location=[orders_cor[i][0], orders_cor[i][1]],
                          popup=str(orders_cor[i][0]) + "|" + str(orders_cor[i][1]),
                          icon=folium.Icon(icon="briefcase", color='orange')).add_to(map)
    else:
        folium.Marker(location=[orders_cor[0][0], orders_cor[0][1]],
                      popup=str(orders_cor[0][0]) + "|" + str(orders_cor[0][1]),
                      icon=folium.Icon(icon="briefcase", color='orange')).add_to(map)
    map.save(r"templates\map_admin.html")
