# marzikill.github.io

- Secondes 
  - [Feuille d'exercices](./Secondes D/5 - Étude qualitative de fonctions/Exercices/3 - Vers le second degré/exo.pdf) 

- Premières
- Terminales NSI
- Terminales STMG


   {% assign doclist = site.pages | sort: 'url'  %}
    <ul>
       {% for doc in doclist %}
            {% if doc.name contains '.md' or doc.name contains '.html' %}
                <li><a href="{{ site.baseurl }}{{ doc.url }}">{{ doc.url }}</a></li>
            {% endif %}
        {% endfor %}
    </ul>
