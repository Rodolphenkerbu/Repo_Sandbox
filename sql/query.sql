SELECT category,
       COUNT(*)
FROM tickets
GROUP BY category;