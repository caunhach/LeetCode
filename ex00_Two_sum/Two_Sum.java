
package leetcode_practice.ex00_Two_sum;

import java.util.*;

public class Two_Sum{
    static int size = 4;
    static int target = 9;
    public static void main(String[] args){
        Scanner out = new Scanner(System.in);
        ArrayList<Integer> array = new ArrayList<Integer>();
        for (int i = 0; i < size; i++){
            int num = out.nextInt();
            array.add(num);
        }
        int[] num_list = array.stream().mapToInt(Integer::intValue).toArray();
        System.out.println(Arrays.toString(num_list));
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < num_list.length; i++){
            map.put(num_list[i], i);
        }
        for (int i = 0; i < num_list.length; i++){
            int primitive = target - num_list[i];
            if (map.containsKey(primitive) && map.get(primitive) != i){
                System.out.println(num_list[i] + " " + primitive);
                break;
            }
        }
        out.close();
    }
}