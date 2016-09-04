import java.awt.List
import java.lang.reflect.Array

/**
 * Created by shubham on 4/9/16.
 */
class QuickSort implements SortingMethod {
    def sort(array){

        if(! (array instanceof ArrayList)){
            throw new Exception();
        }

        array.each {
            arrayElement ->
                if(!(arrayElement instanceof Integer || arrayElement instanceof BigDecimal))
                    throw new Exception()
        }

        if (array.size() < 2)
            return array

        def pivot = array[array.size().intdiv(2)];

        def left = array.findAll {item -> item < pivot};
        def middle = array.findAll {item -> item == pivot};
        def right = array.findAll {item -> item > pivot};

        return (sort(left) + middle + sort(right));
    }
}
