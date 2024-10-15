import requests

url = 'http://127.0.0.1:5000/'

data = {
    'duedate' : 'September 1, 2024',
    'from_addr' : {
        'addr1' : 'Hamilton, NY',
        'addr2' : 'Sunnyville, CA 12345',
        'company_name' : 'ABC'
    },
    'invoice_number ' : 156,
    'items' : [{
        'charge' : 500.0,
        'title' : 'Logo Design'
    },{
        'charge' : 85.0,
        'title' : 'Hosting (6 Months)'
    },{
        'charge' : 10.0,
        'title' : 'Domain Name (1 year)'
    }],
    'to_addr' : {
        'company_name' : 'CUI Isb',
        'person_email' : 'abc@gmail.com',
        'person_name' : 'Zeeshan Aftab'
    }
}

html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)