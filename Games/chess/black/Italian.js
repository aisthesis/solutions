/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,e5 2.Nf3,Nc6 3.Bc4': {
      '3..Bc5': {
        '4.b4': 'EvansGambit',
        '4.c3': 'GiuocoPiano',
        '4.d3': 'GiuocoPianissimo',
        '4.Nc3': {
          '4..d6': {
            '5.d3': 'GiuocoPianissimo'
          }
        },
        '4.0-0': {
          '4..d6': {
            '5.c3': 'GiuocoPiano',
            '5.d3': 'GiuocoPianissimo'
          }
        }
      }
    }
  };
  return  repertoire;
})();
