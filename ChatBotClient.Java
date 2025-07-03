import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ChatbotClient {

    public static void askQuestion(String message) {
        try {
            URL url = new URL("http://localhost:5000/chatbot");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);

            String jsonInputString = "{\"message\": \"" + message + "\"}";

            try(OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"));
            StringBuilder response = new StringBuilder();
            String responseLine;
            while ((responseLine = br.readLine()) != null) {
                response.append(responseLine.trim());
            }

            System.out.println("Chatbot Response: " + response.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Ask your question (or type 'exit' to quit):");
            String question = sc.nextLine();
            if (question.equalsIgnoreCase("exit")) {
                System.out.println("Exiting chatbot.");
                break;
            }
            askQuestion(question);
        }
        sc.close();
    }
}

