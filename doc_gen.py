from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [
    [2, "pen", 0.5, 1],
    [1, "paper pack", 5, 5],
    [2, "notebook", 2, 4]
]

subtotal = sum(item[3] for item in invoice_list)
total = subtotal  # No GST, total is just the subtotal

doc.render({
    "name": "John",
    "phone": "555-55555",
    "invoice_list": invoice_list,
    "subtotal": subtotal,
    "total": total
})

doc.save("new_invoice.docx")
