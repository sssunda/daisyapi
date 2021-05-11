from email.mime.text import MIMEText
from flask_restx import Resource, reqparse

from app.api import response
from app.api.restx import api
from app.api.auth.modules.decorate import jwt_token_required
from app.api.mail.modules.setting import access_mail_server

ns = api.namespace("mail", description="Endpoints for sending email")

parser = reqparse.RequestParser()
parser.add_argument("to_mail_address", required=True)
parser.add_argument("body", required=True)


@ns.route("/send")
class Send(Resource):
    @jwt_token_required
    def post(self, **kwargs):
        parsed = parser.parse_args()

        to_mail_address = parsed.to_mail_address
        body = parsed.body

        if to_mail_address is None or to_mail_address == '' or body is None or body == '':
            # Required Fields
            return response.bad_request()

        # access_mail_server
        smtp = access_mail_server()

        msg = MIMEText(body)
        msg['Subject'] = '[TEST] Daisy API에서 보내드립니다.'
        smtp.sendmail(smtp.user, to_mail_address, msg.as_string())
        smtp.quit()
