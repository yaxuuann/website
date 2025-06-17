from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {
        "id": "1",
        "name": "Pupuk SawitPRO 50kg + Abu Janjang 40kg",
        "price": 315934.00,
        "description": "Pupuk SawitPRO adalah pupuk organik yang dapat membantu petani kelapa sawit meningkatkan hasil panen dan kualitas buah.",
        "image": "Pupuk SawitPRO 50kg + Abu Janjang 40kg.png",
        "category": "Fertilizers",
        "rating": 4.5,
        "benefits": [
            "Meningkatkan ketersediaan unsur hara (nitrogen, fosfat, dan kalium)",
            "Membantu perombakan bahan organik (dekomposisi) dan mineralisasi unsur organik",
            "Memicu pertumbuhan tanaman",
            "Melindungi akar dari mikroba patogen",
            "Meningkatkan efisiensi penyerapan dari pupuk lain"
        ],
        "stock": 10,
        "lab_tested": True,
        "dosage": "1 kg Abu Janjang and 0.5 kg SawitPRO per tanaman"
    },
    # Add more products as needed
]

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/products')
def product_listing():
    return render_template('productlisting.html', products=products)

@app.route('/product/<product_id>')
def product_details(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return redirect(url_for('product_listing'))
    return render_template('productdetails.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
