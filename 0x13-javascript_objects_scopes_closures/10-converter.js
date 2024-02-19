#!/usr/bin/node
// export a num to base 10
exports.converter = function (number, base) 
// Define char to represent digits beyond 9
const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
// initialize result as an empty string
const result = '';
// perform conversion
while (number > 0) {
const remainder = number % base;
result = digits[remainder] + result;
	
// update for next iteration
number = Math.floor(number / base);
}
// return converted number
 return result || '0';
};
