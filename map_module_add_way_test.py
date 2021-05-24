import folium
import os
import data_base as db

map = folium.Map(location=[53.2521, 34.3717], zoom_start=14)


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
        folium.PolyLine(locations=[(53.262993, 34.341527), (53.262369, 34.338932)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.262369, 34.338932), (53.260535, 34.340564)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.260535, 34.340564), (53.260289, 34.339915)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.260289, 34.339915), (53.260106, 34.339848)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.260106, 34.339848), (53.257765, 34.334476)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.257765, 34.334476), (53.256867, 34.331441)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.256867, 34.331441), (53.256571, 34.331538)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.256867, 34.331441), (53.256034, 34.328589)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.256034, 34.328589), (53.25579, 34.328268)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.25579, 34.328268), (53.255367, 34.328329)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.255367, 34.328329), (53.248446, 34.334189)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.248446, 34.334189), (53.248453, 34.334492)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.248453, 34.334492), (53.249269, 34.337292)], line_opacity=0.5).add_to(map)
        folium.PolyLine(locations=[(53.249269, 34.337292), (53.249355, 34.337203)], line_opacity=0.5).add_to(map)

        map.save("templates" + "\\" + map_name + ".html")



def set_cor_for_admin(courier_id=[], courier_cor=[], orders_cor=[]):
    # courier_login = db.get_courier_login_by_id(courier_id)
    if len(courier_cor) > 1:
        for i in range(len(courier_cor)):
            folium.CircleMarker(location=[courier_cor[i][0], courier_cor[i][1]], radius=4,
                                popup="courier", fill=True,
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

# create_folder_with_maps()
# set_cor_for_admin([[53.256412, 34.331337], [53.255469, 34.335811]], [[53.256584, 34.334221], [53.254682, 34.336206]])
# set_cor_for_courier([53.263220, 34.341596], [[53.256412, 34.331337], [53.249489, 34.337176]])
