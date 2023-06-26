# Form implementation generated from reading ui file 'timkiemUi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtWidgets import QMessageBox
from bson.objectid import ObjectId
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import sys


class Ui_timkiem_mainwindows(object):
    mongo_url="mongodb://localhost:27017"
    #mongo_url = "mongodb+srv://test1:test1@cluster0.73t2bch.mongodb.net/?retryWrites=true&w=majority"
    database_name = "MAC"
    def setupUi(self, timkiem_mainwindows):
        timkiem_mainwindows.setObjectName("timkiem_mainwindows")
        timkiem_mainwindows.resize(1113, 730)
        self.centralwidget = QtWidgets.QWidget(parent=timkiem_mainwindows)
        self.centralwidget.setObjectName("centralwidget")
        self.search_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(350, 10, 321, 31))
        self.search_text.setObjectName("search_text")
        self.bt_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_search.setGeometry(QtCore.QRect(100, 10, 101, 31))
        self.bt_search.setObjectName("bt_search")
        self.table_data_view = QtWidgets.QTableView(parent=self.centralwidget)
        self.table_data_view.setGeometry(QtCore.QRect(20, 50, 1081, 471))
        self.table_data_view.setObjectName("table_data_view")
        self.bt_del = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_del.setGeometry(QtCore.QRect(520, 550, 75, 41))
        self.bt_del.setObjectName("bt_del")
        self.bt_insert_new = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_insert_new.setGeometry(QtCore.QRect(240, 550, 75, 41))
        self.bt_insert_new.setObjectName("bt_insert_new")
        self.select_search = QtWidgets.QComboBox(parent=self.centralwidget)
        self.select_search.setGeometry(QtCore.QRect(220, 10, 111, 31))
        self.select_search.setObjectName("select_search")
        self.select_search.addItem("")
        self.select_search.addItem("")
        self.select_search.addItem("")
        self.bt_edit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_edit.setGeometry(QtCore.QRect(360, 550, 75, 41))
        self.bt_edit.setObjectName("bt_edit")
        self.bt_insert_rc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_insert_rc.setGeometry(QtCore.QRect(30, 550, 121, 41))
        self.bt_insert_rc.setObjectName("bt_insert_rc")
        self.bt_print = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_print.setGeometry(QtCore.QRect(670, 550, 75, 41))
        self.bt_print.setObjectName("bt_print")
        timkiem_mainwindows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=timkiem_mainwindows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 21))
        self.menubar.setObjectName("menubar")
        timkiem_mainwindows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=timkiem_mainwindows)
        self.statusbar.setObjectName("statusbar")
        timkiem_mainwindows.setStatusBar(self.statusbar)

        self.retranslateUi(timkiem_mainwindows)
        QtCore.QMetaObject.connectSlotsByName(timkiem_mainwindows)
        
        self.bt_insert_new.setObjectName("bt_insert_new")
        self.bt_insert_new.clicked.connect(self.open_mac_form)  # Gắn kết sự kiện click cho button bt_insert_new
        self.bt_insert_rc.setObjectName("bt_insert_rc")
        self.bt_insert_rc.clicked.connect(self.open_mac_form_rc)
        self.bt_search.setObjectName("bt_search")
        self.bt_search.clicked.connect(self.search_data)
        self.bt_edit.clicked.connect(self.edit)
        self.bt_del.clicked.connect(self.delete)
        self.bt_print.clicked.connect(self.fill_datas)
        self.load_data()
    def retranslateUi(self, timkiem_mainwindows):
        _translate = QtCore.QCoreApplication.translate
        timkiem_mainwindows.setWindowTitle(_translate("timkiem_mainwindows", "MainWindow"))
        self.bt_search.setText(_translate("timkiem_mainwindows", "SEARCH"))
        self.bt_del.setText(_translate("timkiem_mainwindows", "DELETE"))
        self.bt_insert_new.setText(_translate("timkiem_mainwindows", "INSERT NEW"))
        self.select_search.setItemText(0, _translate("timkiem_mainwindows", "select"))
        self.select_search.setItemText(1, _translate("timkiem_mainwindows", "Fullname"))
        self.select_search.setItemText(2, _translate("timkiem_mainwindows", "Phone"))
        self.bt_edit.setText(_translate("timkiem_mainwindows", "EDIT"))
        self.bt_insert_rc.setText(_translate("timkiem_mainwindows", "INSERT RECEIVER"))
        self.bt_print.setText(_translate("timkiem_mainwindows", "FORM"))

    def connect_to_mongodb(self, mongo_url, database_name):
        try:
            client = MongoClient(mongo_url)
            db = client[database_name]
            return client, db
        except:
            return None, None
    def search_data(self):
        # Kết nối tới MongoDB
        client, db = self.connect_to_mongodb(self.mongo_url, self.database_name)
        
        if client is not None and db is not None:
            # Lấy collection "Sender"
            sender_collection = db["Sender"]
            
            # Lấy collection "Receiver"
            receiver_collection = db["Receiver"]

            Shipping_collection= db["ShippingDetail"]
            
                # Lấy giá trị từ ô tìm kiếm
            search_value = self.search_text.text()
            
            # Lấy giá trị từ combobox
            search_type = self.select_search.currentText()
            
            # Tạo điều kiện tìm kiếm
            search_condition = {}
            
            if search_type == "Fullname":
                search_condition["$or"] = [
                    {"Fullname_sender": search_value},
                    
                ]
            elif search_type == "Phone":
                search_condition["$or"] = [
                    {"Phone_sender": search_value},
                   
                ]
            
            # Tìm kiếm trong collection "Sender"
            sender_data = list(sender_collection.find(search_condition))
            
            # Tìm kiếm trong collection "Receiver"
            receiver_data = list(receiver_collection.find())
            
            shipping_data=list(Shipping_collection.find())
            
            
            # Hiển thị thông tin trên table_data_view
            self.display_data(sender_data,receiver_data,shipping_data)
            
            # Đóng kết nối
            client.close()
    def display_data(self,sd,rc,shipping):
        # Xóa dữ liệu cũ trên table_data_view
        self.clear_table_data()
        
        # Tạo model cho table_data_view
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Fullname_sender", "Phone_sender", "Address_sender", "Fullname_receiver", "Phone_receiver", "Address_receiver",
                                         "tracking_number","weight","declared", "total_charge",
                                         "date", "number_of_pieces", "commodity_description",
                                        "quantity", "value", "Sender_id", "Receiver_id"])
        for item_sd in sd:
            for item_rc in rc:
                if item_sd['_id'] == item_rc['Sender_id']:
                    for item_ship in shipping:
                        if item_rc['_id']==item_ship['Receiver_id']:
                            row = [
                                    QtGui.QStandardItem(str(item_sd.get("Fullname_sender"))),
                                    QtGui.QStandardItem(str(item_sd.get("Phone_sender"))),
                                    QtGui.QStandardItem(str(item_sd.get("Address_sender"))),
                                    QtGui.QStandardItem(str(item_rc.get("Fullname_receiver"))),
                                    QtGui.QStandardItem(str(item_rc.get("Phone_receiver"))),
                                    QtGui.QStandardItem(str(item_rc.get("Address_receiver"))),
                                    QtGui.QStandardItem(str(item_ship.get("tracking_number"))),
                                    QtGui.QStandardItem(str(item_ship.get("weight"))),
                                    QtGui.QStandardItem(str(item_ship.get("declared"))),
                                    QtGui.QStandardItem(str(item_ship.get("total_charge"))),
                                    QtGui.QStandardItem(str(item_ship.get("date"))),
                                    QtGui.QStandardItem(str(item_ship.get("number_of_pieces"))),
                                    QtGui.QStandardItem(str(item_ship.get("commodity_description"))),
                                    QtGui.QStandardItem(str(item_ship.get("quantity"))),
                                    QtGui.QStandardItem(str(item_ship.get("value"))),
                                    QtGui.QStandardItem(str(item_ship.get("Sender_id"))),
                                    QtGui.QStandardItem(str(item_ship.get("Receiver_id")))
                                    ]
                            model.appendRow(row)
        self.table_data_view.setModel(model)
    def clear_table_data(self):
        model = QtGui.QStandardItemModel()
        self.table_data_view.setModel(model)
    def open_mac_form_rc(self):
            # Get data from the selected row in the table view
            # Fill out the data in the Mac form
            from mac import Ui_Mac_mainwindown
            self.mac_form = QtWidgets.QMainWindow()
            self.uis = Ui_Mac_mainwindown()
            self.uis.setupUi(self.mac_form)
            fullname, phone, address = self.get_data_from_tableview()
            id_sender=self.search()
            self.uis.fill_data(fullname, phone, address)
            self.uis.get_id(id_sender)
            self.mac_form.show()
    def fill_datas(self):
        from mac import Ui_Mac_mainwindown
        self.mac_form = QtWidgets.QMainWindow()
        self.uis = Ui_Mac_mainwindown()
        self.uis.setupUi(self.mac_form)
        fullname, phone, address,fullname_r,phone_r,address_r = self.get_data_from_tableview_all()
        id_sender=self.search()
        self.uis.fill_data_test(fullname, phone, address,fullname_r,phone_r,address_r)
        self.uis.get_id(id_sender)
        self.mac_form.show()
    def open_mac_form(self):
        # Get data from the selected row in the table view
            # Fill out the data in the Mac form
            from mac import Ui_Mac_mainwindown
            self.mac_form = QtWidgets.QMainWindow()
            self.uis = Ui_Mac_mainwindown()
            self.uis.setupUi(self.mac_form)
            self.mac_form.show()        
    def load_data(self):
        client, db = self.connect_to_mongodb(self.mongo_url, self.database_name)
        

        # Lấy dữ liệu từ collection Sender
        sender_collection = db["Sender"]
        sender_data = list(sender_collection.find())

        # Lấy dữ liệu từ collection Receiver
        receiver_collection = db["Receiver"]
        receiver_data = list(receiver_collection.find())
        shipping_collection = db["ShippingDetail"]
        shipping_data = list(shipping_collection.find())
        

        # Tạo model và thiết lập dữ liệu cho QTableView
        num_columns = 15
        model = QStandardItemModel(0, num_columns)
        header_labels = [
            "Fullname_sender", "Phone_sender", "Address_sender",
            "Fullname_receiver", "Phone_receiver", "Address_receiver",
            "tracking_number","weight",
            "declared", "total_charge",
            "date", "number_of_pieces", "commodity_description",
            "quantity", "value", "Sender_id", "Receiver_id"
        ]
        model.setHorizontalHeaderLabels(header_labels)
        for item_sd, item_rc, item_ship in zip(sender_data, receiver_data, shipping_data):
            row = [
            QtGui.QStandardItem(str(item_sd.get("Fullname_sender"))),
            QtGui.QStandardItem(str(item_sd.get("Phone_sender"))),
            QtGui.QStandardItem(str(item_sd.get("Address_sender"))),
            QtGui.QStandardItem(str(item_rc.get("Fullname_receiver"))),
            QtGui.QStandardItem(str(item_rc.get("Phone_receiver"))),
            QtGui.QStandardItem(str(item_rc.get("Address_receiver"))),
            QtGui.QStandardItem(str(item_ship.get("tracking_number"))),
            QtGui.QStandardItem(str(item_ship.get("weight"))),
            QtGui.QStandardItem(str(item_ship.get("declared"))),
            QtGui.QStandardItem(str(item_ship.get("total_charge"))),
            QtGui.QStandardItem(str(item_ship.get("date"))),
            QtGui.QStandardItem(str(item_ship.get("number_of_pieces"))),
            QtGui.QStandardItem(str(item_ship.get("commodity_description"))),
            QtGui.QStandardItem(str(item_ship.get("quantity"))),
            QtGui.QStandardItem(str(item_ship.get("value"))),
            QtGui.QStandardItem(str(item_ship.get("Sender_id"))),
            QtGui.QStandardItem(str(item_ship.get("Receiver_id")))
            ]
            model.appendRow(row)
        self.table_data_view.setModel(model)
       
        """for item in combined_data:
            sender_id = item.get("Sender_id")
            receiver_id = item.get("Receiver_id")
            for sender_item in sender_data:
                if sender_item["_id"] == sender_id:
                    for receiver_item in receiver_data:
                        if receiver_item["_id"] == receiver_id:
                            row = [
                                QtGui.QStandardItem(str(sender_item.get("Fullname_sender"))),
                                QtGui.QStandardItem(str(sender_item.get("Phone_sender"))),
                                QtGui.QStandardItem(str(sender_item.get("Address_sender"))),
                                QtGui.QStandardItem(str(receiver_item.get("Fullname_receiver"))),
                                QtGui.QStandardItem(str(receiver_item.get("Phone_receiver"))),
                                QtGui.QStandardItem(str(receiver_item.get("Address_receiver"))),
                                QtGui.QStandardItem(str(item.get("tracking_number"))),
                                QtGui.QStandardItem(str(item.get("service_type"))),
                                QtGui.QStandardItem(str(item.get("delivery_option"))),
                                QtGui.QStandardItem(str(item.get("cargo_type"))),
                                QtGui.QStandardItem(str(item.get("dimension"))),
                                QtGui.QStandardItem(str(item.get("weight"))),
                                QtGui.QStandardItem(str(item.get("chargeable_weight"))),
                                QtGui.QStandardItem(str(item.get("declared"))),
                                QtGui.QStandardItem(str(item.get("other_charges"))),
                                QtGui.QStandardItem(str(item.get("total_charge"))),
                                QtGui.QStandardItem(str(item.get("payment_method"))),
                                QtGui.QStandardItem(str(item.get("date"))),
                                QtGui.QStandardItem(str(item.get("number_of_pieces"))),
                                QtGui.QStandardItem(str(item.get("commodity_description"))),
                                QtGui.QStandardItem(str(item.get("quantity"))),
                                QtGui.QStandardItem(str(item.get("value"))),
                                QtGui.QStandardItem(str(sender_id)),
                                QtGui.QStandardItem(str(receiver_id))
                            ]
                            model.appendRow(row)"""
    def edit(self):
        # Lấy dữ liệu từ QTableView
        selected_row = self.table_data_view.currentIndex().row()
        if selected_row >= 0:
            # Lấy dữ liệu từ các ô trong hàng đã chọn
            fullname_sender = self.table_data_view.model().index(selected_row, 0).data()
            phone_sender = self.table_data_view.model().index(selected_row, 1).data()
            address_sender = self.table_data_view.model().index(selected_row, 2).data()
            fullname_receiver = self.table_data_view.model().index(selected_row, 3).data()
            phone_receiver = self.table_data_view.model().index(selected_row, 4).data()
            address_receiver = self.table_data_view.model().index(selected_row, 5).data()
            tracking_number = self.table_data_view.model().index(selected_row, 6).data()
            weight = self.table_data_view.model().index(selected_row, 7).data()
            declared = self.table_data_view.model().index(selected_row, 8).data()
            total_charge = self.table_data_view.model().index(selected_row, 9).data()
            date = self.table_data_view.model().index(selected_row, 10).data()
            number_of_pieces = self.table_data_view.model().index(selected_row, 11).data()
            commodity_description = self.table_data_view.model().index(selected_row, 12).data()
            quantity = self.table_data_view.model().index(selected_row, 13).data()
            value = self.table_data_view.model().index(selected_row, 14).data()

            client, db = self.connect_to_mongodb(self.mongo_url, self.database_name)

            # Lấy collection Sender
            sender_collection = db["Sender"]
            record = sender_collection.find_one({"Phone_sender": phone_sender})
            if record:
                sender_id = record["_id"]
                # Tìm và cập nhật dữ liệu trong collection Sender
                sender_collection.update_one(
                    {"_id": sender_id},
                    {"$set": {"Fullname_sender":fullname_sender,"Phone_sender": phone_sender, "Address_sender": address_sender}}
                )

                # Lấy collection Receiver
                receiver_collection = db["Receiver"]

                # Tìm và cập nhật dữ liệu trong collection Receiver
                receiver_collection.update_one(
                    {"Sender_id":sender_id},
                    {"$set": {"Fullname_receiver": fullname_receiver,"Phone_receiver": phone_receiver, "Address_receiver": address_receiver}}
                )
                get_id_receiver=receiver_collection.find_one({"Sender_id":sender_id})
                # Lấy collection ShippingDetail
                shipping_detail_collection = db["ShippingDetail"]
                if get_id_receiver:
                    id_receiver=get_id_receiver["_id"]
                # Tìm và cập nhật dữ liệu trong collection ShippingDetail
                    shipping_detail_collection.update_one(
                        {"Receiver_id":id_receiver},
                        {"$set": {"tracking_number": tracking_number,"weight": weight, "declared": declared, "total_charge": total_charge,
                                "date": date, "number_of_pieces": number_of_pieces,
                                "commodity_description": commodity_description, "quantity": quantity, "value": value}}
                    )

            # Cập nhật lại dữ liệu trong QTableView
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 0), fullname_sender)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 1), phone_sender)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 2), address_sender)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 3), fullname_receiver)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 4), phone_receiver)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 5), address_receiver)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 6), tracking_number)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 7), weight)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 8), declared)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 9), total_charge)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 10), date)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 11), number_of_pieces)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 12), commodity_description)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 13), quantity)
            self.table_data_view.model().setData(self.table_data_view.model().index(selected_row, 14), value)

            # Hiển thị thông báo edit thành công
            QMessageBox.information(self.table_data_view, "Success", "Edit successful!")
 
    def search(self):
        client, db = self.connect_to_mongodb(self.mongo_url, self.database_name)
        sender_collection = db["Sender"]
        sender_data = list(sender_collection.find())
        phone=self.get_data_from_tableview()
        
        for item in sender_data:
            if phone[1]==item['Phone_sender']:
                 return item['_id']
    def get_data_from_tableview(self):
        # Get the index of the selected row in QTableView
        selected_row = self.table_data_view.currentIndex().row()

        # Check if the selected row is valid
        if selected_row >= 0:
            # Get the data model from QTableView
            model = self.table_data_view.model()

            # Get the data from the columns in the selected row
            fullname_index = model.index(selected_row, 0)
            phone_index = model.index(selected_row, 1)
            address_index = model.index(selected_row, 2)

            # Get the values from the cells in the selected row
            fullname = model.data(fullname_index)
            phone = model.data(phone_index)
            address = model.data(address_index)
            return fullname, phone, address
    def get_data_from_tableview_all(self):
        # Get the index of the selected row in QTableView
        selected_row = self.table_data_view.currentIndex().row()

        # Check if the selected row is valid
        if selected_row >= 0:
            # Get the data model from QTableView
            model = self.table_data_view.model()

            # Get the data from the columns in the selected row
            fullname_index_sd = model.index(selected_row, 0)
            phone_index_sd = model.index(selected_row, 1)
            address_index_sd = model.index(selected_row, 2)
            fullname_index_rc = model.index(selected_row, 3)
            phone_index_rc = model.index(selected_row, 4)
            address_index_rc = model.index(selected_row, 5)
            

            # Get the values from the cells in the selected row
            fullname_sd = model.data(fullname_index_sd)
            phone_sd = model.data(phone_index_sd)
            address_sd = model.data(address_index_sd)
            fullname_rc = model.data(fullname_index_rc)
            phone_rc = model.data(phone_index_rc)
            address_rc = model.data(address_index_rc)
            

            return (
                fullname_sd,
                phone_sd,
                address_sd,
                fullname_rc,
                phone_rc,
                address_rc,
            )
    def get_data_from_tableview_alls(self):
              
        selected_row = self.table_data_view.currentIndex().row()

        # Check if the selected row is valid
        if selected_row >= 0:
            # Get the data model from QTableView
            model = self.table_data_view.model()

            # Define the column indices
            column_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

            # Get the values from the cells in the selected row
            data = [model.data(model.index(selected_row, column)) for column in column_indices]

            # Return the data as a tuple
            return tuple(data)

        # Return None if no row is selected or the selected row is invalid
        return None
    """def run_sheet(self):
       
        credentials_file = "data/key_api.json"
        
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        gc = gspread.authorize(credentials)

        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1yraAQblwXdBV0zULq4AbQ95u5Nl_O9M8qYDjGZQr2bU/edit#gid=1349128033')

        data = self.get_data_from_tableview_alls()

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
            QMessageBox.information(None, "NO!", "NO DATA")"""

    def delete(self):
        # Lấy dữ liệu từ QTableView
        selected_row = self.table_data_view.currentIndex().row()
        if selected_row >= 0:
            # Lấy dữ liệu từ các ô trong hàng đã chọn
            #fullname_sender = self.table_data_view.model().index(selected_row, 0).data()
            phone_sender=self.table_data_view.model().index(selected_row, 1).data()
            # Xác nhận xóa bản ghi
            confirmation = QMessageBox.question(self.table_data_view, "Delete", "Are you sure you want to delete this record?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmation == QMessageBox.StandardButton.Yes:
                
                client = MongoClient(self.mongo_url)
                db = client[self.database_name]

                # Lấy collection Sender
                sender_collection = db["Sender"]
                record = sender_collection.find_one({"Phone_sender": phone_sender})
                if record:
                    # Lấy ID của bản ghi Sender
                    sender_id = record["_id"]
                    
                    # Xóa bản ghi trong Sender
                    sender_collection.delete_one({"_id": sender_id})
                    
                    # Xóa bản ghi trong Receiver
                    db["Receiver"].delete_many({"Sender_id": sender_id})
                    
                    # Xóa bản ghi trong ShippingDetail
                    db["ShippingDetail"].delete_many({"Sender_id": sender_id})

                    # Xóa dữ liệu trong QTableView
                    self.table_data_view.model().removeRow(selected_row)

                    # Hiển thị thông báo delete thành công
                    QMessageBox.information(self.table_data_view, "Success", "Delete successful!")
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    timkiem_mainwindows = QtWidgets.QMainWindow()
    ui = Ui_timkiem_mainwindows()
    ui.setupUi(timkiem_mainwindows)
    timkiem_mainwindows.show()
    sys.exit(app.exec())
