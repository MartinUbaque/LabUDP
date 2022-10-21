import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class UDP_servidor {
	
	
	public static void main (String[] args) {
		try {
			DatagramSocket socket = new DatagramSocket(2525);
			
			byte[] buffer = new byte[1024];
			while(true) {
				DatagramPacket paquete = new DatagramPacket(buffer, 1024);
				socket.receive(paquete);
				System.out.println("ip: "+paquete.getAddress());
				System.out.println("puerto : "+paquete.getPort());
				System.out.println("mensaje : "+new String(paquete.getData(),0,paquete.getLength()));
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
