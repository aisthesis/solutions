/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';
  var games = [
    {
      "white": "Meek, Alexander Beaufort",
      "black": "Morphy, Paul",
      "year": "1855",
      "opening": "Scotch Gambit",
      "sources": ["Paul_Morphy (HIARCS) 326"],
      "ECO": "C44"
    },
    {
      "white": "Paulsen, Louis",
      "black": "Morphy, Paul",
      "year": "1857",
      "opening": "Three Knights",
      "sources": ["Paul_Morphy (HIARCS) 289"],
      "ECO": "C46"
    },
    {
      "white": "Morphy, Paul",
      "black": ["Isouard", "Karl, Duke of Brunswick"],
      "year": "1858",
      "opening": "Philidor",
      "sources": ["https://youtu.be/vFnY77FmSeU"]
    },
    {
      "white": "Morphy, Paul",
      "black": "Barnes, Thomas Wilson",
      "year": "1858",
      "opening": "Philidor",
      "sources": ["ClassicGames (HIARCS) 5"]
    },
    {
      "white": "Wygodschikoff, K.",
      "black": "Alekhine, Alexander",
      "year": "1909",
      "opening": "Spanish",
      "sources": ["Aljechin 1908-23 34"],
      "ECO": "C78"
    },
    {
      "white": ["Fleissig, A.", "Staehelin, G."],
      "black": "Alekhine, Alexander",
      "year": "1922",
      "opening": "Scotch",
      "sources": ["Aljechin 1908-23 94"]
    },
    {
      "white": "Pons, A.",
      "black": "Alekhine, Alexander",
      "year": "1926",
      "opening": "Bishop",
      "sources": ["Alexander_Alekhine (HIARCS) 1781"],
      "ECO": "C24"
    },
    {
      "white": "Olafsson, Fridrik",
      "black": "Fischer, Bobby",
      "year": "1959",
      "opening": "Kings Indian",
      "sources": [
        "Fischer Memorable 7",
        "Robert_James_Fischer (HIARCS) 859"
      ],
      "ECO": "E93"
    },
    {
      "white": "Fischer, Bobby",
      "black": "Tal, Mikhail",
      "year": "1959",
      "opening": "Sicilian",
      "sources": ["Fischer Memorable 17"]
    },
    {
      "white": "Reshevsky, Samuel",
      "black": "Fischer, Bobby",
      "year": "1961",
      "opening": "Kings Indian",
      "sources": ["Fischer Memorable 28"],
      "related": [
        "Petrosian_Gligorich 1970",
        "Gligorich_Fischer 1961"
      ]
    },
    {
      "white": "Gligorich, Svetozar",
      "black": "Fischer, Bobby",
      "year": "1961",
      "opening": "Kings Indian",
      "sources": ["Fischer Memorable 30"],
      "related": "Petrosian_Gligorich 1970"
    },
    {
      "white": "Fischer, Bobby",
      "black": "Gligorich, Svetozar",
      "year": "1966",
      "opening": "Spanish",
      "sources": ["Fischer Memorable 56"]
    },
    {
      "black": "Larsen, Bent",
      "white": "Fischer, Bobby",
      "year": "1967",
      "opening": "Kings Indian",
      "sources": [
        "Fischer Memorable 57",
        "Robert_James_Fischer (HIARCS) 682"
      ],
      "ECO": "E97"
    },
    {
      "white": "Petrosian, Tigran",
      "black": "Gligorich, Svetozar",
      "year": "1970",
      "opening": "Kings Indian",
      "sources": [
        "Svetozar_Gligoric (HIARCS), 2160",
        "https://www.youtube.com/watch?v=HFIOzJwUK4o"
      ],
      "related": "Gligorich_Fischer 1961"
    },
    {
      "white": "Ost Hansen, Jacob",
      "black": "Nunn, John",
      "year": "1974",
      "opening": "Vienna",
      "sources": [
        "John_D_M_Nunn (HIARCS) 1708"
      ],
      "ECO": "C27"
    },
    {
      "white": "Karpov, Anatoly",
      "black": "Kupreichik, Viktor D.",
      "year": "1976",
      "opening": "Spanish",
      "sources": [
        "Anatoly_Karpov (HIARCS) 1548"
      ],
      "ECO": "C61"
    },
    {
      "white": "Kasparov, Garry",
      "black": "Gicin",
      "year": "1977",
      "opening": "Alekhine",
      "sources": [
        "Garry_Kasparov (HIARCS) 1399"
      ],
      "related": ["aisthesis_Robzored 2015"]
    },
    {
      "white": "Tseshkovsky, Vitaly",
      "black": "Jussupow, Artur",
      "year": "1981",
      "opening": "Bishop",
      "sources": [ "Relevant (HIARCS) 31" ],
      "ECO": "C24"
    },
    {
      "white": "Shirov, Alexei",
      "black": "Kasparov, Garry",
      "year": "1992",
      "opening": "Kings Indian",
      "sources": ["Garry_Kasparov (HIARCS) 1942"],
      "related": [
        "Gligorich_Fischer 1961",
        "Petrosian_Gligorich 1970"
      ]
    },
    {
      "white": "Tal, Mikhail",
      "black": "Korchnoi, Viktor",
      "year": "1987",
      "opening": "Spanish",
      "sources": ["Mikhail__Tal (HIARCS) 168"],
      "transposesTo": ["1.e4,e5 2.Nf3,Nc6 3.Bb5,Nf6 4.d4,Ne4: 5.0-0,a6 6.Ba4"]
    },
    {
      "white": "Hort, Vlastimil",
      "black": "Geller, Efim",
      "year": "1989",
      "opening": "Spanish",
      "sources": ["Vlastimil_Hort (HIARCS) 318"],
      "ECO": "C69"
    },
    {
      "white": "Morozevich, Alexander",
      "black": "Kasparov, Garry",
      "year": "1995",
      "opening": "Kings Gambit",
      "sources": ["Garry_Kasparov (HIARCS) 1858"],
      "ECO": "C34"
    },
    {
      "white": "150803dnas",
      "black": "aisthesis",
      "year": "2015",
      "opening": "Kings Indian",
      "sources": ["MyGames (HIARCS) 24"]
    },
    {
      "white": "tinhamodek",
      "black": "aisthesis",
      "year": "2015",
      "opening": "Trompovsky Attack",
      "sources": ["MyGames (HIARCS) 27"]
    },
    {
      "white": "aisthesis",
      "black": "Robzored",
      "year": "2015",
      "opening": "Alekhine",
      "sources": ["MyGames (HIARCS) 28"],
      "related": ["Kasparov_Gicin 1977"]
    }
  ];
  console.log(games);
  return  games;
})();
