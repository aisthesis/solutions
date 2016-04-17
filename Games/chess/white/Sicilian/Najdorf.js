/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';
  var repertoire = {
    '1.e4,c5 2.Nf3,d6 3.d4,cd4: 4.Nd4:,Nf6 5.Nc3,a6 6.Bc4,e6 7.Bb3': {
      'notes': 'Lipnitzky attack (6.Bc4)',
      '7..b5': {
        'Fischer_Tal1959': ['Fischer60:17'],
        'Kasparov_Gelfand1991': []
      },
      '7..Nbd7': {
        'Fischer_Bednarski1966': ['Fischer60:55']
      },
      '7..Be7': {
        'Rublevsky_Ivanchuk2007': ['MyFavorites.png']
      },
      '7..Nc6': {
        'Short_Kasparov1993': []
      },
    }
  };

  console.log(repertoire);
  return  repertoire;
})();
