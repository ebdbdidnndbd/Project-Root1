from flask import Flask, request, jsonify

app = Flask(__name__)

# صفحة العرض الأساسية للتأكد أن الرابط يعمل
@app.route('/')
def home():
    return "<h1>Receiver is Online</h1><p>Send POST requests to /collect</p>"

# المسار المخصص لاستقبال المعلومات
@app.route('/collect', methods=['POST', 'GET'])
def collect():
    if request.method == 'POST':
        # استقبال البيانات بغض النظر عن نوعها
        data = request.get_json(silent=True) or request.form.to_dict()
        
        # طباعة البيانات في "Logs" الخاصة بالسيرفر لكي تراها أنت
        print(f"Received Data: {data}")
        
        return jsonify({
            "status": "success",
            "received_data": data
        }), 200
    else:
        return "Method Not Allowed. Use POST to send data.", 405

# تعريف الـ handler الخاص بـ Vercel
def handler(event, context):
    return app(event, context)
