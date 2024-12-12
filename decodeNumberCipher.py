import enchant
from itertools import product

def number_to_letter(number):
    """
    Convert a number to a corresponding letter.
    1 = A, 2 = B, ..., 26 = Z.
    """
    if 1 <= number <= 26:
        return chr(number + 64)  # ASCII mapping for letters A-Z
    return ""  # Invalid numbers return empty

def decode_sequence(sequence):
    """
    Decode a numeric sequence into possible letter combinations.
    """
    results = []

    def backtrack(index, path):
        # If we've reached the end of the sequence, store the result
        if index == len(sequence):
            results.append("".join(path))
            return

        # Try one digit
        if index < len(sequence):
            one_digit = int(sequence[index])
            letter = number_to_letter(one_digit)
            if letter:
                backtrack(index + 1, path + [letter])

        # Try two digits
        if index + 1 < len(sequence):
            two_digits = int(sequence[index:index + 2])
            letter = number_to_letter(two_digits)
            if letter:
                backtrack(index + 2, path + [letter])

    backtrack(0, [])
    return results

def filter_valid_words(decoded_combinations):
    """
    Filter decoded combinations to return only valid English words.
    """
    dictionary = enchant.Dict("en_US")
    valid_words = [word for word in decoded_combinations if dictionary.check(word)]
    return valid_words

def refine_with_suggestions(sequence, decoded_combinations):
    """
    Use enchant to refine ambiguous or partial decoded combinations by leveraging suggestions.
    """
    dictionary = enchant.Dict("en_US")
    suggestions = []

    for word in decoded_combinations:
        if dictionary.check(word):
            suggestions.append(word)
        else:
            # Add the top suggestions for partial matches
            suggestions.extend(dictionary.suggest(word)[:3])  # Take top 3 suggestions

    # Deduplicate and return refined suggestions
    return list(set(suggestions))

def fallback_decoding(sequence):
    """
    Attempt a brute-force decoding of sequences that failed initial processing.
    """
    results = decode_sequence(sequence)
    refined_results = refine_with_suggestions(sequence, results)
    return refined_results if refined_results else results

def analyze_group(group, group_index):
    """
    Analyze a single group, attempting to decode it and handle ambiguities.
    """
    decoded_combinations = decode_sequence(group)
    valid_combinations = filter_valid_words(decoded_combinations)

    if not valid_combinations:
        valid_combinations = fallback_decoding(group)

    print(f"Group {group_index + 1} ({group}):")
    print(f"  Decoded Combinations: {decoded_combinations}")
    print(f"  Valid Words: {valid_combinations}")
    return valid_combinations

def decipher(input_string):
    """
    Decipher the entire input string, splitting into words by spaces.
    """
    groups = input_string.split(" ")  # Split input by spaces
    decoded_words = []

    for i, group in enumerate(groups):
        decoded_words.append(analyze_group(group, i))

    return decoded_words

def generate_sentences(decoded_output):
    """
    Generate possible sentences using the decoded words from all groups.
    """
    # Filter out empty groups
    non_empty_groups = [group for group in decoded_output if group]

    # Generate all combinations of words from groups
    all_combinations = list(product(*non_empty_groups))

    # Combine each combination into a sentence
    sentences = [" ".join(combination) for combination in all_combinations]

    # Filter out sentences that are not meaningful
    valid_sentences = []
    dictionary = enchant.Dict("en_US")
    
    for sentence in sentences:
        words = sentence.split()
        if all(dictionary.check(word) for word in words):  # Ensure all words are valid
            valid_sentences.append(sentence)

    return valid_sentences

# Input puzzle sequence
input_sequence = "9 426137 2015 22137229 2085 141811 9142051814198916"

# Decipher the sequence
decoded_output = decipher(input_sequence)

# Generate and print possible valid sentences
valid_sentences = generate_sentences(decoded_output)
print("\nValid English Sentences:")
for sentence in valid_sentences:
    print(sentence)
