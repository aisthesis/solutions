/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    "1.e4,e5 2.Nf3,Nc6 3.Bb5, Nf6": {
      "4.0-0,Ne4: 5.d4": {
        "5..Nd6": {
          "Fischer_Fuller1963": ["http://www.365chess.com/view_game.php?g=2573670]
        },
        "5..a6": "BerlinRosenthal",
        "5..Be7 6.Qe2,Nd6 7.Bc6:,bc6: 8.de5:,Nb7 9.Nd4": {
          "name": "BerlinWinawer",
          "sources": ["http://www.365chess.com/eco/C67_Ruy_Lopez_Berlin_defence_Winawer_attack"]
        }
      },
      "4.d4": {
        "Morphy_Anderssen1858": ["http://www.365chess.com/view_game.php?g=2689202"],
        "Tal_Furman1958": ["http://www.365chess.com/view_game.php?g=2541034"]
      }
    }
  };
  return  repertoire;
})();
