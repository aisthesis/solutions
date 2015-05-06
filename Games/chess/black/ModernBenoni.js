/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.d4,Nf6 2.c4,c5 3.d5,e6 4.Nc3,ed5: 5. cd5:,d6': {
      '6.e4,g6': {
        '7.Nf3,Bg7': {
          '8.Be2,0-0 9.0-0': 'Classical',
          '8.h3,0-0 9.Bd3': 'Modern'
        },
        '7.f4': 'TaimanovAttack',
        '7.Bd3': 'Knaak',
        '7.f3': 'Kapengut'
      },
      '6.Nf3,g6': {}
    }
  };
  return repertoire;
})();
