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
