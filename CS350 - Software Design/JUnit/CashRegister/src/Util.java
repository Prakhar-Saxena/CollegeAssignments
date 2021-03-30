/**
 * @author Sean Grimes, 09/19/17
 * <p>
 * I really just don't like typing System.out.println("...") all over the place.
 * </p>
 */
public class Util {

    public static void writeln(Object msg){
        System.out.println(msg);
    }

    public static void writef(String format, Object... args){
        System.out.print(String.format(format, args));
    }

}
