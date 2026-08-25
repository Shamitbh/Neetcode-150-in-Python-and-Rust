/// 271. Encode and Decode Strings
/// Difficulty: Medium
/// Topics: Array, String, Design
/// https://leetcode.com/problems/encode-and-decode-strings/

fn main() {

    /// Encodes a list of strings to a single string.
    fn encode(strs: Vec<String>) -> String {
        let mut output = String::new();

        for word in strs {
            output.push_str(&word.len().to_string());
            output.push('#');
            output.push_str(&word);
        }

        output
    }
	
    /// Decodes a single string to a list of strings.
    fn decode(s: String) -> Vec<String> {
        let mut result = Vec::new();
        let mut i = 0;

        while i < s.len() {
            let mut j = i;

            while s.as_bytes()[j] != b'#' {
                j += 1;
            }

            // now we hit the delimiter
            let word_len: usize = s[i..j].parse().unwrap();

            let start_word_idx = j + 1;
            let end_word_idx = start_word_idx + word_len;

            let word = s[start_word_idx..end_word_idx].to_string();
            result.push(word);

            i = end_word_idx;
        }

        result
    }


    // Test cases
    let case_1 = vec!["Hello".to_string(), "World".to_string()];
    let case_1_encoded = encode(case_1.clone());
    let case_1_decoded = decode(case_1_encoded);

    let case_2 = vec!["".to_string()];
    let case_2_encoded = encode(case_2.clone());
    let case_2_decoded = decode(case_2_encoded);
    
    assert_eq!(case_1, case_1_decoded);
    assert_eq!(case_2, case_2_decoded);
    
    println!("All tests passed successfully!");
}