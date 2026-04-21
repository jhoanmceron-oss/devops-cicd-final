from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>DevOps CI/CD</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: #0f0c29;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .card {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 50px 60px;
            text-align: center;
            max-width: 600px;
        }
        .badge {
            background: #00c896;
            color: #003d2e;
            font-size: 13px;
            font-weight: bold;
            padding: 6px 16px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 24px;
            letter-spacing: 1px;
        }
        h1 {
            font-size: 2.8rem;
            margin-bottom: 12px;
            background: linear-gradient(90deg, #00c896, #7b61ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p {
            color: rgba(255,255,255,0.6);
            font-size: 1.1rem;
            margin-bottom: 36px;
        }
        .tags {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }
        .tag {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            padding: 8px 18px;
            border-radius: 30px;
            font-size: 13px;
            color: rgba(255,255,255,0.85);
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">LIVE EN PRODUCCION</div>
        <h1>Hola Mundo!</h1>
        <p>Desplegado automaticamente con CI/CD<br>usando GitHub Actions y Docker</p>
        <div class="tags">
            <span class="tag">Python + Flask</span>
            <span class="tag">Docker</span>
            <span class="tag">GitHub Actions</span>
            <span class="tag">Render</span>
        </div>
    </div>
</body>
</html>
'''

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
