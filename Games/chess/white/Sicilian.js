/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';
  var repertoire = {
    '1.e4,c5 2.Nf3': {
      '2..d6 3.d4,cd4: 4.Nd4:,Nf6 5.Nc3': {
        '5..Nc6 6.Bc4': 'Sozin',
        '5..a6': 'Najdorf',
        '5..g6': 'Dragon',
        '5..e6': 'Scheveningen'
      },
      '2..Nc6 3.d4,cd4: 4.Nd4:': {
        '4..Nf6 5.Nc3': {
          '5..e5': 'Sveshnikov',
          '5..d6 6.Bc4': 'Sozin',
        },
        '4..e6 5.Nb5': 'Szen',
        '4..g6 5.Nc3': 'DragonAcc'
      },
      '2..e6 3.d4,cd4: 4.Nd4:,Nc6 5.Nb5': 'Szen',
    }
  };

  console.log(repertoire);
  return  repertoire;
})();
