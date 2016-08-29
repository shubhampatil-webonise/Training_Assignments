/**
 * Created by webonise on 29/8/16.
 */
class SortingHandler {
    static void main(String[] args){
        SortingMethod quick = new QuickSort();
        def sorted_array = quick.sort([2, 1, 3]);
        println("1 " + sorted_array);

        SortingMethod merge = new MergeSort();
        merge.sort([2, 1, 3]);
        println("2 " + sorted_array);
    }
}
