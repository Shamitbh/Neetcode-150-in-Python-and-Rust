use std::collections::HashSet;
fn main() {
    fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut unique_nums: HashSet<i32> = HashSet::new();
        for num in nums {
            if unique_nums.contains(&num) {
                return true
            }
            unique_nums.insert(num);
        }
        false
    }
    
    // Test cases
    let case_1 = vec!(1, 2, 3, 1);
    let case_2 = vec!(1, 2, 3, 4);
    let case_3 = vec!(1, 1, 1, 3, 3, 4, 3, 2, 4, 2);
    
    assert_eq!(contains_duplicate(case_1), true);
    assert_eq!(contains_duplicate(case_2), false);
    assert_eq!(contains_duplicate(case_3), true);
    
    println!("All tests passed successfully!");
}