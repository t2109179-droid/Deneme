from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
  print("🌐 [LOG] Biri ana sayfaya girdi.")
  return render_template("index.html")


@app.route("/api/istek-at", methods=["GET"])
def istek_at():
  print("\n" + "=" * 40)
  print("🚀 [KONSOL]: Butona basıldı ve Python sunucusuna istek geldi!")
  print("=" * 40 + "\n")

  return jsonify({
      "durum": "Başarılı",
      "mesaj": "İstek Python sunucusuna ulaştı ve konsola yazdırıldı! ✅",
  })


if __name__ == "__main__":
  # iOS kısıtlamalarına takılmamak için parametresiz çalıştırıyoruz
  app.run()
