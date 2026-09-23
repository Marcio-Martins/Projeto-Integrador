
import unittest

from urna import registrar_voto


class TestUrna(unittest.TestCase):

    def test_registrar_voto_valido(self):
        votos = {}
        brancos = 0
        nulos = 0

        brancos, nulos = registrar_voto(
            '15',
            votos,
            brancos,
            nulos
        )

        self.assertEqual(votos['15'], 1)
        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 0)

    def test_registrar_voto_branco(self):
        votos = {}
        brancos = 0
        nulos = 0

        brancos, nulos = registrar_voto(
            '1',
            votos,
            brancos,
            nulos
        )

        self.assertEqual(brancos, 1)
        self.assertEqual(nulos, 0)
        self.assertEqual(votos, {})

    def test_registrar_voto_nulo(self):
        votos = {}
        brancos = 0
        nulos = 0

        brancos, nulos = registrar_voto(
            'Nulo',
            votos,
            brancos,
            nulos
        )

        self.assertEqual(brancos, 0)
        self.assertEqual(nulos, 1)
        self.assertEqual(votos, {})

    def test_contagem_de_votos(self):
        votos = {}
        brancos = 0
        nulos = 0

        brancos, nulos = registrar_voto(
            '15',
            votos,
            brancos,
            nulos
        )

        brancos, nulos = registrar_voto(
            '15',
            votos,
            brancos,
            nulos
        )

        self.assertEqual(votos['15'], 2)


if __name__ == '__main__':
    unittest.main()