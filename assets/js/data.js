  var nodes = [
    { id: 1, x:38, y:45 },
    { id: 2, x:38, y:150 },
    { id: 3, x:38, y:255 },
    { id: 4, x:38, y:360 },
    { id: 5, x:38, y:463 },
    { id: 6, x:125, y:45 },
    { id: 7, x:1, y:3 },
    { id: 8, x:1, y:2 },
    { id: 9, x:1, y:1 },
    { id: 10, x:1, y:0 },
    { id: 11, x:2, y:4 },
    { id: 12, x:2, y:3 },
    { id: 13, x:2, y:2 },
    { id: 14, x:2, y:1 },
    { id: 15, x:2, y:0 },
    { id: 16, x:3, y:4 },
    { id: 17, x:3, y:2 },
    { id: 18, x:3, y:1 },
    { id: 19, x:4, y:4 },
    { id: 20, x:4, y:3 },
    { id: 21, x:4, y:2 },
    { id: 22, x:4, y:1 },
    { id: 23, x:5, y:4 },
    { id: 24, x:5, y:2 },
    { id: 25, x:5, y:1 },
    { id: 26, x:6, y:4 },
    { id: 27, x:6, y:3 },
    { id: 28, x:6, y:2 },
    { id: 29, x:6, y:1 },
    { id: 30, x:6, y:0 },
    { id: 31, x:7, y:4 },
    { id: 32, x:7, y:3 },
    { id: 33, x:7, y:2 },
    { id: 34, x:7, y:1 },
    { id: 35, x:7, y:0 },
    { id: 36, x:8, y:1 },
    { id: 37, x:8, y:0 },
  ];

  var n = function(node) {
    return nodes[node-1];
  }

  var l = [0, 45, 150, 255, 360, 463];
  var c = [0, 38, 125, 210, 298, 383, 470, 557, 642, 729];


  var data = [
              [c[1],l[1], 1],
              [c[1],l[2], 2],
              [c[1],l[3], 3],
              [c[1],l[4], 10],
              [c[1],l[5], 6],
              [c[2],l[1], 10],
              [c[2],l[2], 10],
              [c[2],l[3], 10],
              [c[2],l[4], 10],
              [c[2],l[5], 3],
              [c[3],l[1], 4],

              [c[4],l[1], 2],

              [c[5],l[1], 11],

              [c[6],l[1], 14],

              [c[7],l[1], 13],

              [c[8],l[1], 12],

              [c[9],l[5], 15],

              [c[5],l[4], 19],
              [c[5],l[3], 16],
              [c[4],l[4], 17],
              // [l[3],c[1], 10],
              // [l[4],c[1], 10],
              // [l[5],c[1], 10],
              // [n(2)['x'], n(2)['y'], 10],
              // [n(3)['x'], n(3)['y'], 10],
              // [n(4)['x'], n(4)['y'], 10],
              // [n(5)['x'], n(5)['y'], 10],
              // [n(6)['x'], n(6)['y'], 10],
              // // [n(11)['x'], n(11)['y'], 10],
              // [n(16)['x'], n(16)['y'], 10],
              // [n(19)['x'], n(19)['y'], 10],
              // [n(23)['x'], n(23)['y'], 10],
              // [n(26)['x'], n(26)['y'], 10],
              // [n(31)['x'], n(31)['y'], 10],
              // [n(36)['x'], n(36)['y'], 10],
             ];