/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    "1.e4,e5 2.Nf3,Nc6 3.Bb5": {
      "3..a6": {
        "4.Bc6:": "Exchange"
      },
      "3..Nf6": "BerlinDefence",
      "3..f5": "SchliemannDefence"
    }
  };
  return  repertoire;
})();
