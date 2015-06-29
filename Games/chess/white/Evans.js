/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    "1.e4,e5 2.Nf3,Nc6 3.Bc4,Bc5 4.b4": {
      "4..Bb4: 5.c3": {
        "5..Ba5 6.d4": {
          "6..d6": "LaskerDefence",
          "6..ed4: 7.O-O": {
            "7..dc3": "CompromisedDefence",
            "7..Bb6 8.cd4:,d6": "NormalVariation",
            "7..d6 8.Qb3": "WallerAttack" 
          }
        },
        "5..Be7": {}
      },
      "ref": "http://www.masterchessopenings.com/c51-c52-evans-gambit.html"
    }
  };
  console.log(repertoire);
  return  repertoire;
})();
