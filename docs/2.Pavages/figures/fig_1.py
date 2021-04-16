from ipythonblocks import BlockGrid, colors
grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['White'])
grid[:, 0] = colors['Blue']
grid[:, 5] = colors['Blue']
grid[0, 1:5] = colors['LightGreen']
grid[3, 1:5] = colors['Green']
grid[1:3, 1:3] = colors['Red']
grid[1:3, 3:5] = colors['DarkRed']
grid[0:2, 6:8] = colors['Red']
grid[2:4, 6:8] = colors['DarkRed']

with open("fig_1.html", 'w') as f:
    f.write(grid._repr_html_())
