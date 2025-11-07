from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price

@app.route("/discount", methods=["GET"])
def discount():
    try:
        price = float(request.args.get("price"))
        discount = float(request.args.get("discount"))
        result = calculate_discount(price, discount)
        return jsonify({
            "price": price,
            "discount": discount,
            "discounted_price": result
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameters"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
