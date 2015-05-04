/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    'white': {
      '1.e4': {
        '1..e5': {
          'variations': {
            '2.Nf3': {
              '2..Nc6': {}
            },
            '2.Nc3': {
              '2..Nf6': {}
            },
            '2.Bc4': {
              '2..Nf6': {}
            },
            '2.d4': {}
        },
        '1..c5': {
          'name': 'Sicilian',
          'variations': {}
        },
        '1..e6': {
          'name': 'French',
          'variations': {}
        },
        '1..c6': {
          'name': 'Caro-Kann',
          'variations': {}
        }
      }
    },
    'black': {
      '1.e4': {
        '1..e5': {}
      },
      '1.d4': {
        '1..Nf6': {}
      },
      '1.c4': {
        '1..Nf6': {}
      },
      '1.Nf3': {
        '1..Nf6': {}
      }
    }
  };
  return  repertoire;
})();
