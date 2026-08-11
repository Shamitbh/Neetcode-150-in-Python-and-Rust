/// 347. Top K Frequent Elements
/// Difficulty: Medium
/// Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
/// https://leetcode.com/problems/top-k-frequent-elements/

use std::collections::{BinaryHeap, HashMap};
fn main() {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        
        let mut freq_map: HashMap<i32, i32> = HashMap::new();
        for num in nums.clone() {
            *freq_map.entry(num).or_insert(0) += 1;
        }
        
        // min heap
        let mut heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        
        for (num, count) in freq_map {
            heap.push((count * -1, num));
            if heap.len() as i32 > k {
                heap.pop();
            }
        }
        
        let mut res = Vec::new();
        for (_, num) in heap {
            res.push(num);
        }
        
        res
    }

    // Test cases
    let case_1_nums = vec![1,1,1,2,2,3];
    let case_1_k = 2;
    let mut case_1_output = vec![2, 1];
    
    let case_2_nums = vec![1];
    let case_2_k = 2;
    let mut case_2_output = vec![1];
    
    let case_3_nums = vec![1,2,1,2,1,2,3,1,3,2];
    let case_3_k = 2;
    let mut case_3_output = vec![1, 2];
    
    assert_eq!(top_k_frequent(case_1_nums, case_1_k).sort(), case_1_output.sort());
    assert_eq!(top_k_frequent(case_2_nums, case_2_k).sort(), case_2_output.sort());
    assert_eq!(top_k_frequent(case_3_nums, case_3_k).sort(), case_3_output.sort());

    println!("All tests passed successfully!");
}