#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  list.forEach((item) => item === searchElement ? nb++ : null);
  return nb;
};
