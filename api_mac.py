"""from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_url = "mongodb://localhost:27017"
database_name = "MAC"

# Connect to the MongoDB server
client = MongoClient(mongo_url)

# Access the database
db = client[database_name]
def insert_sender(fullname_sd, phone_sd, address_sd):
    Sender = {
        'Fullname_sender': fullname_sd,
        'Phone_sender': phone_sd,
        'Address_sender': address_sd
    }
    Sender_collection = db['Sender']
    result = Sender_collection.insert_one(Sender)
    return result.inserted_id
def insert_receiver(fullname_rc, phone_rc, address_rc, sender_id):
    Receiver = {
        'Fullname_receiver': fullname_rc,
        'Phone_receiver': phone_rc,
        'Address_receiver': address_rc,
        'Sender_id': sender_id
    }
    Receiver_collection = db['Receiver']
    result = Receiver_collection.insert_one(Receiver)
    return result.inserted_id

def insert_shipping_detail(tracking_number, service_type, delivery_option, cargo_type, dimension, weight,
                           chargeable_weight, declared, other_charges, total_charge, payment_method, date,
                           number_of_pieces, commodity_description, quantity, value, sender_id, receiver_id):
    # Create the ShippingDetail JSON object with Sender_id and Receiver_id
    shipping_detail = {
        'tracking_number': tracking_number,
        'service_type': service_type,
        'delivery_option': delivery_option,
        'cargo_type': cargo_type,
        'dimension': dimension,
        'weight': weight,
        'chargeable_weight': chargeable_weight,
        'declared': declared,
        'other_charges': other_charges,
        'total_charge': total_charge,
        'payment_method': payment_method,
        'date': date,
        'number_of_pieces': number_of_pieces,
        'commodity_description': commodity_description,
        'quantity': quantity,
        'value': value,
        'Sender_id': sender_id,
        'Receiver_id': receiver_id
    }

    # Insert the shipping detail into the collection
    shipping_detail_collection = db['ShippingDetail']
    shipping_detail_collection.insert_one(shipping_detail)


"""

from pymongo import MongoClient
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from PyQt6.QtWidgets import QMessageBox
from bson.objectid import ObjectId
from oauth2client.service_account import ServiceAccountCredentials
#mongo_url = "mongodb+srv://test1:test1@cluster0.73t2bch.mongodb.net/?retryWrites=true&w=majority"
mongo_url="mongodb://localhost:27017"
database_name = "MAC"

# Connect to the MongoDB server
client = MongoClient(mongo_url)

# Access the database
db = client[database_name]

def insert_sender(fullname_sd, phone_sd, address_sd):
    Sender = {
        'Fullname_sender': fullname_sd,
        'Phone_sender': phone_sd,
        'Address_sender': address_sd
    }
    Sender_collection = db['Sender']
    result = Sender_collection.insert_one(Sender)
    return result.inserted_id

def insert_receiver(fullname_rc, phone_rc, address_rc, sender_id):
    Receiver = {
        'Fullname_receiver': fullname_rc,
        'Phone_receiver': phone_rc,
        'Address_receiver': address_rc,
        'Sender_id': sender_id
    }
    Receiver_collection = db['Receiver']
    result = Receiver_collection.insert_one(Receiver)
    return result.inserted_id

def insert_shipping_detail(tracking_number, service_type, delivery_option, cargo_type, dimension, weight,
                           chargeable_weight, declared, other_charges, total_charge, payment_method, date,
                           number_of_pieces, commodity_description, quantity, value, sender_id, receiver_id):
    # Create the ShippingDetail JSON object with Sender_id and Receiver_id
    shipping_detail = {
        'tracking_number': tracking_number,
        'service_type': service_type,
        'delivery_option': delivery_option,
        'cargo_type': cargo_type,
        'dimension': dimension,
        'weight': weight,
        'chargeable_weight': chargeable_weight,
        'declared': declared,
        'other_charges': other_charges,
        'total_charge': total_charge,
        'payment_method': payment_method,
        'date': date,
        'number_of_pieces': number_of_pieces,
        'commodity_description': commodity_description,
        'quantity': quantity,
        'value': value,
        'Sender_id': sender_id,
        'Receiver_id': receiver_id
    }

    # Insert the shipping detail into the collection
    shipping_detail_collection = db['ShippingDetail']
    shipping_detail_collection.insert_one(shipping_detail)

def run_sheet_api(data):
       
        credentials_file = "data/key_api.json"
        
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        gc = gspread.authorize(credentials)

        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1yraAQblwXdBV0zULq4AbQ95u5Nl_O9M8qYDjGZQr2bU/edit#gid=1349128033')


        if data is not None:
            worksheet = sheet.worksheet('SHIPPING FORM')
            ranges = ['D6:G6', 'D8:G8', 'D10:G10', 'D16:G16', 'D18:G18', 
                    'C20:J21', 'N3:Q4', 'Q15:R15', 
                    'Q17','Q21:R21','P25','N13','A30:P30']
            
            for range_, current_data in zip(ranges, data):
                    values = [[current_data]]
                    
                    if ';' in current_data:
                        #num_semicolons = current_data.count(';')
                        split_data = current_data.split(';')
                        num_rows = len(split_data)
                        
                        for i in range(num_rows):
                            row_number = 30 + i
                            range_i = f'A{row_number}:P{row_number}'
                            values = [[split_data[i]]]
                            worksheet.update(range_i, values)
                    else:
                        values = [[current_data]]
                        worksheet.update(range_, values)
                            
                   
            QMessageBox.information(None, "Success", "Insert Sheet successfully.")
        else:
            QMessageBox.information(None, "NO!", "NO DATA")


