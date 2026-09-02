/// 49. Group Anagrams
/// Difficulty: Medium
/// Topics: Array, Hash Table, String, Sorting
/// https://leetcode.com/problems/group-anagrams/

use std::collections::HashMap;
fn main() {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut char_count_map: HashMap<[u8; 26], Vec<String>> = HashMap::new();
        
        // loop through strs
        for word in strs {
            let char_count_of_word = find_char_count_of_word(&word);
            char_count_map.entry(char_count_of_word)
                .or_insert_with(Vec::new)
                .push(word);
        }

        /// Given a word, finds character count of each letter in word
        /// puts it into char_count_array, and returns it
        fn find_char_count_of_word(word: &str) -> [u8; 26] {
            let mut char_count_array = [0; 26];
            for ch in word.chars() {
                char_count_array[(ch as usize) - ('a' as usize)] += 1;
            }
            char_count_array
        }

        let mut result = Vec::new();
        for anagram in char_count_map.values() {
            result.push(anagram.to_vec());
        }
        result
    }

    // Test cases
    let case_1_input = vec!["eat","tea","tan","ate","nat","bat"].into_iter()
        .map(String::from)
        .collect();
    let mut case_1_output: Vec<Vec<String>> = vec![vec!["eat".to_string(),"tea".to_string(),"ate".to_string()],
    vec!["tan".to_string(),"nat".to_string()],
    vec!["bat".to_string()]];

    let case_2_input = vec!["".to_string()];
    let mut case_2_output: Vec<Vec<String>> = vec![vec!["".to_string()]];

    let case_3_input = vec!["a".to_string()];
    let mut case_3_output: Vec<Vec<String>> = vec![vec!["a".to_string()]];
    
    assert_eq!(group_anagrams(case_1_input).sort(), case_1_output.sort());
    assert_eq!(group_anagrams(case_2_input).sort(), case_2_output.sort());
    assert_eq!(group_anagrams(case_3_input).sort(), case_3_output.sort());
    
    println!("All tests passed successfully!");
}