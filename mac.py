# Form implementation generated from reading ui file 'mac.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from api_mac import insert_sender,insert_receiver,insert_shipping_detail,run_sheet_api,generate_tracking_number
from PyQt6.QtWidgets import  QMessageBox


class Ui_Mac_mainwindown(object):
    list_data=[]
    def setupUi(self, Mac_mainwindown):
        Mac_mainwindown.setObjectName("Mac_mainwindown")
        Mac_mainwindown.resize(1127, 905)
        self.centralwidget = QtWidgets.QWidget(parent=Mac_mainwindown)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 471, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.fullname_lb_sender = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.fullname_lb_sender.setObjectName("fullname_lb_sender")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fullname_lb_sender)
        self.fullname_text_sender = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.fullname_text_sender.setObjectName("fullname_text_sender")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fullname_text_sender)
        self.phone_lb_sender = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.phone_lb_sender.setObjectName("phone_lb_sender")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.phone_lb_sender)
        self.phone_text_sender = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.phone_text_sender.setObjectName("phone_text_sender")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phone_text_sender)
        self.address_lb_sender = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.address_lb_sender.setObjectName("address_lb_sender")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.address_lb_sender)
        self.address_text_sender = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.address_text_sender.setObjectName("address_text_sender")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.address_text_sender)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(570, 70, 471, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.fullname_lb_receiver = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.fullname_lb_receiver.setObjectName("fullname_lb_receiver")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fullname_lb_receiver)
        self.fullname_text_receiver = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.fullname_text_receiver.setObjectName("fullname_text_receiver")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fullname_text_receiver)
        self.phone_lb_receiver = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.phone_lb_receiver.setObjectName("phone_lb_receiver")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.phone_lb_receiver)
        self.phone_text_receiver = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.phone_text_receiver.setObjectName("phone_text_receiver")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phone_text_receiver)
        self.address_lb_receiver = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.address_lb_receiver.setObjectName("address_lb_receiver")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.address_lb_receiver)
        self.address_text_receiver = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.address_text_receiver.setObjectName("address_text_receiver")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.address_text_receiver)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 280, 471, 381))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.tracking_number_lb = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.tracking_number_lb.setObjectName("tracking_number_lb")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.tracking_number_lb)
        self.tracking_number_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.tracking_number_text.setObjectName("tracking_number_text")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tracking_number_text)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.cbox_service = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.cbox_service.setObjectName("cbox_service")
        self.cbox_service.addItem("")
        self.cbox_service.addItem("")
        self.cbox_service.addItem("")
        self.cbox_service.addItem("")
        self.cbox_service.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbox_service)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.cbox_delivery = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.cbox_delivery.setObjectName("cbox_delivery")
        self.cbox_delivery.addItem("")
        self.cbox_delivery.addItem("")
        self.cbox_delivery.addItem("")
        self.cbox_delivery.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbox_delivery)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.cbox_cargo = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.cbox_cargo.setObjectName("cbox_cargo")
        self.cbox_cargo.addItem("")
        self.cbox_cargo.addItem("")
        self.cbox_cargo.addItem("")
        self.cbox_cargo.addItem("")
        self.cbox_cargo.addItem("")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbox_cargo)
        self.pieces_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.pieces_text.setObjectName("pieces_text")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pieces_text)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.dimention_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.dimention_text.setObjectName("dimention_text")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dimention_text)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.weight_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.weight_text.setObjectName("weight_text")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.weight_text)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.charge_weight_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.charge_weight_text.setObjectName("charge_weight_text")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.charge_weight_text)
        self.label_11 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.declar_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.declar_text.setObjectName("declar_text")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.declar_text)
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.othe_decla_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.othe_decla_text.setObjectName("othe_decla_text")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.othe_decla_text)
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.total_charge_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        self.total_charge_text.setObjectName("total_charge_text")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.total_charge_text)
        self.label_15 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.cbox_pay = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.cbox_pay.setObjectName("cbox_pay")
        self.cbox_pay.addItem("")
        self.cbox_pay.addItem("")
        self.cbox_pay.addItem("")
        self.cbox_pay.addItem("")
        self.cbox_pay.addItem("")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbox_pay)
        self.label_16 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.date_time = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.date_time.setDate(QtCore.QDate(2023, 6, 19))
        self.date_time.setObjectName("date_time")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.date_time)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 220, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.bt_cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_cancel.setGeometry(QtCore.QRect(90, 700, 75, 23))
        self.bt_cancel.setObjectName("bt_cancel")
        self.bt_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_submit.setGeometry(QtCore.QRect(310, 700, 75, 23))
        self.bt_submit.setObjectName("bt_submit")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(560, 280, 561, 201))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.value_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.value_text.setObjectName("value_text")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.value_text)
        self.quantity_text = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.quantity_text.setObjectName("quantity_text")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.quantity_text)
        self.commodity_textplain = QtWidgets.QPlainTextEdit(parent=self.formLayoutWidget_4)
        self.commodity_textplain.setObjectName("commodity_textplain")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.commodity_textplain)
        self.bt_print = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_print.setGeometry(QtCore.QRect(500, 700, 75, 23))
        self.bt_print.setObjectName("bt_print")
        self.bt_add_new_rc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_add_new_rc.setGeometry(QtCore.QRect(570, 170, 75, 41))
        self.bt_add_new_rc.setObjectName("bt_add_new_rc")
        self.bt_add_shipping = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_add_shipping.setGeometry(QtCore.QRect(670, 700, 81, 31))
        self.bt_add_shipping.setObjectName("bt_add_shipping")
        Mac_mainwindown.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Mac_mainwindown)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName("menubar")
        Mac_mainwindown.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Mac_mainwindown)
        self.statusbar.setObjectName("statusbar")
        Mac_mainwindown.setStatusBar(self.statusbar)

        self.retranslateUi(Mac_mainwindown)
        QtCore.QMetaObject.connectSlotsByName(Mac_mainwindown)


        # button click
        self.bt_submit.clicked.connect(self.submit_data)
        self.bt_add_new_rc.clicked.connect(self.test)
        self.bt_print.clicked.connect(self.print)
        self.bt_cancel.clicked.connect(self.handle_close)
        self.bt_add_shipping.clicked.connect(self.add_shipping)
    def retranslateUi(self, Mac_mainwindown):
        _translate = QtCore.QCoreApplication.translate
        Mac_mainwindown.setWindowTitle(_translate("Mac_mainwindown", "MainWindow"))
        self.fullname_lb_sender.setText(_translate("Mac_mainwindown", "Full Name:"))
        self.phone_lb_sender.setText(_translate("Mac_mainwindown", "Phone:"))
        self.address_lb_sender.setText(_translate("Mac_mainwindown", "Address:"))
        self.label.setText(_translate("Mac_mainwindown", "Sender"))
        self.fullname_lb_receiver.setText(_translate("Mac_mainwindown", "Full Name:"))
        self.phone_lb_receiver.setText(_translate("Mac_mainwindown", "Phone:"))
        self.address_lb_receiver.setText(_translate("Mac_mainwindown", "Address:"))
        self.label_2.setText(_translate("Mac_mainwindown", "Receiver"))
        self.label_3.setText(_translate("Mac_mainwindown", "Shipping Information"))
        self.tracking_number_lb.setText(_translate("Mac_mainwindown", "TRACKING NUMBER:"))
        self.label_4.setText(_translate("Mac_mainwindown", "SERVICE TYPRE:"))
        self.cbox_service.setItemText(0, _translate("Mac_mainwindown", "Select"))
        self.cbox_service.setItemText(1, _translate("Mac_mainwindown", "AIRPORT"))
        self.cbox_service.setItemText(2, _translate("Mac_mainwindown", "DOOR"))
        self.cbox_service.setItemText(3, _translate("Mac_mainwindown", "STATION"))
        self.cbox_service.setItemText(4, _translate("Mac_mainwindown", "DOOR/Excl. Duty"))
        self.label_5.setText(_translate("Mac_mainwindown", "DELIVERY OPTION:"))
        self.cbox_delivery.setItemText(0, _translate("Mac_mainwindown", "Select"))
        self.cbox_delivery.setItemText(1, _translate("Mac_mainwindown", "PRIORITY"))
        self.cbox_delivery.setItemText(2, _translate("Mac_mainwindown", "EXPEDITE"))
        self.cbox_delivery.setItemText(3, _translate("Mac_mainwindown", "SAVER"))
        self.label_6.setText(_translate("Mac_mainwindown", "CARGO TYPE:"))
        self.cbox_cargo.setItemText(0, _translate("Mac_mainwindown", "Select"))
        self.cbox_cargo.setItemText(1, _translate("Mac_mainwindown", "GIFT"))
        self.cbox_cargo.setItemText(2, _translate("Mac_mainwindown", "DOCUMENTS"))
        self.cbox_cargo.setItemText(3, _translate("Mac_mainwindown", "COMMERCIAL SAMPLE"))
        self.cbox_cargo.setItemText(4, _translate("Mac_mainwindown", "RETURNED GOOD"))
        self.label_8.setText(_translate("Mac_mainwindown", "DIMENTION:"))
        self.label_9.setText(_translate("Mac_mainwindown", "WEIGHT:"))
        self.label_10.setText(_translate("Mac_mainwindown", "CHARGEABLE WEIGHT:"))
        self.label_11.setText(_translate("Mac_mainwindown", "DECLARARED:"))
        self.label_12.setText(_translate("Mac_mainwindown", "OTHER CHARGES:"))
        self.label_13.setText(_translate("Mac_mainwindown", "TOTAL CHARGE:"))
        self.label_15.setText(_translate("Mac_mainwindown", "PAYMENT METHOD"))
        self.cbox_pay.setItemText(0, _translate("Mac_mainwindown", "select"))
        self.cbox_pay.setItemText(1, _translate("Mac_mainwindown", "CASH"))
        self.cbox_pay.setItemText(2, _translate("Mac_mainwindown", "CHECK"))
        self.cbox_pay.setItemText(3, _translate("Mac_mainwindown", "UNPAID"))
        self.cbox_pay.setItemText(4, _translate("Mac_mainwindown", "OTHER"))
        self.label_16.setText(_translate("Mac_mainwindown", "DATE:"))
        self.date_time.setDisplayFormat(_translate("Mac_mainwindown", "MM-dd-yyyy"))
        self.label_7.setText(_translate("Mac_mainwindown", "NUMBER OF PIECES:"))
        self.label_14.setText(_translate("Mac_mainwindown", "Details"))
        self.bt_cancel.setText(_translate("Mac_mainwindown", "Cancel"))
        self.bt_submit.setText(_translate("Mac_mainwindown", "Submit"))
        self.label_17.setText(_translate("Mac_mainwindown", "COMMODITY DESCRIPTION (CHI TIẾT HÀNG GỞI):"))
        self.label_18.setText(_translate("Mac_mainwindown", "QUANTITY:"))
        self.label_19.setText(_translate("Mac_mainwindown", "VALUE:"))
        self.bt_print.setText(_translate("Mac_mainwindown", "Print"))
        self.bt_add_new_rc.setText(_translate("Mac_mainwindown", "Add New"))
        self.bt_add_shipping.setText(_translate("Mac_mainwindown", "Add shipping"))

    def submit_data(self):
        
        fullname_sd = self.fullname_text_sender.text()
        phone_sd = self.phone_text_sender.text()  # Example phone number
        address_sd = self.address_text_sender.text()  # Example address
        fullname_rc = self.fullname_text_receiver.text()
        phone_rc = self.phone_text_receiver.text()  # Example phone number
        address_rc = self.address_text_receiver.text()  # Example address
        tracking_number= self.tracking_number_text.text()
        service_type=self.cbox_service.currentText()
        delivery_option=self.cbox_delivery.currentText()
        cargo_type=self.cbox_cargo.currentText()
        dimension=self.dimention_text.text()
        weight= self.weight_text.text()          
        chargeable_weight=self.charge_weight_text.text()
        declared=self.declar_text.text()
        other_charges=self.othe_decla_text.text()
        total_charge=self.total_charge_text.text()
        payment_method=self.cbox_pay.currentText()
        date=self.date_time.date().toString("MM/dd/yyyy")
        number_of_pieces=self.pieces_text.text()
        commodity_description= self.commodity_textplain.toPlainText()
        quantity= self.quantity_text.text()
        value= self.value_text.text()
        
        
        # Call the insert_sender function with the retrieved values
        senderid=insert_sender(fullname_sd, phone_sd, address_sd)
        rec_id=insert_receiver(fullname_rc, phone_rc, address_rc, senderid)
        insert_shipping_detail(tracking_number, service_type, delivery_option, cargo_type, dimension, weight,
                           chargeable_weight, declared, other_charges, total_charge, payment_method, date,
                           number_of_pieces, commodity_description, quantity, value, senderid, rec_id)
        QMessageBox.information(None, "Success", "Data submitted successfully.")
        
    def print(self):
        list_data=[]
        fullname_sd = self.fullname_text_sender.text()
        phone_sd = self.phone_text_sender.text()  # Example phone number
        address_sd = self.address_text_sender.text()  # Example address
        fullname_rc = self.fullname_text_receiver.text()
        phone_rc = self.phone_text_receiver.text()  # Example phone number
        address_rc = self.address_text_receiver.text()  # Example address
        tracking_number= self.tracking_number_text.text()
        weight= self.weight_text.text()          
        total_charge=self.total_charge_text.text()
        date=self.date_time.date().toString("MM/dd/yyyy")
        declared=self.declar_text.text()
        number_of_pieces=self.pieces_text.text()
        commodity_description= self.commodity_textplain.toPlainText()
        
        
        list_data.append(fullname_sd)
        list_data.append(phone_sd)
        list_data.append(address_sd)
        list_data.append(fullname_rc)
        list_data.append(phone_rc)
        list_data.append(address_rc)
        list_data.append(tracking_number)
        list_data.append(weight)
        list_data.append(declared)
        list_data.append(total_charge)
        list_data.append(date)
        list_data.append(number_of_pieces)
        list_data.append(commodity_description)
        tuple_data = tuple(list_data)
        run_sheet_api(tuple_data)
        list_data.clear
        
    def fill_data_one(self):
        tracking_number = generate_tracking_number()  # Gọi hàm generate_tracking_number để lấy tracking number
        self.tracking_number_text.setText(tracking_number)
    def fill_data(self, fullname_sd, phone_sd, address_sd):
        self.fullname_text_sender.setText(fullname_sd)
        self.phone_text_sender.setText(phone_sd)
        self.address_text_sender.setText(address_sd)
        self.fill_data_one()
    def fill_data_test(self, fullname_sd, phone_sd, address_sd,fullname_r,phone_r,address_r):
        self.fullname_text_sender.setText(fullname_sd)
        self.phone_text_sender.setText(phone_sd)
        self.address_text_sender.setText(address_sd)
        self.fullname_text_receiver.setText(fullname_r)
        self.phone_text_receiver.setText(phone_r)
        self.address_text_receiver.setText(address_r)
        self.fill_data_one()
    def test(self):
        fullname_rc = self.fullname_text_receiver.text()
        phone_rc = self.phone_text_receiver.text()  # Example phone number
        address_rc = self.address_text_receiver.text()  # Example address
        tracking_number= self.tracking_number_text.text()
        service_type=self.cbox_service.currentText()
        delivery_option=self.cbox_delivery.currentText()
        cargo_type=self.cbox_cargo.currentText()
        dimension=self.dimention_text.text()
        weight= self.weight_text.text()          
        chargeable_weight=self.charge_weight_text.text()
        declared=self.declar_text.text()
        other_charges=self.othe_decla_text.text()
        total_charge=self.total_charge_text.text()
        payment_method=self.cbox_pay.currentText()
        date=self.date_time.date().toString("MM-dd-yyyy")
        number_of_pieces=self.pieces_text.text()
        commodity_description= self.commodity_textplain.toPlainText()
        quantity= self.quantity_text.text()
        value= self.value_text.text()
        # Call the insert_sender function with the retrieved values
        data=Ui_Mac_mainwindown.list_data[0]
        rec_id=insert_receiver(fullname_rc, phone_rc, address_rc, data)
        insert_shipping_detail(tracking_number, service_type, delivery_option, cargo_type, dimension, weight,
                           chargeable_weight, declared, other_charges, total_charge, payment_method, date,
                           number_of_pieces, commodity_description, quantity, value, data, rec_id)
        Ui_Mac_mainwindown.list_data.clear()
        QMessageBox.information(None, "Success", "Data add new receiver successfully.")
    def add_shipping(self):
       
        tracking_number= self.tracking_number_text.text()
        service_type=self.cbox_service.currentText()
        delivery_option=self.cbox_delivery.currentText()
        cargo_type=self.cbox_cargo.currentText()
        dimension=self.dimention_text.text()
        weight= self.weight_text.text()          
        chargeable_weight=self.charge_weight_text.text()
        declared=self.declar_text.text()
        other_charges=self.othe_decla_text.text()
        total_charge=self.total_charge_text.text()
        payment_method=self.cbox_pay.currentText()
        date=self.date_time.date().toString("MM-dd-yyyy")
        number_of_pieces=self.pieces_text.text()
        commodity_description= self.commodity_textplain.toPlainText()
        quantity= self.quantity_text.text()
        value= self.value_text.text()
        # Call the insert_sender function with the retrieved values
        id_sender=Ui_Mac_mainwindown.list_data[0]
        id_receiver=Ui_Mac_mainwindown.list_data[1]
        
        insert_shipping_detail(tracking_number, service_type, delivery_option, cargo_type, dimension, weight,
                           chargeable_weight, declared, other_charges, total_charge, payment_method, date,
                           number_of_pieces, commodity_description, quantity, value, id_sender, id_receiver)
        Ui_Mac_mainwindown.list_data.clear()
        QMessageBox.information(None, "Success", "Data add new receiver successfully.")
    def get_id(self,id_sender):
        Ui_Mac_mainwindown.list_data.append(id_sender)
    def get_id_rc(self,id_rc):
        Ui_Mac_mainwindown.list_data.append(id_rc)
    def handle_close(self):
        Mac_mainwindown.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mac_mainwindown = QtWidgets.QMainWindow()
    ui = Ui_Mac_mainwindown()
    ui.setupUi(Mac_mainwindown)
    
    Mac_mainwindown.show()
    sys.exit(app.exec())