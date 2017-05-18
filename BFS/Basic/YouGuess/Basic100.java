import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.nio.charset.*;
public class Basic100{
	public static void main(String[] args){
		try {
			BufferedReader br = new BufferedReader(new FileReader("Basic-04.txt"));
			StringBuilder sb = new StringBuilder();
			String line = br.readLine();

			while (line != null) {
				sb.append(line);
				//sb.append(System.lineSeparator());
				line = br.readLine();
			}
			String encodeFlag = sb.toString();
			byte[] outData = hexStringToByteArray(encodeFlag);
			System.out.println(encodeFlag);
			FileOutputStream fos = new FileOutputStream("flag.zip");
			fos.write(outData);
			fos.close();
		} catch (Exception e){
			e.printStackTrace();
		}
	}
	public static byte[] hexStringToByteArray(String s) {
		int len = s.length();
		byte[] data = new byte[len / 2];
		for (int i = 0; i < len; i += 2) {
			data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
								 + Character.digit(s.charAt(i+1), 16));
		}
		return data;
	}
}