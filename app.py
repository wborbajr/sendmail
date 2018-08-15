import sendmail

from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/contato', methods=['POST'])
def send_email():
    data = request.form
    email = sendmail.MailSender(data['usuario'], data['senha'], data['destinatario'], data['assunto'], data['conteudo'])
    status = email.send_email()
    
    return status
  
'''
curl -X POST \
  http://localhost:1469/contato \
  -F usuario=alguem.no.gmail@gmail.com \
  -F 'senha=*********' \
  -F destinatario=alguem.no.gmail@gmail.com \
  -F 'assunto=CARA DEU' \
  -F 'conteudo=Nossa funcionou mesmo'
'''
  
#from flask import make_response
#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify({'error': 'Not found'}), 404)

# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1469)