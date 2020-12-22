from rest_auth.serializers import PasswordResetSerializer


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        return {
            'html_email_template_name': 'password_reset_email.html',
            'subject_template_name': 'subject_template_name.txt',
        }
