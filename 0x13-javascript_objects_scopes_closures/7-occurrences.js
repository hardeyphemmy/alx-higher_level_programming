#!/usr/bin/node
// Return the number of occurrences in a list
exports.nbOccurrences = function (list, searchElement) {
	// initialize the variable to count
	let count = 0;
	// Loop throughh the list
	for (let i = 0; i < list.length; i ++) {
		// check if current element is equal to a search element
		if (list[i] === serachElement) {
			// Increment count
			count++;
		}
	}
	return count;
}
