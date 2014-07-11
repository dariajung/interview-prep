helper n _ [] i = i
helper n globalIndex (x:xs) i 
    | n == x    = helper n (globalIndex + 1) xs (globalIndex)
    | otherwise = helper n (globalIndex + 1) xs i

lastIndexOf n arr = helper n 0 arr (-1)
