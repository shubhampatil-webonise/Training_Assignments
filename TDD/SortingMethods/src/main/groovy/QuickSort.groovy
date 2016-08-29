/**
 * Created by webonise on 29/8/16.
 */
class QuickSort implements SortingMethod {

    def sort(array){
        return quicksort(array);
    }

    def quicksort(array){

        if ( array.size() < 2)
            return  array

        def pivot = array[array.size().intdiv(2)];

        def left = array.findAll {item -> item < pivot};
        def middle = array.findAll {item -> item == pivot};
        def right = array.findAll {item -> item > pivot};

        return (quicksort(left) + middle + quicksort(right))
    }
}
