
# Python TDD Explorando Testes Unitarios

Repositorio do curso que estou cursando na Alura

<br>
Take a look at coveragerc and pytest.ini, these files have interesting configs

<br>
Gera um report no formato xml
```bash
pytest --junitxml report.xml
```

<br>
Roda a Ferramenta de testes para checar se todos os cenarios foram cobertos.
```bash
pytest --cov
```
<br>
Executa pytest no modo verboso, o que retorna mais informacoes
```bash
pytest -v 
```
<br>
Executa pytest no modo verboso, mas so testa os testes marcados com a tag bonus
```bash
pytest -vm bonus
```
<br>
Checa somente o arquivo/pasta especificada. Codigo para pasta, tests para arquivo
```bash
pytest --cov=codigo tests
```

<br>
Checa o arquivo e retorna o que esta faltando
```bash
pytest --cov=codigo tests/ --cov-report term-missing
```

<br>
Checa o arquivo e retorna o que estava faltando em formato de relatio usando html
```bash
pytest --cov=codigo tests/ --cov-report html
```
<br>
Gera um report no formato xml

```bash
pytest --cov=codigo tests/ --cov-report xml
```
