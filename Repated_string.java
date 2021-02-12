import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        int i,j;
        String s1="";
        long c=0,d=0;
        long x=0;
         long y=0,z=0;
        for(i=0;i<s.length();i++)
        {
            if(s.charAt(i)=='a')
            c++;
        }
        y=(n/s.length());
        z=(n%s.length());
        int v=(int)z;
        if(z!=0)

        {  s1=s.substring(0,v);
            for(i=0;i<s1.length();i++)
            {   
            if(s1.charAt(i)=='a')
            d++;
            }
        }
        x=(y*c)+d;
        return x;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        long n = scanner.nextLong();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        long result = repeatedString(s, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
