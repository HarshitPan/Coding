import java.util.Scanner;
public class To_Capital {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("Enter a String ->");
        String str=sc.nextLine();
        char small[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        char capital[]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        String new_string=new String();
        for(int i=0;i<str.length();i++)
        {
            boolean check=true;
            for(int j=0;j<26;j++)
            {
                if(str.charAt(i)==small[j])
                {
                    new_string=new_string+capital[j];
                    check=false;
                    break;
                }
            }
            if(check)
                {
                    new_string=new_string+str.charAt(i);
                }
        }
        System.out.println("Capital String -> "+ new_string);
    }
}
