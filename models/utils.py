import numpy as np
import pickle
import json
import config


class ItemOutletSales():
    def __init__(self,Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Outlet_Type, Item_Type, Outlet_Identifier):
    
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = Outlet_Type
        self.Item_Type = "Item_Type_" + Item_Type
        self.Outlet_Identifier = "Outlet_Identifier_" + Outlet_Identifier

    def load_model(self):
        with open(config.PROJECT_MODEL_PATH, "rb") as f:
        # with open(r"C:\Users\abhij\OneDrive\Desktop\DATA SCIENCTIST\Visual Studio code\Web Framework\Sales_data\models\project_model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_DATA_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_outlet_sales(self):

        self.load_model()

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.Item_Weight
        array[1] = self.json_data["Item_Fat_Content"][self.Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.Item_MRP
        array[4] = self.Outlet_Establishment_Year
        array[5] = self.json_data["Outlet_Size"][self.Outlet_Size]
        array[6] = self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        array[7] = self.json_data["Outlet_Type"][self.Outlet_Type]

        Item_Type_index = self.json_data["columns"].index(self.Item_Type)
        array[Item_Type_index] = 1
        
        Outlet_Identifier_index = self.json_data["columns"].index(self.Outlet_Identifier)
        array[Outlet_Identifier_index] = 1

        result = self.model.predict([array])[0]
        return round(result,2)


if __name__ == "__main__":
    print("SUCCESS")

    Item_Weight = 9.3
    Item_Fat_Content = "Low Fat"
    Item_Visibility = 0.016047301
    Item_MRP = 249.8092
    Outlet_Establishment_Year = 1999
    Outlet_Size = "Medium"
    Outlet_Location_Type = "Tier 1"
    Outlet_Type = "Supermarket Type1"
    Item_Type = "Baking Goods"
    Outlet_Identifier = "OUT049"

    Obj = ItemOutletSales(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Outlet_Type, Item_Type, Outlet_Identifier)
    result = Obj.get_outlet_sales()
    print(f"Item Outlet Sales is {result}")
        




