import re


def count_patterns(pattern, text, weight):
    """Count the occurrences of a pattern in a text and return the weighted score."""
    return sum(len(match) for match in re.findall(pattern, text)) * weight


def count_sequences(sequence_length, text, weight):
    """Count the occurrences of ascending or descending sequences of a specific length in a text and return the weighted score."""
    count = 0
    for i in range(len(text) - sequence_length + 1):
        subseq = text[i:i+sequence_length]
        if subseq in '0123456789012' or subseq in '9876543210987':
            count += 1
    return count * weight


def count_palindromes(text, weight):
    """Count the palindromes in a text and return the weighted score."""
    return sum(text[i] == text[-(i + 1)] for i in range(len(text) // 2)) * weight


def calculate_pattern_scores(number, weights):
    """Calculate the pattern scores using the given weights."""
    return {
        'repeated_patterns': count_patterns(r'(\d)\1{2,}', number, weights['repeated_patterns']),
        'sequence_patterns': count_sequences(4, number, weights['sequence_patterns']),
        'alternating_patterns': count_patterns(r'(\d\d)\1{1,}', number, weights['alternating_patterns']),
        'palindrome_patterns': count_palindromes(number, weights['palindrome_patterns']),
        'repeated_8s': count_patterns(r'(8)\1{2,}', number, weights['repeated_8s'])
    }


def memorability_score(number):
    """Calculate the memorability score for a given number."""
    # Remove the first three characters (the three 8s)
    number = number[3:]

    # Define the weights for each pattern type
    weights = {
        'repeated_patterns': 2,
        'sequence_patterns': 1,
        'alternating_patterns': 2,
        'palindrome_patterns': 1,
        'repeated_8s': 1
    }

    # Calculate the pattern scores
    pattern_scores = calculate_pattern_scores(number, weights)

    # Calculate the total pattern score
    total_patterns_score = sum(pattern_scores.values())

    # Find the maximum weight
    total_weight = max(weights.values())

    # Normalize the score to a range of 0 to 1
    score = total_patterns_score / (len(number) * total_weight)

    return min(score, 1)
