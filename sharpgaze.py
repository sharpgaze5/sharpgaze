from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example product list (later can be loaded from database)
products = [
    {"id": 1, "name": "Active Performance Tee", "price": 999, "image": "https://placehold.co/600x600/e2e8f0/ffffff?text=Active+Tee"},
    {"id": 2, "name": "Training Shorts", "price": 1299, "image": "https://placehold.co/600x600/e2e8f0/ffffff?text=Training+Shorts"},
    {"id": 3, "name": "Essential Gym Joggers", "price": 1799, "image": "https://placehold.co/600x600/e2e8f0/ffffff?text=Gym+Joggers"},
    {"id": 4, "name": "Seamless Sports Bra", "price": 899, "image": "https://placehold.co/600x600/e2e8f0/ffffff?text=Sports+Bra"},
]

@app.route("/")
def home():
    return render_template("sharpgaze.html", products=products)

@app.route("/product/<int:id>")
def product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return render_template("product.html", product=product)
    return "Product not found", 404

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    print(f"📩 New subscriber: {email}")  # later save to DB or send to Mailchimp
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
