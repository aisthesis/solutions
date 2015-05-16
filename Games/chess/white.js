/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';
  var repertoire = {
    '1.e4': {
      '1..e5': {
        '2.Nf3': {
          '2..Nc6': {
            '3.Bb5': 'Spanish'
          },
          '2..Nf6': 'Russian',
          '2..d6': 'Philidor'
        }
      },
      '1..c5': 'Sicilian',
      '1..e6': 'French',
      '1..c6': 'Caro-Kann',
      '1..Nf6': 'Alekhine'
    }
  };

  console.log(repertoire);
  return  repertoire;
})();
