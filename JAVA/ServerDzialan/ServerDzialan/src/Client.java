import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
	public static void main(String[] args) {
		try {
			BufferedReader keyboardStream = new BufferedReader(new InputStreamReader(System.in));

			Socket socket = new Socket("localhost", 2011);
			InputStream inStream = socket.getInputStream();
			OutputStream outStream = socket.getOutputStream();

			boolean done = false;

			int k;
			StringBuffer sb;

			while (!done) {

				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());

				outStream.write((keyboardStream.readLine() + "\n").getBytes());

				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());

				outStream.write((keyboardStream.readLine() + "\n").getBytes());

				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());

				outStream.write((keyboardStream.readLine() + "\n").getBytes());

				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());
				sb = new StringBuffer();
				while ((k = inStream.read()) != -1 && k != '\n')
					sb.append((char) k);
				System.out.println(sb.toString());

				String koniec = keyboardStream.readLine();

				outStream.write((koniec + "\n").getBytes());

				if (koniec.equals("t") || koniec.equals("T")) {
					done = true;
				} else {
					done = false;
				}

			}
			inStream.close();
			outStream.close();
			socket.close();

		} catch (Exception e) {

		}
	}
}
