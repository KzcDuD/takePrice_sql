from flask import Flask, render_template, request
from model import db, Product, Price

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:secribe_su_contrasena@localhost:3306/price_comparison" ## 'sqlite:///pricing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def search_product():
    product_name = request.args.get('name')
    product = Product.query.filter_by(name=product_name).first()
    if product:
        prices = Price.query.filter_by(product_id=product.id).all()
        return render_template('index.html', product=product, prices=prices)
    else:
        return render_template('index.html', message='Product not found')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
