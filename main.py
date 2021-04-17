import os
from ipythonblocks import BlockGrid, colors

def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>

[Lien dans une autre page](https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}../{exo})
"""

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<--- "docs/{env.variables.page.url}../{nom}"
```"""

    @env.macro
    def html_fig(num: int) -> str:
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'


    @env.macro
    def pv_intro():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['White'])
        grid[:, 0] = colors['Blue']
        grid[:, 5] = colors['Blue']
        grid[0, 1:5] = colors['LightGreen']
        grid[3, 1:5] = colors['Green']
        grid[1:3, 1:3] = colors['Red']
        grid[1:3, 3:5] = colors['DarkRed']
        grid[0:2, 6:8] = colors['Red']
        grid[2:4, 6:8] = colors['DarkRed']
        return grid._repr_html_()

    @env.macro
    def trois_motifs():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['White'])
        grid[:, 0] = colors['Blue']
        grid[0, 2:6] = colors['Green']
        grid[0:2, 7:9] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_0():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[:, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_1():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_2():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = (255, 255, 255)
        grid[3, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_3():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[:, 7] = colors['Blue']
        return grid._repr_html_()

    @env.macro
    def rect4x8_4():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1, 4:8] = colors['LightGreen']
        grid[2, 4:8] = colors['Green']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_5():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 6:8] = colors['DarkRed']
        grid[2:4, 6:8] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_6():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 6:8] = colors['Red']
        grid[2, 4:8] = colors['Green']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_7():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1:3, 6:8] = colors['Red']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_8():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1, 4:8] = colors['LightGreen']
        grid[2:4, 6:8] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_9():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = colors['White']
        grid[2:4, 8:10] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_10():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = colors['White']
        grid[2, 6:10] = colors['Green']
        grid[3, 6:10] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_11():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = colors['White']
        grid[3, 8:10] = colors['White']
        grid[1:3, 8:10] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_12():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = colors['White']
        grid[3, 8:10] = colors['White']
        grid[1, 6:10] = colors['Green']
        grid[2, 6:10] = colors['LightGreen']
        grid[3, 4:8] = colors['Green']
        grid[0, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def table_a():
        a = [1, 1, 2, 3]
        b = [1, 1, 3, 4]
        c = [1, 1, 2, 3]
        for n in range(4, 24):
            # On ajoute a[n], puis b[n], puis c[n]
            a.append(a[n-1] + a[n-2] + a[n-4] + 2*b[n-4] + c[n-4])
            b.append(a[n] + b[n-2])
            c.append(a[n] + c[n-4])

        def markdown(a, ni, nf):
            """Renvoie un joli tableau markdown des valeurs de
            la suite a_n pour n dans [ni, nf["""
            ans = "|$n$|"
            for n in range(ni, nf): ans += f"${n}$|"
            ans += "\n|:---:|"
            for n in range(ni, nf): ans += ":---:|"
            ans+= "\n|$a_n$|"
            for n in range(ni, nf): ans += f"${a[n]}$|"
            return ans + "\n\n"

        return markdown(a, 0, 24)
