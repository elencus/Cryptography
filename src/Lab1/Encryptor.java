package Lab1;

import java.util.HashMap;
import java.util.Scanner;

public class Encryptor {
    public static void main(String[] args) {
        String original = "АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ";
        String permuted = "ЈУШЊСЏЦОЧЖИЛSЗРФТВДЃЕМЉГПАБКХЌН";

        HashMap<Character, Character> encryption = new HashMap<>();
        for (int i = 0; i < original.length(); i++) {
            encryption.put(original.charAt(i), permuted.charAt(i));
        }

        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine().toUpperCase();

        StringBuilder encryptedText = new StringBuilder();
        for (char c : text.toCharArray()) {
                if (c != ' ') {
                    encryptedText.append(encryption.getOrDefault(c, c));
                }
        }

        System.out.println(encryptedText.toString());

        sc.close();
    }
}
