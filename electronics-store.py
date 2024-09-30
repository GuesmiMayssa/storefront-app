from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='static')
app.secret_key = 'dVNzwMa5AaYXUBhs7uQX'
# Dummy product data
products = [
    {'id': 1, 'name': 'Smartphone', 'price': 599, 'description': 'Latest 5G smartphone', 'image': 'images/smartphone.jpg'},
    {'id': 2, 'name': 'Laptop', 'price': 999, 'description': 'High-performance laptop', 'image': 'images/laptop.jpg'},
    {'id': 3, 'name': 'Headphones', 'price': 199, 'description': 'Noise-canceling headphones', 'image': 'images/headphones.jpg'}
]


@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
        session.modified = True
    return redirect(url_for('view_cart'))

@app.route('/healthz')
def health_check():
    return jsonify(status="healthy"), 200
@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        cart = session.get('cart', [])
        total = sum(item['price'] for item in cart)
        session['cart'] = []  # Clear the cart after checkout
        return redirect(url_for('checkout_complete'))
    
    # Render checkout page if GET request
    return render_template('checkout.html')

@app.route('/checkout-complete')
def checkout_complete():
    return render_template('checkout_complete.html')

@app.context_processor
def cart_count():
    return {'cart_count': len(session.get('cart', []))}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
