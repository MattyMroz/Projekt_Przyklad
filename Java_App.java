System.exit(0);

if (jTextField1.getText().equals("")){
    jLabel2.setText("Wpisz swoje imię");
}
else if (jTextField1.getText().equals("admin")){
    jLabel2.setText("Żegnaj admin");
}
else
{
    jLabel2.setText("Witaj "+jTextField1.getText());
    jTextField1.setText("");
}


Double a = Double.parseDouble(jTextField1.getText());
Double b = Double.parseDouble(jTextField5.getText());
Double c = a + b;
jTextField6.setText(c.toString());




// Zad 1

public class Sum {
    private double A, B, SUM;

    public Sum() {}

    public void setA(double A) {
        this.A = A;
    }

    public double getA() {
        return A;
    }

    public void setB(double B) {
        this.B = B;
    }

    public double getB() {
        return B;
    }

    public void setSUM() {
        SUM = A + B;
    }

    public double getSUM() {
        return SUM;
    }
}

// Button CLICK
Sum s = new Sum();
Double A = Double.parseDouble(jTextField1.getText());
Double B = Double.parseDouble(jTextField5.getText());

s.setA(A);
s.setB(B);
s.setSUM();

jTextField6.setText("" + s.getSUM());


