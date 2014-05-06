import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * codeeval Challenge "Longest Lines"
 * https://www.codeeval.com/open_challenges/2/
 * Read lines from stdin (description wrongly says "from a file") and
 * output the 'n' longest lines to stdout.
 * 
 * @author Marshall Farrier
 * @since 2014-05-05
 *
 */
public class Main {

    /**
     * @param args
     */
    public static void main(String[] args) {
        
    	Scanner kbd = new Scanner(System.in);
        try {
            int n = Integer.parseInt(kbd.nextLine());
            String line;
            PriorityQueue<String> longest = new PriorityQueue<String>(n, new Comparator<String>() {
            	public int compare(String a, String b) {
            		return a.length() - b.length();
            	}
            });
            while (kbd.hasNext()) {
            	line = kbd.nextLine();
            	if (longest.size() < n) {
            		longest.add(line);
            	} else if (line.length() > longest.peek().length()) {
            		longest.poll();
            		longest.add(line);
            	}
            }
            int heapSize = longest.size();
            String[] linesToShow = new String[heapSize];
            for (int i = heapSize - 1; i >= 0; --i) {
            	linesToShow[i] = longest.poll();
            }
            for (int i = 0; i < heapSize; ++i) {
            	System.out.println(linesToShow[i]);
            }
        } finally {
            kbd.close();
        }
    }

}
