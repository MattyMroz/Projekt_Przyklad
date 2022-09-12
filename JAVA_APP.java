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
