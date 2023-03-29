# marzikill.github.io

- Secondes 
  - [Feuille d'exercices](./Secondes D/5 - Étude qualitative de fonctions/Exercices/3 - Vers le second degré/exo.pdf) 

- Premières
- Terminales NSI
- Terminales STMG

{{ 'test%40test.com' | url_decode }}

   {% assign doclist = site.pages | sort: 'url'  %}
    <ul>
       {% for doc in doclist %}
            {% if doc.name contains '.md' or doc.name contains '.html' %}
                <li><a href="{{ site.baseurl }}{{ doc.url }}">{{ doc.url | url_decode }} <br> {{ doc.name }}</a></li>
            {% endif %}
        {% endfor %}
    </ul>
