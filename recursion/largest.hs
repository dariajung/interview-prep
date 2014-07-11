max' :: [Int] -> Int -> Int
max' [] n = n
max' (x:xs) n 
    | x > n     = max' xs x
    | otherwise = max' xs n
