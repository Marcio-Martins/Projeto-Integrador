
import unittest
from unittest.mock import patch

from urna import exibir_resultado
from urna import criar_candidatos
from urna import (
    registrar_voto,
    confirmar_voto,
    solicitar_voto,
    votar_eleitor,
    controle_mesario,
    iniciar_votacao
)


class TestUrna(unittest.TestCase):

    def test_criar_candidatos_retorna_dicionarios_independentes(self):
        candidatos_prefeito_1, candidatos_vereador_1 = criar_candidatos()
        candidatos_prefeito_2, candidatos_vereador_2 = criar_candidatos()

        candidatos_prefeito_1["99"] = "Candidato de teste"
        candidatos_vereador_1["99999"] = "Candidato de teste"

        self.assertNotIn("99", candidatos_prefeito_2)
        self.assertNotIn("99999", candidatos_vereador_2)

    def test_criar_candidatos_prefeito(self):
        candidatos_prefeito, _ = criar_candidatos()

        self.assertEqual(
            candidatos_prefeito["15"],
            "Carlos Pedro-PD"
        )
        self.assertEqual(
            candidatos_prefeito["21"],
            "Anderson Silva-PV"
        )
        self.assertEqual(
            candidatos_prefeito["35"],
            "Marta Rocha-PL"
        )
        self.assertEqual(candidatos_prefeito["1"], "Voto Branco")

    def test_criar_candidatos_vereador(self):
        _, candidatos_vereador = criar_candidatos()

        self.assertEqual(
            candidatos_vereador["15112"],
            "Adriana Bela-PD"
        )
        self.assertEqual(
            candidatos_vereador["15121"],
            "Carlos Alberto-PD"
        )
        self.assertEqual(
            candidatos_vereador["1"],
            "Voto Branco"
        )


    def test_solicitar_voto_aceita_espacos(self):
        candidatos = {"15": "Carlos Pedro-PD"}

        with patch("builtins.input", return_value="  15  "):
            resultado = solicitar_voto("Prefeito", candidatos)

        self.assertEqual(resultado, "15")

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

    @patch('builtins.input', return_value='S')
    def test_confirmar_voto_nulo(self, mock_input):
        resultado = confirmar_voto('Nulo', 'Prefeito', {})

        self.assertTrue(resultado)
        mock_input.assert_called_once_with(
            'Confirma voto nulo? [S/N]: '
        )


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



    def test_exibir_resultado_varios_candidatos_prefeito(self):
        votos = {"15": 3, "21": 1}
        candidatos = {
            "15": "Carlos Pedro-PD",
            "21": "Anderson Silva-PV",
            "35": "Marta Rocha-PL",
            "1": "Voto Branco",
        }

        with patch("builtins.print") as imprimir:
            exibir_resultado(votos, candidatos, "Prefeito", 2, 1)

        chamadas = [str(chamada) for chamada in imprimir.call_args_list]
        texto = "\\n".join(chamadas)
        self.assertIn("15 - Carlos Pedro-PD: 3 voto(s)", texto)
        self.assertIn("21 - Anderson Silva-PV: 1 voto(s)", texto)
        self.assertIn("35 - Marta Rocha-PL: 0 voto(s)", texto)
        self.assertIn("Votos brancos: 2", texto)
        self.assertIn("Votos nulos: 1", texto)
        self.assertNotIn("1 - Voto Branco", texto)

    def test_exibir_resultado_varios_candidatos_vereador(self):
        votos = {"15112": 4, "15121": 2, "15221": 1}
        candidatos = {
            "15112": "Adriana Bela-PD",
            "15121": "Carlos Alberto-PD",
            "15221": "Sandro Pereira-PD",
            "1": "Voto Branco",
        }

        with patch("builtins.print") as imprimir:
            exibir_resultado(votos, candidatos, "Vereador", 3, 2)

        chamadas = [str(chamada) for chamada in imprimir.call_args_list]
        texto = "\\n".join(chamadas)
        self.assertIn("15112 - Adriana Bela-PD: 4 voto(s)", texto)
        self.assertIn("15121 - Carlos Alberto-PD: 2 voto(s)", texto)
        self.assertIn("15221 - Sandro Pereira-PD: 1 voto(s)", texto)
        self.assertIn("Votos brancos: 3", texto)
        self.assertIn("Votos nulos: 2", texto)
        self.assertNotIn("1 - Voto Branco", texto)



    def test_confirmar_voto_branco_permitido(self):
        candidatos = {'15': 'Carlos Pedro', '1': 'Voto Branco'}

        self.assertTrue(confirmar_voto('1', 'Prefeito', candidatos))

    def test_confirmar_voto_branco_nao_permitido(self):
        candidatos = {'15': 'Carlos Pedro'}

        with patch('builtins.print'):
            self.assertFalse(
                confirmar_voto('1', 'Prefeito', candidatos)
            )
    @patch('builtins.input', side_effect=['999', '15'])
    def test_solicitar_voto_numero_inexistente(self, mock_input):
        candidatos = {'15': 'Carlos Pedro-PD'}

        resultado = solicitar_voto('Prefeito', candidatos)

        self.assertEqual(resultado, 'Nulo')
        self.assertEqual(mock_input.call_count, 1)

    @patch('builtins.input', side_effect=['15', 'N', '15', 'S'])
    def test_voto_cancelado_e_confirmado_na_tentativa_seguinte(
        self, mock_input
    ):
        candidatos = {'15': 'Carlos Pedro-PD'}
        votos = {}

        brancos, nulos = 0, 0

        from urna import votar_cargo

        brancos, nulos = votar_cargo(
            'Prefeito', candidatos, votos, brancos, nulos
        )

        self.assertEqual(votos['15'], 1)
        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 0)
        self.assertEqual(mock_input.call_count, 4)

    def test_registrar_voto_branco_sem_permissao(self):
        candidatos = {'15': 'Carlos Pedro-PD'}
        votos = {}

        with self.assertRaises(ValueError):
            registrar_voto('1', votos, 0, 0, candidatos)

        self.assertEqual(votos, {})

    @patch('builtins.input', side_effect=['999', 'N', '15', 'S'])
    def test_voto_invalido_corrigido_para_candidato(self, mock_input):
        candidatos = {'15': 'Carlos Pedro-PD'}
        votos = {}

        from urna import votar_cargo

        brancos, nulos = votar_cargo(
            'Prefeito', candidatos, votos, 0, 0
        )

        self.assertEqual(votos, {'15': 1})
        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 0)

    @patch('builtins.input', side_effect=['999', 'S'])
    def test_voto_invalido_confirmado_como_nulo(self, mock_input):
        candidatos = {'15': 'Carlos Pedro-PD'}
        votos = {}

        from urna import votar_cargo

        brancos, nulos = votar_cargo(
            'Prefeito', candidatos, votos, 0, 0
        )

        self.assertEqual(votos, {})
        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 1)

if __name__ == '__main__':
    unittest.main()
