/**
 * Created by webonise on 29/8/16.
 */
class MergeSort implements SortingMethod {
    def sort(array){
        println("3" + array)
        println(array.size())
        mergesort(array, 0, array.size() - 1)
    }

    def mergesort(array, start, end){


        if (end > start){
            int middle = (int)((end+start)/2);

            mergesort(array, start, middle);
            mergesort(array, middle + 1, end);

            mergeArrays(array, start, middle, end);

            println(array);
        }
    }

    def mergeArrays(array, start, middle, end){

        def left_part = Arrays.copyOfRange(array, start, middle + 1 );
        def right_part = Arrays.copyOfRange(array, middle + 1, end + 1);

        int current_index = start, index_of_left = 0 , index_of_right = 0;

        while (index_of_left < left_part.length && index_of_right < right_part.length)
            array[current_index++] = (left_part[index_of_left] <= right_part[index_of_right]) ? left_part[index_of_left++] : right_part[index_of_right++];

        while (index_of_left < left_part.length)
            array[current_index++] = left_part[index_of_left++];

        while (index_of_right < right_part.length)
            array[current_index++] = right_part[index_of_right++];
    }
}
