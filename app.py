from flask import Flask, render_template, request
from datetime import datetime
import json
from chat import tellme_bot

app = Flask(__name__)

@app.route('/')
def hello_world():
    cur_year = datetime.now().year
    return render_template('home.html',year=cur_year )

@app.route('/chat-bot')
def chat():
    return render_template('chat.html')



# with open('static/products_data.json', 'r') as file:
#     product_data = json.load(file)

# # Example function to retrieve product information based on intent
# def get_product_info(intent, product_name):
#     if intent == 'product_inquiry':
#         products = product_data['products']
#         for product in products:
#             if product['name'].lower() == product_name.lower():
#                 return product
#         return None

@app.route('/submit', methods=['POST'])
def submit():
    res_in = request.form.get('query')
    product_info = tellme_bot(response=res_in)
    return render_template('chat.html', result=product_info)




if __name__ == '__main__':
    app.run(debug=True)