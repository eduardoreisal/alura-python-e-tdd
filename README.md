
# Python TDD Explorando Testes Unitarios

Repositorio do curso que estou cursando na Alura

<br>
Take a look at coveragerc and pytest.ini, these files have interesting configs
<br>
<br>
Gera um report no formato xml<br>
```bash
pytest --junitxml report.xml
```
<br>
<br>
Roda a Ferramenta de testes para checar se todos os cenarios foram cobertos.<br>
```bash
pytest --cov
```
<br>
<br>
Executa pytest no modo verboso, o que retorna mais informacoes<br>
```bash
pytest -v 
```
<br>
<br>
Executa pytest no modo verboso, mas so testa os testes marcados com a tag bonus<br>
```bash
pytest -vm bonus
```
<br>
<br>
Checa somente o arquivo/pasta especificada. Codigo para pasta, tests para arquivo<br>
```bash
pytest --cov=codigo tests
```

<br>
<br>
Checa o arquivo e retorna o que esta faltando<br>
```bash
pytest --cov=codigo tests/ --cov-report term-missing
```
<br>
<br>
Checa o arquivo e retorna o que estava faltando em formato de relatio usando html<br>
```bash
pytest --cov=codigo tests/ --cov-report html
```
<br>
<br>
Gera um report no formato xml<br>

```bash
pytest --cov=codigo tests/ --cov-report xml
```
