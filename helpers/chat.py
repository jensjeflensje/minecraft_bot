from minecraft.networking.packets import serverbound

def send_message(conn, msg):
    packet = serverbound.play.ChatPacket()
    packet.message = str(msg)
    conn.write_packet(packet)
