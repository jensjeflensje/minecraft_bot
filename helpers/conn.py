from minecraft.networking.connection import Connection

def create_conn(address, port, version, token):
    mc_conn = Connection(
        address=address,
        port=port,
        auth_token=token,
        initial_version=version,
        allowed_versions=[version],
    )
    mc_conn.connect()
    return mc_conn
