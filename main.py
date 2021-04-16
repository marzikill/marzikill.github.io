def define_env(env):
  "Hook function"

  @env.macro
  def basthon(exo: str, hauteur: int):
      return f"""<iframe src="https://console.basthon.fr/?from={{ io_url }}{{ page.url }}{exo}" width=100% height="f{hauteur}"></iframe>"""

  @env.macro
  def script(lang: str, nom: str):
      return f"""```{lang}
--8<--- "docs/1.Compte_triangles/triangles/scripts/{nom}"
```"""
