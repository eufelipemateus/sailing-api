from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token, create_refresh_token
from flask_restful import Resource

class TokenRefresh(Resource):
    """
    Token Refresh Api
    """

    @jwt_refresh_token_required
    def post(self):

        # Generating new access token
        current_user = get_jwt_identity()

        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)

        return {'access_token': access_token, 'refresh_token': refresh_token}