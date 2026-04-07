import openpyxl
import os

def get_test_data():
    file_path = os.path.join(os.path.dirname(__file__), "sample.xlsx")
    wb = openpyxl.load_workbook(file_path)
    ws = wb["sheet1"]

    data = []

    for r in ws.iter_rows(min_row=2, values_only=True):
        data.append(r)

    return data