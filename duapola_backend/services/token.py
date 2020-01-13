from rest_framework_simplejwt.tokens import RefreshToken


class Token():
    def generate(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)
