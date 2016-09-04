/**
 * Created by shubham on 4/9/16.
 */
class MergeSort implements SortingMethod {
    def sort(array){

        if(! (array instanceof ArrayList)){
            throw new Exception();
        }

        array.each {
            arrayElement ->
                if(!(arrayElement instanceof Integer || arrayElement instanceof BigDecimal))
                    throw new Exception()
        }

        if(array.size() <= 1) {
            return array;
        }else {

            def center = array.size()/2;
            def left = array[0..center-1];
            def right = array[center..array.size()-1]

            return merge(sort(left), sort(right));
        }
    }

    def merge(left, right){

        def merged = [];

        while(left.size() > 0 && right.size() > 0){
            if(left.get(0) <= right.get(0)){
                merged << left.remove(0);
            }else {
                merged << right.remove(0);
            }
        }

        merged = merged + left + right;
        return merged;
    }
}
