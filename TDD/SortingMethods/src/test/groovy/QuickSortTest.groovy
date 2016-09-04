import spock.lang.Specification
import spock.lang.Unroll

/**
 * Created by shubham on 4/9/16.
 */
class QuickSortTest extends Specification{
    def SortingMethod sortingMethod

    def setup(){
        sortingMethod = new QuickSort();
    }

    def 'test something basic'(){
        expect:
        true;
    }

    @Unroll('in unroll : #array should raise exception')
    def 'should raise exception if input is not arraylist'(){
        when:
        sortingMethod.sort(array)

        then:
        thrown Exception

        where:
        array   |   _
        "abc"   |   _
        2       |   _
        true    |   _
        4.6     |   _
    }

    @Unroll('in unroll : #array should raise exception')
    def 'should raise exception if all elements in arraylist are not int'(){
        when:
        sortingMethod.sort(array)

        then:
        thrown Exception

        where:
        array           |   _
        [1, '2', 3]     |   _
        ['1+i', '2', 3] |   _
        [true, 2 , '1'] |   _
        [2.4, '2+i', 1] |   _
    }

    @Unroll('in unroll : Sorting #array should give #sortedArray')
    def 'the final showdown to test if sorting is working properly'(){
        when:
        def retValue = sortingMethod.sort(array)

        then:
        retValue == sortedArray

        where:
        array       |   sortedArray
        [1, 4, 2]   |   [1, 2, 4]
        [4, 21, 5]  |   [4, 5, 21]
        [3.5, 1, 4] |   [1, 3.5, 4]
    }
}

