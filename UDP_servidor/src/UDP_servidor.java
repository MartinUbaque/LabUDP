import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class UDP_servidor {
	
	
	public static void main (String[] args) {
		
		
		// TODO Auto-generated method stub
		BufferedReader reader = new BufferedReader(
	            new InputStreamReader(System.in));
	 
	        // Reading data using readLine
	        
				try {
					String msn = reader.readLine();
					DatagramSocket socket = new DatagramSocket();
					byte[] mensaje = msn.getBytes();
					InetAddress host = InetAddress.getByName("192.168.52.130");
					int puerto = 2525;
					DatagramPacket paquete = new DatagramPacket(mensaje,msn.length(),host,puerto);
					socket.send(paquete);
					
				} catch (SocketException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (UnknownHostException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	}
}
