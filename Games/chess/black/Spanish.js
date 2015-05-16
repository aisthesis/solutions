/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,e5 2.Nf3,Nc6 3.Bb5,a6': {
      '4.Bc6:,dc6:': 'Exchange',
      '4.Ba5,Nf6 5.0-0': {
        '5..Bc5': 'Moller'
      }
    }
  };
  console.log(repertoire);
  return  repertoire;
})();
