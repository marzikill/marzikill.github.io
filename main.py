def define_env(env):
  "Hook function"

  @env.macro
  def basthon(exo: str, hauteur: int):
      return f'<iframe src="https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}{exo}" width=100% height={hauteur}></iframe>'

  @env.macro
  def script(lang: str, nom: str):
      return f"""```{lang}
--8<--- "docs/{env.variables.page.url}{nom}"
```"""
