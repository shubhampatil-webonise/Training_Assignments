/**
 * Created by shubham on 4/9/16.
 */
class MainHandler {
    static void main(String[] args){
        SortingMethod sortingMethod = new MergeSort();
        println(sortingMethod.sort([1, 3, 2]));
    }
}
