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
            '3.Bc4': 'Italian',
            '3.c3': 'Ponziani'
          }
        },
        '2.Nc3': {},
        '2.Bc4': 'BishopsOpening',
        '2.f4': 'KingsGambit'
      }
    },
    '1.d4': {
      '1..Nf6': {
        '2.c4': {
         '2..c5': {
           '3.d5,e6': 'ModernBenoni'
         },
         '2..g6': 'KingsIndian'
        },
        '2.Bg5': 'Trompovsky',
        '2.g3': 'QueensPawnGame'
      }
    },
    '1.c4': {
      '1..Nf6': {
        '2.Nc3': {
          '2..g6': {
            '3.g3': 'English',
            '3.d4': 'KingsIndian'
          }
        }
      }
    },
    '1.Nf3': {
      '1..Nf6': {}
    }
  };
  console.log(repertoire);
  return repertoire;
})();
