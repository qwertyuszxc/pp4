from prettytable import PrettyTable

items = [
    {"name": "Clean Code, Robert C. Martin", "netto": 100.00, "vat_rate": 8},
    {"name": "Applying UML and Patterns, C. Larman", "netto": 300.00, "vat_rate": 8},
    {"name": "Shipping", "netto": 50.00, "vat_rate": 23}
]

total_netto_8 = 0
total_netto_23 = 0
vat_sums = {}

for item in items:
    if item["vat_rate"] == 8:
        total_netto_8 += item["netto"]
    elif item["vat_rate"] == 23:
        total_netto_23 += item["netto"]

total_vat_8 = total_netto_8 * 8 / 100
total_vat_23 = total_netto_23 * 23 / 100

table = [['', 'Total net', 'Total vat'], ["VAT 8%", total_netto_8, total_vat_8], ["VAT 23%", total_netto_23, total_vat_23]]
tab = PrettyTable(table[0],  align='c', valign='t')
tab.add_rows(table[1:])
print(tab)
