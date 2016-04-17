/**
 * Created 2015-05-04
 * Copyright (c) 2015 Marshall Farrier
 */

(function() {
  'use strict';

  var repertoire = {
    '1.e4,c6 2.d4,d5': {
      '3.Nd2': 'Karpov',
      '3.Nf3,de4: 4.Ne4:,Bf5':{
        'name': 'Classical',
        '5.Ng3,Bg6 6.h4,h6 7.Nf3,Nd7 8.h5': {
          'name': 'Spassky',
          '8..Bh7 9.Bd3,Bd3: 10.Qd3:': {
            'players': ['Tal', 'Karpov', 'Adams']
            '10..Qc7': {},
            '10..Ngf6': {},
            '10..e6': {
              '11.Bf4': {},
              '11.Bd2': {
                'Adams_Nakamura2012': ['HIARCS']
              },
            }
          },
        }
      }
    }
  };
  return  repertoire;
})();
