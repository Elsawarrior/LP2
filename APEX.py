class first {
public static void sendMail(String address, String subject, String body) {
Messaging.SingleEmailMessagemail=newMessaging.SingleEmailMessage();
String[] toAddresses = new String[] {address};
mail.setToAddresses(toAddresses);
mail.setSubject(subject);
mail.setPlainTextBody(body);
Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
}
}
