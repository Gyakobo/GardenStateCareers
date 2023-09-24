leetcode = {
    "2Sum": {
        "name": "Two Sum",
        "description": '''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.''',
        "example": [
            "Input: nums = [2,7,11,15], target = 9",
            "Output: [0,1]",
            "Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."
        ],
        "parameters": [2, 7, 11, 15],
        "answer": 9
    },

    "long_sub": {
        "name": "Longest Substring Without Repeating Characters",
        "description": '''Given a string s, find the length of the longest substring without repeating characters.''',
        "example": [
            "Input: s = 'abcabcbb'",
            "Output: 3",
            "Explanation: The answer is 'abc', with the length of 3."
        ],
        "parameters": "abcabcbb",
        "answer": 3
    },

    "long_palin": {
        "name": "Longest Palindromic Substring",
        "description": "Given a string s, return the longest palindromic substring in s.",
        "example": [
            "Input: s = 'babad'",
            "Output: 'bab'"
            "Explanation: 'aba' is also a valid answer."
        ],
        "parameters": "babad",
        "answer": "bab"
    },

    "water_container": {
        "name": "Container With Most Water",
        "description": '''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.''',
        "example": [
            "Input: height = [1,8,6,2,5,4,8,3,7]",
            "Output: 49"
            "Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49."
        ],
        "parameters": [1,8,6,2,5,4,8,3,7],
        "answer": 49
    }


}





