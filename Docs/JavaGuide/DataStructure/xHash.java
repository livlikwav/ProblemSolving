package Docs.JavaGuide.DataStructure;

import java.util.HashMap;

public class xHash {
    /*
     * hm.get(key)
     * hm.remove(key)
     * hm.clear()
     * hm.size()
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
    }
}