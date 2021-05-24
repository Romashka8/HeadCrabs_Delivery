from flask import Flask, redirect, url_for, session, render_template, request
import data_base2 as db

app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "Very&Strong%#Key*"
app.jinja_env.globals.update(in_str=db.order_cor_in_str)


@app.route("/")
def entering():
    session["data"] = db.get_all_data()
    session["courier_id"] = None
    session["courier_login"] = None
    session["order_loc"] = None
    session["orders_location"] = session["data"][1]
    session["courier_location"] = None
    session["admin_login"] = None
    session["admin_password"] = None
    return redirect(url_for("main_page"))


@app.route("/main_page")
def main_page():
    return render_template("main_page.html", status="unknown")


@app.route("/status_courier")
def status_courier():
    return render_template("main_page.html", status="courier")


@app.route("/status_admin")
def status_admin():
    return render_template("main_page.html", status="admin")


@app.route("/admin_auth", methods=["POST", "GET"])
def admin_auth():
    if request.method == "POST":
        session["admin_login"] = request.form.get("adm_login")
        session["admin_password"] = request.form.get("adm_password")
        if db.check_admin(session["admin_login"], session["admin_password"]) is True:
            return render_template("admin_page.html", admin_login=session["admin_login"],
                                   couriers_count=len(db.get_all_couriers_id()), map_center=[53.25, 34.33],
                                   all_couriers_list=db.get_all_couriers_id(),
                                   all_couriers_start_location_list=db.get_start_courier_location_list(
                                       db.get_all_couriers_id()),
                                   orders_count=len(db.get_all_orders_location()),
                                   orders_list=db.get_all_orders_location(), orders_name=db.get_orders_dict_from_data(),
                                   cour_to_ord=db.get_all_ord_to_cour())
        return render_template("error_page.html")


@app.route("/give_order", methods=["POST", "GET"])
def give_order():
    if request.method == "POST":
        order_id = request.form.get("ord_id")
        courier_id = request.form.get("cour_id")
        if len(order_id) > 0 and len(courier_id) > 0:
            order_id = [float(order_id[:order_id.find("|")]), float(order_id[order_id.find("|") + 1:])]
            if db.check_courier_status(courier_id) is False and db.check_order_status(order_id) is False:
                db.add_order_to_courier(courier_id, order_id)
                cour_to_ord = db.get_all_ord_to_cour()
                return render_template("admin_page.html", cour_to_ord=cour_to_ord, admin_login=session["admin_login"],
                                       couriers_count=len(db.get_all_couriers_id()), map_center=[53.25, 34.33],
                                       all_couriers_list=db.get_all_couriers_id(),
                                       all_couriers_start_location_list=db.get_start_courier_location_list(
                                           db.get_all_couriers_id()),
                                       orders_count=len(db.get_all_orders_location()),
                                       orders_list=db.get_all_orders_location(),
                                       orders_name=db.get_orders_dict_from_data())
            cour_to_ord = db.get_all_ord_to_cour()
            return render_template("admin_page.html", cour_to_ord=cour_to_ord, admin_login=session["admin_login"],
                                   couriers_count=len(db.get_all_couriers_id()), map_center=[53.25, 34.33],
                                   all_couriers_list=db.get_all_couriers_id(),
                                   all_couriers_start_location_list=db.get_start_courier_location_list(
                                       db.get_all_couriers_id()),
                                   orders_count=len(db.get_all_orders_location()),
                                   orders_list=db.get_all_orders_location(), orders_name=db.get_orders_dict_from_data())
        else:
            return render_template("admin_page.html")


@app.route("/courier_auth", methods=["POST", "GET"])
def courier_auth():
    if request.method == "POST":
        session["courier_login"] = request.form.get("courier_login")
        session["courier_id"] = request.form.get("courier_id")
        if db.check_courier_id(session["courier_id"]) is True and db.check_login(session["courier_id"],
                                                                                 session["courier_login"]) is True:
            if db.check_courier_status(session["courier_id"]) is True:
                text_cur_order = db.get_order_name_by_location(
                    db.order_cor_in_str(db.get_cur_order_loc(session["courier_id"])))
                return render_template("free_courier_page.html",
                                       courier_login=db.get_courier_login_by_id(session["courier_id"]),
                                       busy="yes", cur_order=db.get_cur_order_loc(session["courier_id"]),
                                       text_cur_order=text_cur_order,
                                       courier_cor_list=db.get_start_courier_location(session["courier_id"]),
                                       map_center=[53.25, 34.33],
                                       orders_count=len(db.get_all_orders_location()))
            return render_template("free_courier_page.html",
                                   courier_login=db.get_courier_login_by_id(session["courier_id"]), busy="not",
                                   courier_cor_list=db.get_start_courier_location(session["courier_id"]),
                                   map_center=[53.25, 34.33], orders_list=db.get_all_orders_location(),
                                   orders_count=len(db.get_all_orders_location()),
                                   orders_name=db.get_orders_dict_from_data())
        return render_template("error_page.html")


@app.route("/take_order", methods=["POST", "GET"])
def take_order():
    if request.method == "POST":
        order = request.form.get("ord_id")
        if len(order) > 1:
            print(type(order), order, sep="\n")
            print(str(order[0]) + "|" + str(order[1]))
            return render_template("free_courier_page.html",
                                   courier_login=db.get_courier_login_by_id(session["courier_id"]),
                                   busy="yes", cur_order=order, text_cur_order=db.get_order_name_by_location(order),
                                   courier_cor_list=db.get_start_courier_location(session["courier_id"]),
                                   map_center=[53.25, 34.33], orders_list=db.get_all_orders_location(),
                                   orders_count=len(db.get_all_orders_location()))
        else:
            return render_template("free_courier_page.html",
                                   courier_login=db.get_courier_login_by_id(session["courier_id"]),
                                   busy="not", courier_cor_list=db.get_start_courier_location(session["courier_id"]),
                                   map_center=[53.25, 34.33], orders_list=db.get_all_orders_location(),
                                   orders_count=len(db.get_all_orders_location()))


if __name__ == "__main__":
    app.run(port=80)
    # app.run(port=80, host="192.168.0.11")
