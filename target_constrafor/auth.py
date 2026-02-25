from hotglue_singer_sdk.target_sdk.auth import Authenticator


class ConstraforAuthenticator(Authenticator):
    @property
    def auth_headers(self) -> dict:
        return {
            "Authorization": f"Api-Key {self._config['access_token']}"
        }
