import Data.List
import qualified Data.Char as Char

main = do
    line <- getLine
    let ans = panagram line ['a'..'z']

    -- silly workaround for HackerRank; 
    -- didn't want quote marks
    case ans of 
        True -> putStrLn $ id "pangram"
        False -> putStrLn $ id "not pangram"

-- check for intersections between given string and alphabet
panagram xs ys = null $ ys \\ (map Char.toLower xs)
