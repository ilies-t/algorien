# Algorien
Simple algorithm to get the similarity between two string implemented on Python and Javascript, based on Levenshtein and Hamming distance
* [Python](python/algorien.py)
* [Javascript](javascript/algorien.mjs)

## Examples
### Python
```python
#!/usr/bin/python3

from algorien import Algorien

result = Algorien.search('Fayrefox', 'Firefox')
print(result)
# expected output: 42.86

result = Algorien.search('Fairefokse', 'Firefox')
print(result)
# expected output: 7.14
```
### Javascript
```js
const Algorien = require('algorien');

let result = Algorien.search('Netflixe', 'Netflix');
console.log(result);
// expected output: 53.85

result = Algorien.search('Naitefliks', 'Netflix');
console.log(result);
// expected output: 7.69
```

## Notes
Based on Levenshtein distance</br>
https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm</br>
And Hamming distance</br>
https://leetcode.com/problems/hamming-distance/

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
