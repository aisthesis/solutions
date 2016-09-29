/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,e5 2.Nf3,Nc6 3.Nc3,Nf6': {
      '4.Bb5': {
        'eco': 'C48',
        'name': 'FourKnightsSpanish',
        'Chajes_Capablanca1918': ['MyFavorites.pgn']
      },
      '4.d4': {
        'eco': 'C47',
        'name': 'FourKnightsScotch',
        '4..ed4:': {
          'Nakamura_Carlsen2014': ['MyFavorites.pgn'],
          'DeepBlue_Kasparov1996': []
        },
        '4..Bb4': {
          'name': 'Krause',
          'Paulsen_Morphy1857': ['MyFavorites.pgn']
        }
      }
    }
  };
  return  repertoire;
})();
