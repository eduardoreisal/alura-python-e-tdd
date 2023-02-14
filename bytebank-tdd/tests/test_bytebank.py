from codigo.funcionario import Funcionario
import pytest
import datetime
from pytest import mark

class TestClass: 
    def esperado(self):
        today = datetime.date.today()
        year = today.year
        return int(year) - 2000

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
       # Given, When, Then 
       # Given -> Dado contexto
        esperado = self.esperado()
        entrada = '13/03/2000'

        funcionario_test = Funcionario('Test', entrada, 2500)
        # When - acao
        resultado = funcionario_test.idade()
        # Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 5000)
        resultado = lucas.sobrenome() # When
        assert resultado == esperado # Then


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 
        entrada_nome = 'Paulo Braganca'
        esperado = 90000 
        funcionario_test = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario
        assert resultado == esperado

    def test_quando_decrescimo_recebe_valor_e_nao_e_socio_nao_deve_descontar(self):
        funcionario_test = Funcionario('Eduardo Alvarenga', '11/11/1999', 10000)
        esperado = salario_antigo = funcionario_test.salario
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario
        assert resultado == esperado

    def test_quando_chamar_print_em_funcionario_printa_informacao_correta(self):
        funcionario = Funcionario('Eduardo Alvarenga', '10/10/1999', 100000)
        esperado = f'Funcionario(Eduardo Alvarenga, 10/10/1999, 100000)'
        resultado = funcionario.__str__()
        assert resultado == esperado

    @mark.bonus
    def test_quando_salario_for_menor_que_10_mil_retorna_um_bonus_de_10_porcento(self):
        salario = 9000 
        esperado = 900
        funcionario_test = Funcionario('Test Test', '11/11/2000', salario)
        resultado = funcionario_test.calcular_bonus()
        assert resultado == esperado

    @mark.bonus
    def test_quando_salario_for_maior_que_10_mil_retorna_exception(self):
        with pytest.raises(Exception):
            salario = 10001
            funcionario_test = Funcionario('Test Test', '11/11/2000', salario)
            resultado = funcionario_test.calcular_bonus()
            assert resultado

    @mark.skip
    def test_quando_salario_for_maior_que10_mil_retorna_exception(self):
        with pytest.raises(Exception):
            salario = 10001
            funcionario_test = Funcionario('Test Test', '11/11/2000', salario)
            resultado = funcionario_test.calcular_bonus()
            assert resultado
