import os
import pandas as pd
from datetime import datetime

# Filename for the storage
EXCEL_FILE = "business_tracker.xlsx"

def initialize_database():
    """Creates the Excel sheets if they don't exist yet."""
    if not os.path.exists(EXCEL_FILE):
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
            # Stock Sheet
            pd.DataFrame(columns=["Item ID", "Item Name", "Category", "Stock Added", "Current Stock",
                                  "Cost Price (UGX)"]).to_excel(writer, sheet_name="Stock", index=False)
            # Sales Sheet
            pd.DataFrame(columns=["Date", "Item Name", "Quantity Sold", "Selling Price (UGX)", "Total Revenue (UGX)",
                                  "Order Type (Retail/Preorder)"]).to_excel(writer, sheet_name="Sales", index=False)
            # Expenses Sheet
            pd.DataFrame(
                columns=["Date", "Expense Name", "Amount (UGX)", "Category (Shipping/Marketing/Other)"]).to_excel(
                writer, sheet_name="Expenses", index=False)
        print(f"🎉 Created new tracking database: {EXCEL_FILE}")


def load_sheet(sheet_name):
    return pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)


def save_all_sheets(stock_df, sales_df, expenses_df):
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        stock_df.to_excel(writer, sheet_name="Stock", index=False)
        sales_df.to_excel(writer, sheet_name="Sales", index=False)
        expenses_df.to_excel(writer, sheet_name="Expenses", index=False)


def add_stock():
    print("\n--- 📦 ADD NEW INVENTORY ---")
    stock_df = load_sheet("Stock")
    sales_df = load_sheet("Sales")
    expenses_df = load_sheet("Expenses")

    item_id = input("Enter unique Item ID (e.g., J01, B01): ").strip().upper()
    name = input("Enter Item Name: ").strip()
    category = input("Enter Category (Jewelry / Beddings / Housewares): ").strip()
    qty = int(input("Quantity Added: "))
    cost_price = float(input("Cost Price per item in UGX (Buying price + split shipping cost): "))

    # Check if item exists to update stock, or add a new row
    if item_id in stock_df['Item ID'].values:
        idx = stock_df[stock_df['Item ID'] == item_id].index[0]
        stock_df.at[idx, 'Stock Added'] += qty
        stock_df.at[idx, 'Current Stock'] += qty
    else:
        new_row = {
            "Item ID": item_id, "Item Name": name, "Category": category,
            "Stock Added": qty, "Current Stock": qty, "Cost Price (UGX)": cost_price
        }
        stock_df = pd.concat([stock_df, pd.DataFrame([new_row])], ignore_index=True)

    save_all_sheets(stock_df, sales_df, expenses_df)
    print(f"✅ Successfully updated stock for {name}!")


def record_sale():
    print("\n--- 💰 RECORD A SALE / PRE-ORDER ---")
    stock_df = load_sheet("Stock")
    sales_df = load_sheet("Sales")
    expenses_df = load_sheet("Expenses")

    item_id = input("Enter Item ID being sold: ").strip().upper()

    if item_id not in stock_df['Item ID'].values:
        print("❌ Error: Item ID not found in Stock database. Please add stock first.")
        return

    idx = stock_df[stock_df['Item ID'] == item_id].index[0]
    item_name = stock_df.at[idx, 'Item Name']
    current_stock = stock_df.at[idx, 'Current Stock']

    print(f"Item: {item_name} | Available Stock: {current_stock}")
    qty = int(input("Quantity Sold: "))

    order_type = input("Is this a standard Retail sale or a Pre-order? (R/P): ").strip().upper()
    order_str = "Preorder" if order_type == 'P' else "Retail"

    # Check stock limit if it's a regular retail sale
    if order_str == "Retail" and qty > current_stock:
        print(f"⚠️ Warning: Not enough physical stock. Only {current_stock} available.")
        proceed = input("Proceed anyway? (y/n): ").strip().lower()
        if proceed != 'y': return

    sell_price = float(input("Selling Price per item in UGX: "))
    total_rev = qty * sell_price
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Deduct stock
    stock_df.at[idx, 'Current Stock'] -= qty

    # Log Sale row
    new_sale = {
        "Date": date_str, "Item Name": item_name, "Quantity Sold": qty,
        "Selling Price (UGX)": sell_price, "Total Revenue (UGX)": total_rev,
        "Order Type (Retail/Preorder)": order_str
    }
    sales_df = pd.concat([sales_df, pd.DataFrame([new_sale])], ignore_index=True)

    save_all_sheets(stock_df, sales_df, expenses_df)
    print(f"✅ Registered sale of {qty}x {item_name} for total {total_rev:,.0f} UGX!")


def record_expense():
    print("\n--- 🧾 RECORD AN EXPENSE ---")
    stock_df = load_sheet("Stock")
    sales_df = load_sheet("Sales")
    expenses_df = load_sheet("Expenses")

    name = input("Expense Description (e.g., Delivery rider, TikTok Ads, Packaging): ").strip()
    amount = float(input("Amount in UGX: "))
    cat = input("Category (Marketing / Delivery / Packaging / Other): ").strip()
    date_str = datetime.now().strftime("%Y-%m-%d")

    new_expense = {"Date": date_str, "Expense Name": name, "Amount (UGX)": amount,
                   "Category (Shipping/Marketing/Other)": cat}
    expenses_df = pd.concat([expenses_df, pd.DataFrame([new_expense])], ignore_index=True)

    save_all_sheets(stock_df, sales_df, expenses_df)
    print(f"✅ Expense of {amount:,.0f} UGX documented.")


def view_dashboard():
    print("\n================ 📊 BUSINESS DASHBOARD ================")
    stock_df = load_sheet("Stock")
    sales_df = load_sheet("Sales")
    expenses_df = load_sheet("Expenses")

    total_revenue = sales_df['Total Revenue (UGX)'].sum()
    total_expenses = expenses_df['Amount (UGX)'].sum()

    # Calculate Cost of Goods Sold (COGS) dynamically based on sales
    cogs = 0
    for _, sale in sales_df.iterrows():
        match_stock = stock_df[stock_df['Item Name'] == sale['Item Name']]
        if not match_stock.empty:
            cost_price = match_stock.iloc[0]['Cost Price (UGX)']
            cogs += sale['Quantity Sold'] * cost_price

    net_profit = total_revenue - cogs - total_expenses

    print(f"💰 Total Revenue:     {total_revenue:,.0f} UGX")
    print(f"📦 Cost of Goods:     {cogs:,.0f} UGX (Wholesale product costs)")
    print(f"🧾 Operating Costs:   {total_expenses:,.0f} UGX (Ads, delivery, etc.)")
    print("-----------------------------------------------------")
    if net_profit >= 0:
        print(f"📈 NET PROFIT:        {net_profit:,.0f} UGX")
    else:
        print(f"📉 NET LOSS:          {abs(net_profit):,.0f} UGX")
    print("=====================================================")


def main():
    initialize_database()
    while True:
        print("\n🌟 LUXURY RETAIL TRACKER 🌟")
        print("1. Record New Stock / Inventory")
        print("2. Record a Sale or Pre-Order")
        print("3. Record an Expense")
        print("4. View Financial Performance Dashboard")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            add_stock()
        elif choice == '2':
            record_sale()
        elif choice == '3':
            record_expense()
        elif choice == '4':
            view_dashboard()
        elif choice == '5':
            print("Goodbye! Success in your business journey.")
            break
        else:
            print("❌ Invalid entry, please try again.")


if __name__ == "__main__":
    main()
