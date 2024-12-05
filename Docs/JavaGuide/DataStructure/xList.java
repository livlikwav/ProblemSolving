package Docs.JavaGuide.DataStructure;

import java.util.ArrayList;
import java.util.Collections;

public class xList {
    /*
     * https://wikidocs.net/121712
     * ar.add(val);
     * ar.add(idx, val);
     * ar.remove(idx);
     * ar.get(idx);
     * idx = ar.indexOf(val);
     * ar.size();
     * bool = ar.contains(val);
     */
    static void ArrayList() {
        ArrayList<Integer> mylist = new ArrayList<Integer>();
        System.out.println(mylist.toString()); // []

        mylist.add(9);
        mylist.add(8);
        mylist.add(7);
        System.out.println(mylist.toString());

        // 정렬
        Collections.sort(mylist);
        System.out.println(mylist.toString());
    }
}

/*
 * https://wikidocs.net/121712
 * ArrayList 는 동적 배열
 * LinkedList 는 연결 리스트 (순차 탐색에 약하고, 값 중간 추가에 강하다)
 */