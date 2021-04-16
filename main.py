def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f'<iframe src="https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}{exo}" width=100% height={hauteur}></iframe>'

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<--- "docs/{env.variables.page.url}{nom}"
```"""

    @env.macro
    def html_fig(num: int):
        "Renvoie le code HTML de la figure n° `num`"
        # ex: --8<-- "docs/2.pavages/figures/fig_1.html"
        return f'--8<-- "docs/{env.variables.page.url}figures/fig_{num}.html"'

