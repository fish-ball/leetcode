/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    for(var i = 0; i < grid.length; ++i) {
        for(var j = 0; j < grid[i].length; ++j) {
            if(i == 0 && j == 0) continue;
            else if(i == 0) grid[i][j] += grid[i][j-1];
            else if(j == 0) grid[i][j] += grid[i-1][j];
            else grid[i][j] += Math.min(grid[i][j-1], grid[i-1][j]);
        }
    }
    return grid[grid.length-1][grid[0].length-1];
};
