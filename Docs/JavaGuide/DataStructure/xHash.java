package Docs.JavaGuide.DataStructure;

import java.util.HashMap;
import java.util.Map;

public class xHash {
    /*
     * hm.get(key)
     * hm.remove(key)
     * hm.clear()
     * hm.size()
     * hm.entrySet()
     * hm.keySet()
     * hm.values()
     * hm.getOrDefault(key, defaultVal)
     */
    static void HashMap() {
        String[] words = { "apple", "banana", "apple", "orange" };
        HashMap<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        for (String key : wordCount.keySet()) {
            System.out.println(key + ": " + wordCount.get(key));
        }

        // k,v loop
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            if (entry.getValue() == 1) {
                System.out.println("Key: " + entry.getKey());
            }
        }

        // k,v loop with Java 8 Stream
        wordCount.entrySet().stream()
                .filter(entry -> entry.getValue() == 1)
                .forEach(entry -> System.out.println("Key: " + entry.getKey()));
    }
}