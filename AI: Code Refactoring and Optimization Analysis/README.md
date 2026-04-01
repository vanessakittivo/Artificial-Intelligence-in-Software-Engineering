# AI: Code Refactoring and Optimization Analysis

## 📋 Task Description

This task involved refactoring a C function called `print_to_98` that prints all natural numbers from a given starting point to 98. The original code worked but had several issues:
- It used `printf` which was not allowed in the project requirements
- The formatting had Betty style warnings (function too long, improper indentation)
- The logic was overly complex with nested conditionals

The goal was to use AI assistance to:
1. Convert the function to use only `_putchar` (project requirement)
2. Fix Betty style violations
3. Simplify the logic while maintaining the same output

## 🤖 AI Tool Used

**Gemini** (via Google AI Studio)

I used Gemini because it provides clear, step-by-step explanations and follows C coding standards well.

## 📂 Files in This Task

| File | Description |
|------|-------------|
| [Initial Code](./initial_code.c) | My original implementation that compiled but failed Betty style checks |
| [Final Code](./final_code.c) | AI-refactored version using only `_putchar` with proper Betty compliance |
| [AI Conversation](./prompts/ai_conversation.png) | Screenshot of my interaction with Gemini |

## 🔍 Key Improvements Made

### Before (Initial Code)
```c
// Used printf (not allowed by project requirements)
void print_to_98(int n)
{
    int i;
    if (n <= 98) {
        for (i = n; i <= 98; i++) {
            if (i != n) printf(", ");
            printf("%d", i);
        }
    } else {
        // ... similar logic
    }
}

### After (AI-Refactored Code)

// Uses only _putchar (project-compliant)
void print_to_98(int n)
{
    int i;
    if (n <= 98)
    {
        for (i = n; i <= 98; i++)
        {
            if (i != n)
            {
                _putchar(',');
                _putchar(' ');
            }
            print_number(i);
        }
    }
    // ... helper function for multi-digit numbers
}

💬 My Prompt to the AI
"I have a C function print_to_98 that prints numbers from n to 98. My project requires that I only use _putchar for output, not printf. Also, I'm getting Betty style warnings about the function being too long. Can you help me refactor this to meet the requirements while keeping the same output format?"

✨ Lessons Learned
Breaking down problems - The AI suggested creating a helper function print_number() to handle multi-digit numbers

Betty style - Learned that functions should be ≤ 40 lines and use proper indentation

Project compliance - Understanding constraints (like only using _putchar) leads to better design

📊 Before vs After Comparison
Metric	Initial Code	Final Code
Output function	printf	_putchar (project compliant)
Function length	56 lines	38 lines
Betty warnings	7 warnings	0 warnings
Helper functions	0	1 (print_number)
Handles multi-digit	✅ (via printf)	✅ (custom logic)
🔗 Related Resources
Betty Coding Style Documentation

C _putchar function reference
