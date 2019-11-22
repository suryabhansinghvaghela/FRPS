#!/usr/bin/env python3
import sqlite3
import os.path
import random
import datetime
import csv
import tkinter as tk
import product
from product import Product
from selenium import webdriver
import time
import os


def OrderInvoice(cart, grandTotal):
    tax = grandTotal * 0.06
    orderTotal = grandTotal + tax
    orderDate = datetime.datetime.now()
    orderNum = random.randint(100,1000)
    file = open("orders\order-confirmation_"+str(orderNum)+".csv","w")
    st="orders\order-confirmation_"+str(orderNum)+".csv"
    for Product in cart:
        if Product.getStock() > 0:
            file.write("Item: " + Product.getName() +" Price: Rs."+ str("{:.2f}".format(Product.getPrice()))
                       +" Qty: "+ str(Product.getStock()) + " Sub-Total: Rs." + str("{:.2f}".format(Product.getPrice() * Product.getStock())) + "\n")

    file.write('=' * 20)
    file.write("\nCart Total:"+ str("{:>10}".format("Rs." + str("{:.2f}".format(grandTotal)))))
    file.write("\nTaxes:" + str("{:>15}".format("+Rs." + str("{:.2f}".format(tax)))))
    file.write("\nOrder Total:" + str("{:>9}".format("Rs." + str("{:.2f}".format(orderTotal)))))
    
    file.write("\n")
    file.write('=' * 20)
    file.write("\nOrder Number: " + str(orderNum))
    file.write("\nOrder Date: " + orderDate.strftime('%m-%d-%y'))
    file.close()
    db = sqlite3.connect('database1.db')
    cn = db.cursor()
    cn.execute('update cart set productStock = 0 where productStock > 0')
    db.commit()
    cn.close()
    des=''' '''
    with open(st,'rt')as f:
        data = csv.reader(f)
        for row in data:
            des=des+str(row)
		
    
	
	
    n1=""
    c1=""
    e1=""
    am=int(orderTotal)*100
    a=[]
    db1=sqlite3.connect('user.db')
    cn1=db1.cursor()
    sql1='select name,mob,email from userinfo'
    cn1.execute(sql1)
    a=list(cn1.fetchall())
    print(a[0][0])
    n1=a[0][0]
    c1=a[0][1]
    e1=a[0][2]
    db1.commit()
    cn1.close()
	
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument('--headless')
    options.executable_path="chromedriver.exe"
	
    driver = webdriver.Chrome(chrome_options=options)
    driver.execute_script("window.open('https://rzp_test_uxn2fKkLYq4J29:dLB9zcMUvz6sOp2bErjYEU8C@api.razorpay.com/v1/payments', 'tab2');")
    driver.switch_to.window("tab2")
    driver.execute_script("window.open('https://suryabhansinghvaghela.github.io/', 'tab3');")
    driver.switch_to.window("tab3")
    description=driver.find_element_by_name('description')
    description.send_keys(des) 
    amount=driver.find_element_by_name('amount')
    amount.send_keys(am) 
    name=driver.find_element_by_name('customer[name]')
    name.send_keys(n1) 
    email=driver.find_element_by_name('customer[email]')
    email.send_keys(e1)  
    contact=driver.find_element_by_name('customer[contact]')
    contact.send_keys(c1)  
    contact.send_keys(u'\ue007')
	
    
    return str(orderNum)
    
    
    
def createInventory():
    if os.path.isdir('orders'):
        print()
    else:
        path = 'orders'
        os.mkdir(path)
    
    if not os.path.isfile('database1.db'):
        return False
    elif os.path.isfile('database1.db'):
        db = sqlite3.connect('database1.db')
        cn = db.cursor()
        try:
            cn.execute('create table inventory as select * from products')
        except sqlite3.OperationalError:
            db.commit()
            cn.close()
            return
        cn.execute('update inventory set productPrice = round(productPrice,2)')
        cn.execute('create table cart as select * from inventory')
        cn.execute('update cart set productStock = 0')
        db.commit()
        cn.close()
    
    
        
def getInventorySize():
    db = sqlite3.connect('database1.db')
    inventSize = db.execute('select count(*) from inventory')
    rowcount = inventSize.fetchall()[0][0]
    return rowcount

def createProduct(index,table):
        db = sqlite3.connect('database1.db')
        cn = db.cursor()
        cn.execute('select ind from '+table+' where ind=' +str(index))
        productInd = cn.fetchone()[0]
        cn.execute('select productName from '+table+' where ind=' +str(index))
        productName = cn.fetchone()[0]
        cn.execute('select productPrice from '+table+' where ind=' +str(index))
        productPrice = cn.fetchone()[0]
        cn.execute('select productStock from '+table+' where ind=' +str(index))
        productStock = cn.fetchone()[0]
        newProd = Product(productInd,productName,productPrice,productStock)
        cn.close()
        return newProd
    
def changeStock(ind):
    db = sqlite3.connect('database1.db')
    cn = db.cursor()
    cn.execute('select productStock from inventory where ind=' +str(ind))
    if cn.fetchone()[0] == 0:
        return False
    else:
        cn.execute('select productStock from inventory where ind=' +str(ind))
        newStock = cn.fetchone()[0] - 1
        cn.execute('update inventory set productStock=' + str(newStock) + ' where ind=' + str(ind))
        db.commit()
        cn.close()
        db = sqlite3.connect('database1.db')
        cn = db.cursor()
        cn.execute('select productStock from cart where ind=' +str(ind))
        newCartStock = cn.fetchone()[0] + 1
        cn.execute('update cart set productStock=' + str(newCartStock) + ' where ind=' + str(ind))
        db.commit()
        db.close()
        return True

def returnStock(ind):
    db = sqlite3.connect('database1.db')
    cn = db.cursor()
    cn.execute('select productStock from cart where ind=' +str(ind))
    if cn.fetchone()[0] == 0:
        return False
    else:
        cn.execute('select productStock from cart where ind=' +str(ind))
        newStock = cn.fetchone()[0] - 1
        cn.execute('update cart set productStock=' + str(newStock) + ' where ind=' + str(ind))
        db.commit()
        cn.close()
        db = sqlite3.connect('database1.db')
        cn = db.cursor()
        cn.execute('select productStock from inventory where ind=' +str(ind))
        newCartStock = cn.fetchone()[0] + 1
        cn.execute('update inventory set productStock=' + str(newCartStock) + ' where ind=' + str(ind))
        db.commit()
        db.close()
        return True

def getProductName(ind):
    db = sqlite3.connect('database1.db')
    cn = db.cursor()
    cn.execute('select productName from inventory where ind=' + str(ind))
    name = cn.fetchone()[0]
    return name


