/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';
  /**
   * Only counting games class C and up from
   * 2015 on
   */
  var counts = {
    "Spanish": {
      "total": 6,
      "variations": {
        "Exchange": {
          "total": 2,
          "variations": {
            "Gligorich": {
              "total": 1,
              "games": [
                "aisthesis_KenGriffey20150514"
              ],
              "ref": [
                "Schallopp_Moll1907",
                "Schallopp_Przepiorka1907",
                "Fischer_Portisch1966",
                "Fischer_Gligorich1966",
                "Hort_Zelandinow1967",
                "Bagirov_Keres1967",
                "Hort_Gligoric1968",
                "Ljubojevic_Gligoric1979",
                "Ivanovic_Gligoric1990"
              ],
              "ECO": "C69"
            },
            "AlapinGambit": {
              "total": 1,
              "games": [
                "aisthesis_NikhilP20150424"
              ],
              "ECO": "C68"
            }
          }
        },
        "Graz": {
          "total": 1,
          "games": [
            "arkadas_aisthesis20150514"
          ],
          "ECO": "C70",
          "transposesTo": "Moeller"
        },
        "Moeller": {
          "total": 1,
          "games": [
            "jptwee_aisthesis20150523"
            ],
          "ref": [
            "Onischuk"
            ],
          "ECO": "C78"
        },
        "Nuernberg": {
          "total": 1,
          "games": [
            "aisthesis_Kingsman20150429"
          ],
          "ECO": "C60"
        },
        "OldSteinitz": {
          "total": 1,
          "games": [
            "aisthesis_elclandestino20150408"
          ],
          "ECO": "C62"
        },
        "Other": {
          "total": 1,
          "games": [
            "aisthesis_bigbalduck20150410"
          ],
          "ECO": "C60"
        }
      }
    },
    "Bishops": {
      "total": 3,
        "games": [
          "sekargnans_aisthesis20150410",
          "Kingsman_aisthesis20150501",
          "5chess1_aisthesis20150517"
        ],
        "ECO": "C24"
    },
    "Sicilian": {
      "total": 1,
      "variations": {
        "Sveshnikov": {
          "total": 1,
          "games": [
            "aisthesis_mib251_20150417"
          ],
          "ECO": "B33"
        }
      }
    },
    "Scotch": {
      "total": 0,
      "variations": {}
    },
    "Italian": {
      "total": 2,
      "variations": {
        "GiuocoPiano": {
          "total": 1,
          "games": [
            "elclandestino_aisthesis20150410"
          ],
          "ECO": "C50"
        },
        "EvansGambit": {
          "total": 1,
          "games": [
            "mismidad_aisthesis20150430"
          ],
          "ECO": "C52"
        }
      }
    },
    "Philidor": {
      "total": 1,
      "variations": {
        "Exchange": {
          "total": 1,
          "games": [
            "aisthesis_150803dnas20150507"
          ],
          "ECO": "C41"
        }
      }
    },
    "KingsIndian": {
      "total": 1,
      "variations": {
        "EastIndian": {
          "total": 1,
          "games": [
            "150803dnas_aisthesis20150505"
          ],
          "ECO": "A48"
        }
      }
    },
    "Trompovsky": {
      "total": 1,
      "variations": {
        "2..c5": {
          "total": 1,
          "games": [
            "tinhamodek_aisthesis20150505"
          ],
          "ECO": "A45"
        }
      }
    },
    "Alekhine": {
      "total": 1,
      "variations": {
        "Modern": {
          "total": 1,
          "games": [
            "aisthesis_Robzored20150410"
          ],
          "ECO": "B05"
        }
      }
    },
    "ThreeKnights": {
      "total": 1,
      "games": [
        "barish_aisthesis20150515"
      ],
      "ECO": "C46"
    }
  };

  console.log(counts);
  return  counts;
})();
