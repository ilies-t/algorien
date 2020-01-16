/*
  Algorien v0.0.1
  Project: https://github.com/ilies-t/algorien
  Author: ilies t <https://github.com/ilies-t>
  License: Apache License 2.0
*/

var algorien = {
	// create array with spliten caracters and add previous caracters for each loop
	splitIncr: splitIncr = (a) => {
        // split with each caracters
        const arr = a.toLowerCase().split(''), finalArray = [];
        let item = '';

        /* example with 'beach'
        * will become -> ['b', 'be', 'bea', 'beac', 'beach',
        *          		  'h', 'hc', 'hca', 'hcae', 'hcaeb']
        * also, to avoid space problem, add a condition
        */
        for(let x = 0; x < 2; x++) {
            for(let i = 0; i < arr.length; i++) {
                if(arr[i] !== undefined) {
                    item += arr[i];
                    finalArray.push(item);
               }
           }
           // same but with reversed array
           item = ''; arr.reverse();
        }
        return finalArray;
	},
	// split word and referrence into array with splitIncr()
	search: search = (word, referrence) => {
        const wordArr = splitIncr(word),
            referenceArr = splitIncr(referrence);
        let pct = 0;

        // compare and add 1 into pct if items are similars
        wordArr.forEach(item => {
            if(referenceArr.includes(item)) pct++;
        });
        // calculate the part of char present in reference array
        pct /= (referenceArr.length - 1);

        // round and return a real percentage
        return +(Math.round((pct * 100) + "e+2")  + "e-2");
	}
};
