import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
		// Scanner inputs and var creations
    Scanner input = new Scanner(System.in);
		int lines = Integer.parseInt(input.next());
		int chars = Integer.parseInt(input.next());
		input.nextLine();
		boolean[] heavy = new boolean[chars];
		String[] results = new String[lines];

		// reading in each line of strs and process each str in this loop
		for (int i = 0; i < lines; i++)
		{
			String str = input.nextLine();
			// System.out.println(str);
			char[] letters = new char[chars];

			// adding chars of each str to an arr
			for (int j = 0; j < chars; j++)
			{
				char ch = str.charAt(j);
				letters[j] = ch;
			}

			// checking if each char is light or heavy
			for (int k = 0; k < letters.length; k++)
			{
				for (int j = 0; j < letters.length; j++)
				{
					// for debugging purposes only
					//System.out.println("k=" + k + ",j=" + j + ",letters[k]=" + letters[k] + ",letters[j]=" + letters[j]);
					if (k == j)
					{
						continue;
					}
					if (letters[k] == letters[j])
					{
						//System.out.println("found duplicate: " + letters[k]);
						heavy[k] = true;
						break;
					}
				}
			}
			
			//System.out.println(Arrays.toString(heavy));

			// check if the str alternates between light and heavy
			String result = "T";
			for (int p = 0; p < heavy.length - 1; p++)
			{
				if (heavy[p] == heavy[p + 1])
				{
					result = "F";
					results[i] = result;
					break;
				}
				else if (p + 2 < heavy.length && heavy[p] == heavy[p + 2] && heavy[p] != heavy[p + 1])
				{
					result = "T";
					results[i] = result;
					break;
				}
			}
			results[i] = result;
		}

		// print the results on separate lines
		for (int i = 0; i < results.length; i++)
		{
			System.out.println(results[i]);
		}
		input.close();
  }
}