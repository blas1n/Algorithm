SELECT
    user_id,
    COUNT(prompt) as prompt_count,
    ROUND(AVG(tokens), 2) as avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(prompt) >= 3 AND MAX(tokens) > AVG(tokens)
ORDER BY AVG(tokens) DESC