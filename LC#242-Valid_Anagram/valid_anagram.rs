/// 242. Valid Anagram
/// Difficulty: Easy
/// Topics: Hash Table, String, Sorting
/// https://leetcode.com/problems/valid-anagram/

fn main() {
    fn valid_anagram(s: String, t: String) -> bool {
        let mut char_count: [i32; 26] = [0; 26];
        if s.len() != t.len() {
            return false
        }

        for (&s_byte, &t_byte) in s.as_bytes().iter().zip(t.as_bytes().iter()) {
            char_count[(s_byte - b'a') as usize] += 1;
            char_count[(t_byte - b'a') as usize] -= 1;
        }

        char_count.iter().all(|&freq| freq == 0)
    }
    
    // Test cases
    let case_1_s = "anagram".to_string();
    let case_1_t = "nagaram".to_string();

    let case_2_s = "rat".to_string();
    let case_2_t = "car".to_string();
    
    assert_eq!(valid_anagram(case_1_s, case_1_t), true);
    assert_eq!(valid_anagram(case_2_s, case_2_t), false);
    
    println!("All tests passed successfully!");
}