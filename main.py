def define_env(env):
  "Hook function"

  @env.macro
  def basthon(exo: str, hauteur: int):
      nom = exo.rstrip(".py")
      return f"""<iframe src="https://console.basthon.fr/?from={{ io_url }}{{ page.url }}/../{nom}.py" width="2500" height="f{hauteur}"></iframe>"""

