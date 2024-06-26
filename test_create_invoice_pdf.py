# -*- coding: utf-8 -*-

from dds_registration.core.helpers.create_invoice_pdf import create_invoice_pdf, TInvoicePdfParams
from dds_registration.core.constants.payments import payment_details_by_currency

# External parameters


optional_text = "Optional invoice text"
client_name = "Nataliia Magdanova"
client_address = """
Client address
multiline text
with a city, a country
and a zip
"""
dds_name = "Départ de Sentier"
dds_address = """
Dorfsteig 8
5223 Riniken
Switzerland
VAT CHE-329.638.515
"""
invoice_no = "#2324"
invoice_date = "May 4, 2023"
payment_terms = "Within **30 business days** of invoice issuance"
currency = "CAD"
payment_details = payment_details_by_currency[currency]


def test_create_invoice_pdf():
    table_data = (
        (
            # Header...
            "Quantity",
            "Event",
            "Option",
            "Costs ({})".format(currency),
        ),
        (
            1,
            "Autumn School on Open Inventory Data Manipulation; October 9-13, 2023; Grosshöchstetten, CH",
            "Shared double room",
            1224,
        ),
        (
            "",
            "__Total__",
            "",
            "__1224__",
        ),
    )

    # Test...

    invoice_pdf_params: TInvoicePdfParams = {
        #  "currency": currency,
        "optional_text": optional_text,
        "client_name": client_name,
        "client_address": client_address,
        "dds_name": dds_name,
        "dds_address": dds_address,
        "invoice_no": invoice_no,
        "invoice_date": invoice_date,
        "payment_terms": payment_terms,
        "payment_details": payment_details,
        "table_data": table_data,
    }

    pdf = create_invoice_pdf(invoice_pdf_params)

    # Output pdf
    pdf.output("test.pdf")


if __name__ == "__main__":
    test_create_invoice_pdf()
