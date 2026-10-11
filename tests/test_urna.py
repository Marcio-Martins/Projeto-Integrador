
import unittest
from unittest.mock import patch

from urna import (
    registrar_voto,
    confirmar_voto,
    solicitar_voto,
    votar_eleitor,
    controle_mesario,
    iniciar_votacao
)


class TestUrna(unittest.TestCase):

    def test_solicitar_voto_valido(self):
        candidatos = {'15': 'Carlos Pedro-PD'}

        with patch('builtins.input', return_value='15'):
            resultado = solicitar_voto('Prefeito', candidatos)

        self.assertEqual(resultado, '15')

    @patch('builtins.input', side_effect=['abc', '15'])
    def test_solicitar_voto_entrada_invalida(self, mock_input):
        candidatos = {'15': 'Carlos Pedro-PD'}

        resultado = solicitar_voto('Prefeito', candidatos)

        self.assertEqual(resultado, '15')
        self.assertEqual(mock_input.call_count, 2)

    def test_registrar_voto_valido(self):
        votos = {}
        candidatos = {'15': 'Carlos Pedro-PD'}

        brancos, nulos = registrar_voto(
            '15', votos, 0, 0, candidatos
        )

        self.assertEqual(votos['15'], 1)
        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 0)

    def test_registrar_voto_branco(self):
        votos = {}
        candidatos = {'15': 'Carlos Pedro-PD', '1': 'Voto Branco'}

        brancos, nulos = registrar_voto(
            '1', votos, 0, 0, candidatos
        )

        self.assertEqual(brancos, 1)
        self.assertEqual(nulos, 0)
        self.assertEqual(votos, {})

    def test_registrar_voto_nulo(self):
        votos = {}

        brancos, nulos = registrar_voto(
            'Nulo', votos, 0, 0, {}
        )

        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 1)
        self.assertEqual(votos, {})

    def test_registrar_voto_candidato_inexistente(self):
        votos = {}
        candidatos = {'15': 'Carlos Pedro-PD'}

        with self.assertRaises(ValueError):
            registrar_voto(
                '999', votos, 0, 0, candidatos
            )

        self.assertEqual(votos, {})

    def test_contagem_de_votos(self):
        votos = {}
        candidatos = {'15': 'Carlos Pedro-PD'}

        registrar_voto('15', votos, 0, 0, candidatos)
        registrar_voto('15', votos, 0, 0, candidatos)

        self.assertEqual(votos['15'], 2)

    @patch('builtins.input', return_value='S')
    def test_confirmar_voto_sim(self, mock_input):
        resultado = confirmar_voto(
            '15', 'Prefeito', {'15': 'Carlos Pedro-PD'}
        )

        self.assertTrue(resultado)

    @patch('builtins.input', return_value='N')
    def test_confirmar_voto_nao(self, mock_input):
        resultado = confirmar_voto(
            '15', 'Prefeito', {'15': 'Carlos Pedro-PD'}
        )

        self.assertFalse(resultado)

    def test_confirmar_voto_branco(self):
        resultado = confirmar_voto(
            '1', 'Prefeito', {'1': 'Voto Branco'}
        )

        self.assertTrue(resultado)

    def test_confirmar_voto_nulo(self):
        resultado = confirmar_voto('Nulo', 'Prefeito', {})

        self.assertTrue(resultado)

    @patch(
        'builtins.input',
        side_effect=['15', 'S', '15112', 'S']
    )
    def test_votar_eleitor(self, mock_input):
        candidatos_prefeito = {'15': 'Carlos Pedro-PD'}
        candidatos_vereador = {'15112': 'Adriana Bela-PD'}

        votos_prefeito = {}
        votos_vereador = {}

        resultado = votar_eleitor(
            candidatos_prefeito,
            candidatos_vereador,
            votos_prefeito,
            votos_vereador,
            0, 0, 0, 0
        )

        self.assertEqual(votos_prefeito['15'], 1)
        self.assertEqual(votos_vereador['15112'], 1)
        self.assertEqual(resultado, (0, 0, 0, 0))

    @patch(
        'builtins.input',
        side_effect=['15', 'N', '21', 'S', '15112', 'S']
    )
    def test_voto_rejeitado_nao_e_contabilizado(self, mock_input):
        candidatos_prefeito = {
            '15': 'Carlos Pedro-PD',
            '21': 'Anderson Silva-PV'
        }
        candidatos_vereador = {'15112': 'Adriana Bela-PD'}

        votos_prefeito = {}
        votos_vereador = {}

        votar_eleitor(
            candidatos_prefeito,
            candidatos_vereador,
            votos_prefeito,
            votos_vereador,
            0, 0, 0, 0
        )

        self.assertNotIn('15', votos_prefeito)
        self.assertEqual(votos_prefeito.get('21'), 1)
        self.assertEqual(votos_vereador.get('15112'), 1)
        self.assertEqual(mock_input.call_count, 6)

    @patch('builtins.input', return_value='1')
    def test_controle_mesario_continuar(self, mock_input):
        self.assertTrue(controle_mesario())

    @patch('builtins.input', return_value='2')
    def test_controle_mesario_encerrar(self, mock_input):
        self.assertFalse(controle_mesario())

    @patch('builtins.input', return_value='1')
    def test_iniciar_votacao(self, mock_input):
        self.assertTrue(iniciar_votacao())

    @patch('builtins.input', return_value='2')
    def test_encerrar_sistema_antes_da_votacao(self, mock_input):
        self.assertFalse(iniciar_votacao())

    @patch('builtins.input', side_effect=['x', 'S'])
    def test_confirmar_voto_resposta_invalida(self, mock_input):
        candidatos = {'15': 'Carlos Pedro-PD'}

        resultado = confirmar_voto(
            '15', 'Prefeito', candidatos
        )

        self.assertTrue(resultado)
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=['0', '1'])
    def test_iniciar_votacao_opcao_invalida(self, mock_input):
        resultado = iniciar_votacao()

        self.assertTrue(resultado)
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=['0', '1'])
    def test_controle_mesario_opcao_invalida(self, mock_input):
        resultado = controle_mesario()

        self.assertTrue(resultado)
        self.assertEqual(mock_input.call_count, 2)


if __name__ == '__main__':
    unittest.main()
