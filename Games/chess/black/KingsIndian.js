/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.d4,Nf6 2.c4,g6': {
      '3.Nf3,Bg7 4.g3': 'Fianchetto',
      '3.Nc3,Bg7 4.e4,d6': {
        '5.Nf3,0-0 6.Be2,e5': 'Classical',
        '5.f3': 'Sämisch',
        '5.Be2,0-0 6.Bg5': 'Averbakh',
        '5.f4': 'FourPawns'
      }
    }
  };
  return repertoire;
})();
