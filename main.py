from flask import Flask, render_template, jsonify, request
from models.utils import ItemOutletSales


app = Flask(__name__)  # instance

@app.route("/")
def hello_flask():
    print("Welcome to Item Outlet Sales Prediction")
    return render_template("index.html")

@app.route("/ItemOutletSales", methods=["POST"])
def sales_prediction():

    print("We are using POST Method")
        
    # availability = request.form.get("availability")
    # size = request.form.get("size")  
    # total_sqft = float(request.form.get("total_sqft"))
    # bath = int(request.form.get("bath"))
    # balcony = request.form.get("balcony")
    # site_location = request.form.get("site_location")
    # area_type = request.form.get("area_type")

    Item_Weight = float(request.form.get("Item_Weight"))
    Item_Fat_Content = request.form.get("Item_Fat_Content")
    Item_Visibility = float(request.form.get("Item_Visibility"))
    Item_MRP = float(request.form.get("Item_MRP"))
    Outlet_Establishment_Year = int(request.form.get("Outlet_Establishment_Year"))
    Outlet_Size = request.form.get("Outlet_Size")
    Outlet_Location_Type = request.form.get("Outlet_Location_Type")
    Outlet_Type = request.form.get("Outlet_Type")
    Item_Type = request.form.get("Item_Type")
    Outlet_Identifier = request.form.get("Outlet_Identifier")

    Obj = ItemOutletSales(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Outlet_Type, Item_Type, Outlet_Identifier)
    result = Obj.get_outlet_sales()
    print(f"Item Outlet Sales is {result}")
    return render_template("index.html", prediction = result)


if __name__ =="__main__":
    app.run(host = "0.0.0.0", port=3009,debug=True)
