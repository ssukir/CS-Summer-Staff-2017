// decipher

// example criteria for "most English"
function letterScore(letter) {
  // letterScore returns the scrabble score of the string letter
  // 'aeilnorstu'.indexOf(let) > -1 is the JS equivalent of letter in 'aeilnorstu' in Python
  if ('aeilnorstu'.indexOf(letter) > -1) {
    return 1;
  }
  else if ('dg'.indexOf(letter) > -1) {
    return 2;
  }
  else if ('bcmp'.indexOf(letter) > -1) {
    return 3;
  }
  else if ('fhvwy'.indexOf(letter) > -1) {
    return 4;
  }
  else if ('k'.indexOf(letter) > -1) {
    return 5;
  }
  else if ('jx'.indexOf(letter) > -1) {
    return 8;
  }
  else if ('qz'.indexOf(letter) > -1) {
    return 10;
  }
  else {
    return 0;
  }
}

function scrabbleScore(S) {
  // outputs the int scrabbleScore of a string S
  // S.slice(1) is the JS equivalent of S[1:] in Python
  if (S !== '') {
    return letterScore(S[0]) + scrabbleScore(S.slice(1));
  }
  else {
    return 0;
  }
}

function decipher(S) {
  // takes in a string and outputs a "translated" string, that has been decoded into the most "English"
  var L;
  for (var n = 0; n <= 26; n++) {
    L[n] = encipher(S, n);
  }
  var LOL;
  var length = L.length;
  //JS does not have tuples! use alternative logic
  for (var x; x < length; x++){
    LOL[x] = scrabbleScore(x);
  }
  var LOLmin = LOL.min();
  var minIndex = LOL.indexOf(LOLmin);
  var translation = L[minIndex];
}

// encipher
function rot(c, n) {
  // rotates a single character c by int n spots in the alphabet
  if ('a'.charCodeAt() <= c.charCodeAt() <= 'z'.charCodeAt()) {
    // c.charCodeAt(0) is the JS equivalent of ord(c) in Python
    if (c.charCodeAt() + n <= 'z'.charCodeAt()) {
      // String.fromCharCode(0) is the JS equivalent of chr(0)
      return String.fromCharCode(c.charCodeAt() + n);
    }
    else {
      return String.fromCharCode(c.charCodeAt() + n - 26);
    }
  }
  else if ('A'.charCodeAt() <= c.charCodeAt() <= 'Z'.charCodeAt()) {
    if(c.charCodeAt() + n <= 'Z'.charCodeAt()){
      return String.fromCharCode(c.charCodeAt() + n);
    }
    else {
      return String.fromCharCode(c.charCodeAt() + n - 26);
    }
  }
  else {
    return c;
  }
}

function list_to_str(L) {
  // converts a list of characers L into a single string
  if (L.length === 0) {
    return '';
  }
  // L.slice(1:4) is the JS equivalent of L.slice[1:4] in Python
  return L[0] + list_to_str(L.slice(1));
}

function encipher(S, n) {
  // S.split("") is the JS equivalent of list(S) in Python
  // creates a list of each character in S
  var L = S.split("");
  var length = L.length;
  for (var c = 0; c < length; c++) {
    L[c] = rot(L[c], n);
  }
  return list_to_str(L);
}
