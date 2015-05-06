/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,e5 2.Nf3,d6': {
      '3.d4': {
        '3..Bg4': {
          'Morphy_BrunswickIsouard1858': ['https://youtu.be/vFnY77FmSeU']
        },
        '3..ed4:': {
          '4.Bc4': {
            'Morphy_Barnes1858': ['http://www.365chess.com/view_game.php?g=2689046'],
            'Morphy_Sicre1864': ['http://www.365chess.com/view_game.php?g=2689879']
          },
          '4.Qd4:': {
            'Morphy_Loewenthal1858': ['http://www.365chess.com/view_game.php?g=2689151'],
            'Morphy_Harrwitz1858': ['http://www.365chess.com/view_game.php?g=2689123'],
            'Morphy_Mongredien1859': ['http://www.365chess.com/view_game.php?g=2689336']
          },
          '4.Nd4:': {
            'Morphy_Seguin1858': ['http://www.365chess.com/view_game.php?g=2689140']
          }
        }
      }
    }
  };
  return  repertoire;
})();
