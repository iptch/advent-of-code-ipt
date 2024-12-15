package ch.asp.aoc.util;

public class SortUtil {
    public static void sort(int[] list){
        quicksort(list, 0, list.length-1);
    }

    private static void quicksort(int[] list, int low, int high){
        if (low >= high || low < 0){
            return;
        }
        int p = partition(list, low, high);
        quicksort(list, low, p-1);
        quicksort(list, p+1, high);
    }

    private static int partition(int[] list, int low, int high){
        int pivot = list[high];
        int i = low;

        for (int j = low; j < high;j++){
            if(list[j] <= pivot) {
                swap(list, i, j);
                i++;
            }
        }
        swap(list, i, high);
        return i;
    }

    private static void swap(int[] list, int a, int b){
        int temp = list[a];
        list[a] = list[b];
        list[b] = temp;
    }
}
