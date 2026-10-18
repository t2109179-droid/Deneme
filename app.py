from flask import Flask, render_template_string

app = Flask(__name__)

HTML_SABLONU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Vercel Flask Test</title>
</head>
<body>
    <h1>Vercel Uzerinde Calisiyor!</h1>
    <button onclick="tikla()">Butona Tikla</button>

    <script>
        function tikla() {
            fetch('/tiklandi', { method: 'POST' })
                .then(response => response.text())
                .then(data => alert("Istek gonderildi!"));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def ana_sayfa():
    return render_template_string(HTML_SABLONU)

@app.route('/tiklandi', methods=['POST'])
def buton_tiklandi():
    print("🚀 [VERCEL KONSOL]: Butona basildi!")
    return "OK"

if __name__ == '__main__':
    app.run()
