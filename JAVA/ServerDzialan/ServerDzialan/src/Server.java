import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	public static void main(String[] args) {
		try {

			ServerSocket s = new ServerSocket(2011);
			System.out.println("Serwer Run...");

			while (true) {
				Socket incoming = s.accept();

				InputStream inStream = incoming.getInputStream();
				OutputStream outStream = incoming.getOutputStream();

				boolean done = false;

				int k;
				StringBuffer sb;

				while (!done) {
					outStream.write("Wybierz operacje jaka ma wykonac serwer\n".getBytes());
					outStream.write("dodawanie   ==> \"+\"\n".getBytes());
					outStream.write("odejmowanie ==> \"-\"\n".getBytes());
					outStream.write("mnozenie    ==> \"*\"\n".getBytes());
					outStream.write("dzielenie   ==> \"/\"\n".getBytes());
					outStream.write("Wybor: \n".getBytes());

					sb = new StringBuffer();
					while ((k = inStream.read()) != -1 && k != '\n')
						sb.append((char) k);
					String operacja = sb.toString();

					outStream.write("a= \n".getBytes());
					sb = new StringBuffer();
					while ((k = inStream.read()) != -1 && k != '\n')
						sb.append((char) k);
					float a = Float.valueOf(sb.toString()).floatValue();

					outStream.write("b= \n".getBytes());
					sb = new StringBuffer();
					while ((k = inStream.read()) != -1 && k != '\n')
						sb.append((char) k);
					float b = Float.valueOf(sb.toString()).floatValue();

					operacja = operacja.trim();
					float wynik = 0;
					if (operacja.equals("+"))
						wynik = a + b;
					if (operacja.equals("-"))
						wynik = a - b;
					if (operacja.equals("*"))
						wynik = a * b;
					if (operacja.equals("/"))
						wynik = a / b;
					outStream.write(("a " + operacja + " b = " + wynik + "\n").getBytes());
					outStream.write("Czy chcesz zakończyć ? <t/n> \n".getBytes());

					sb = new StringBuffer();
					while ((k = inStream.read()) != -1 && k != '\n')
						sb.append((char) k);
					String koniec = sb.toString().trim();

					if (koniec.equals("t") || koniec.equals("T"))
						done = true;

				}
				inStream.close();
				outStream.close();
			}
			// s.close();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
