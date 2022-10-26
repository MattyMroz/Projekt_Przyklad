import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Vector;

public class WatekKlienta extends Thread {
	Socket socket;
	InputStream in;
	OutputStream out;

	WatekKlienta(Socket socket) throws IOException {
		this.socket = socket;
		this.in = socket.getInputStream();
		this.out = socket.getOutputStream();
		start();
	}

	public void run() {
		try {
			boolean done = false;

			int k;
			StringBuffer sb;

			while (!done) {
				out.write("Wybierz operacje jaka ma wykonac serwer\n".getBytes());
				out.write("dodawanie   ==> \"+\"\n".getBytes());
				out.write("odejmowanie ==> \"-\"\n".getBytes());
				out.write("mnozenie    ==> \"*\"\n".getBytes());
				out.write("dzielenie   ==> \"/\"\n".getBytes());
				out.write("Wybor: \n".getBytes());

				sb = new StringBuffer();
				while ((k = in.read()) != -1 && k != '\n')
					sb.append((char) k);
				String operacja = sb.toString();

				out.write("a= \n".getBytes());
				sb = new StringBuffer();
				while ((k = in.read()) != -1 && k != '\n')
					sb.append((char) k);
				float a = Float.valueOf(sb.toString()).floatValue();

				out.write("b= \n".getBytes());
				sb = new StringBuffer();
				while ((k = in.read()) != -1 && k != '\n')
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
				out.write(("a " + operacja + " b = " + wynik + "\n").getBytes());
				out.write("Czy chcesz zakończyć ? <t/n> \n".getBytes());

				sb = new StringBuffer();
				while ((k = in.read()) != -1 && k != '\n')
					sb.append((char) k);
				String koniec = sb.toString().trim();

				if (koniec.equals("t") || koniec.equals("T"))
					done = true;

			}
			in.close();
			out.close();
			socket.close();
		} catch (IOException e) {
			System.out.println(e);
		}
	}

}
