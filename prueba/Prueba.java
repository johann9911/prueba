package prueba;

public class Prueba {

	public static void main(String[] args) {
		for(int i=1;i<=100;i++) {
			if(i%3==0 && i%5==0) {
				System.out.println("mareigua");
			}else if(i%3==0) {
				System.out.println("mare");
			}else if(i%5==0) {
				System.out.println("igua");
			}
		}
	}

}
