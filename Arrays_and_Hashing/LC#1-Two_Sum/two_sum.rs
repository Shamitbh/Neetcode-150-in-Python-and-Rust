/// 1. Two Sum
/// Difficulty: Easy
/// Topics: Junior, Array, Hash Table
/// https://leetcode.com/problems/two-sum/description/

use std::collections::HashMap;
fn main() {
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut index_map = HashMap::new();

        for (i, num) in nums.into_iter().enumerate() {
            let difference = target - num;
            if let Some(difference_indx) = index_map.get(&difference) {
                return vec![i as i32, *difference_indx];
            }
            index_map.insert(num, i as i32);
        }
        unreachable!("will always find a solution above")
    }

    // Test cases
    let case_1_nums = vec![2, 7, 11, 15];
    let case_1_target = 9;

    let case_2_nums = vec![3, 2, 4];
    let case_2_target = 6;

    let case_3_nums = vec![3, 3];
    let case_3_target = 6;
    
    assert_eq!(two_sum(case_1_nums, case_1_target), vec![1, 0]);
    assert_eq!(two_sum(case_2_nums, case_2_target), vec![2, 1]);
    assert_eq!(two_sum(case_3_nums, case_3_target), vec![1, 0]);
    
    println!("All tests passed successfully!");
}