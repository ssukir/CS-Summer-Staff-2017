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
    if(c.charCodeAt() + n <= 'Z'.charCodeAt()) {
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
