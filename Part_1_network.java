import java.io.*;
import java.net.*;

public class UdpClient {

public static void main(String[] args) {
  

String addr= "34.73.176.248";  // host address
        int port = 12345;  // port #
 
        try {
            InetAddress address = InetAddress.getByAddress(hostaddr); // to get IP Address
            DatagramSocket socket = new DatagramSocket(); // To create Socket
 
            while (true) {
 
                DatagramPacket request = new DatagramPacket(new byte[1], 1, address, port);
                socket.send(request); // to send request to server
 
                byte[] buffer = new byte[512];
                DatagramPacket response = new DatagramPacket(buffer, buffer.length);
                socket.receive(response); // To receive message from server
 
                String mes = new String(buffer, 0, response.getLength());
 
                System.out.println(mes); // to print received message
                System.out.println();
 
                Thread.sleep(10000);
            }
 
        } catch (SocketTimeoutException ex) {  // exception handling
            System.out.println("Timeout error: " + ex.getMessage());
            ex.printStackTrace();
        } catch (IOException ex) {
            System.out.println("Client error: " + ex.getMessage());
            ex.printStackTrace();
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}
