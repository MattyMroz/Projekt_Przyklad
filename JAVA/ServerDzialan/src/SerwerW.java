import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Vector;

public class SerwerW {
	public static void main(String[] args) {
		Vector<WatekKlienta> v = new Vector<WatekKlienta>();
		try {

			ServerSocket s = new ServerSocket(2011);
			System.out.println("Serwer Run...");

			while (true) {
				Socket incoming = s.accept();

				WatekKlienta thread = new WatekKlienta(incoming);
				v.addElement(thread);

			}
			// s.close();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
