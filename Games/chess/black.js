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
            '3.Bb5': 'Spanish',
            '3.Bc4': 'Italian'
          }
        },
        '2.Nc3': {},
        '2.Bc4': 'BishopsOpening'
      }
    },
    '1.d4': {
      '1..Nf6': {
        '2.c4': {},
        '2.Bg5': 'Trompovsky',
        '2.g3': 'QueensPawnGame'
      }
    },
    '1.c4': {
      '1..Nf6': {}
    },
    '1.Nf3': {
      '1..Nf6': {}
    }
  };
  return repertoire;
})();
