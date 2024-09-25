from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'haroldmorales720@gmail.com'  
app.config['MAIL_PASSWORD'] = 'wxeo koua tyay gpzr'        

mail = Mail(app)

@app.route('/modalidad', methods=['POST'])
def send_email():
    data = request.get_json()
    try:
        body_content = f"""
        Estimado/a,

        Le informamos que se ha completado exitosamente la reserva con los siguientes detalles:
        
        Modalidad: {data['modalidad']}
        Fecha: {data['fecha']}
        Hora: {data['hora']}
        Precio: {data['precio']}
        Fecha de Inicio: {data['fecha_inicio']}
        Fecha de Fin: {data['fecha_fin']}
        
        """
        msg = Message(subject=data['subject'],
                        sender=app.config['MAIL_USERNAME'],
                        recipients=[data['recipients']],  
                        body=body_content)  

        mail.send(msg)
        return jsonify({"message": "Correo enviado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)