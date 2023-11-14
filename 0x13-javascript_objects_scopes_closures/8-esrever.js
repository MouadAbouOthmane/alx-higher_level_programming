#!/usr/bin/node
exports.esrever = function (list) {
  const ls = [];
  const len = list.length - 1;

  list.forEach((element, i) => {
    ls[len - i] = element;
  });

  return ls;
};
