#!/usr/bin/node
// export a num to base 10
exports.converter = function () {
  return Array.from(arguments).reduce(function (result, arg) {
    while (arg > 0) {
      const remainder = arg % arguments[1];
      result = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[remainder] + result;
      arg = Math.floor(arg / arguments[1]);
    }
    return result || '0';
  }, '');
};
