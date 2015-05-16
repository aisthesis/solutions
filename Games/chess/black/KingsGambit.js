/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,e5 2.f4': {
      '2..ef4:': {
        '3.Nf3': {
          '3..d6': 'FischerDefense'
        },
        '3.Bc4': {}
      },
      '2..d5': 'Falkbeer'
    }
  };
  console.log(repertoire);
  return  repertoire;
})();
