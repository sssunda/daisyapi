from email.mime.text import MIMEText
from flask_restx import Resource, reqparse
import smtplib

from app.api.restx import api
from app.api.auth.modules.decorate import jwt_token_required
from app.util.configs import get_config

ns = api.namespace("mail", description="Endpoints for sending email")

parser = reqparse.RequestParser()
parser.add_argument("subject", required=True)
parser.add_argument("to_addrs", type=str, action='append', required=True)
parser.add_argument("body", required=True)


@ns.route("")
class Send(Resource):
    @jwt_token_required
    def post(self, **kwargs):
        parsed = parser.parse_args()

        # access_mail_server
        smtp = self.access_mail_server()

        msg = MIMEText(parsed.body)
        msg['Subject'] = parsed.subject
        smtp.sendmail(smtp.user, ', '.join(parsed.to_addrs), msg.as_string())
        smtp.quit()

    def access_mail_server(self):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()

        master_email = get_config('EMAIL')
        master_password = get_config('EMAIL_PASSWORD')
        smtp.login(master_email, master_password)

        return smtp
